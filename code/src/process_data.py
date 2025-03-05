import logging
import os
from pyspark.sql import SparkSession
from pyspark.sql.functions import col
import yaml
from pathlib import Path
from datasets import load_dataset
import pandas as pd

# Ensure logs directory exists
os.makedirs("logs", exist_ok=True)

# Configure logging
logging.basicConfig(
    level=logging.DEBUG,  # Use DEBUG for local debugging
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("logs/data_processed.txt", mode="w"),  # Overwrite log file
        logging.StreamHandler()  # Print logs to the console
    ]
)
logger = logging.getLogger(__name__)

def load_config(config_path: str) -> dict:
    """Load configuration from a YAML file."""
    logger.info(f"Loading configuration from {config_path}")
    with open(config_path, "r") as file:
        return yaml.safe_load(file)

def process_selected_words(spark: SparkSession, dataset_path: str, selected_words: list, output_dir: str) -> None:
    """Process selected words and save the result as a parquet file."""
    logger.info(f"Processing selected words: {selected_words}")
    
    dataset = spark.read.option("header", True).csv(dataset_path)
    
    word_counts = []
    for word in selected_words:
        count = dataset.filter(col("description").contains(word)).count()
        word_counts.append((word, count))
        logger.debug(f"Word: {word}, Count: {count}")
    
    df_output = spark.createDataFrame(word_counts, ["word", "count"])
    output_path = Path(output_dir) / f"word_count_{pd.Timestamp.today().strftime('%Y%m%d')}.parquet"
    df_output.write.parquet(str(output_path))
    logger.info(f"Processed data saved to {output_path}")
    
    # Explicitly flush logs
    for handler in logger.handlers:
        handler.flush()







