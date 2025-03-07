import logging
import os
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, split, explode
import yaml
from pathlib import Path
import pandas as pd

# Ensure logs directory exists
os.makedirs("logs", exist_ok=True)

# Configure logging
logging.basicConfig(
    level=logging.DEBUG,  
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("logs/data_processed_all.txt", mode="w"),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)
logging.getLogger("py4j").setLevel(logging.WARNING)

logger.info("Process started") 

def load_config(config_path: str) -> dict:
    """Load configuration from a YAML file."""
    logger.info(f"Loading configuration from {config_path}")
    with open(config_path, "r") as file:
        return yaml.safe_load(file)

def process_all_words(spark: SparkSession, dataset_path: str, output_dir: str) -> None:
    """Process all words and save the result as a parquet file."""
    logger.info("Processing all words in the dataset")
    
    dataset = spark.read.json(dataset_path)
    
    words = dataset.select(explode(split(col("description"), " ")).alias("word"))
    
    word_counts = words.groupBy("word").count()
    logger.debug(f"Total unique words processed: {word_counts.count()}")
    
    output_path = Path(output_dir) / f"word_count_all_{pd.Timestamp.today().strftime('%Y%m%d')}.parquet"
    word_counts.write.mode("overwrite").parquet(str(output_path))
    logger.info(f"Processed all words saved to {output_path}")
    
    for handler in logger.handlers:
        handler.flush()




