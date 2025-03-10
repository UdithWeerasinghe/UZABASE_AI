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
logging.getLogger("py4j").setLevel(logging.WARNING)


def load_config(config_path: str) -> dict:
    """
    Load configuration from a YAML file.

    Args:
        config_path (str): Path to the YAML configuration file.

    Returns:
        dict: Configuration data loaded from the YAML file.
    """
    logger.info(f"Loading configuration from {config_path}")
    with open(config_path, "r") as file:
        return yaml.safe_load(file)


def process_selected_words(spark: SparkSession, dataset_path: str, selected_words: list, output_dir: str) -> None:
    """
    Process selected words from a JSONL dataset and save the word count as a Parquet file.

    Args:
        spark (SparkSession): The active Spark session.
        dataset_path (str): Path to the dataset file in JSONL format.
        selected_words (list[str]): List of words to count in the dataset.
        output_dir (str): Directory where the output Parquet file should be saved.

    Returns:
        None
    """
    logger.info(f"Processing selected words: {selected_words}")

    # Read JSONL file
    dataset = spark.read.json(dataset_path)

    # Ensure 'description' column exists
    if "description" not in dataset.columns:
        logger.error("The dataset does not contain a 'description' column.")
        return

    word_counts = []
    for word in selected_words:
        count = dataset.filter(col("description").contains(word)).count()
        word_counts.append((word, count))

    # Create DataFrame for output
    df_output = spark.createDataFrame(word_counts, ["word", "count"])

    # Save result to local Parquet file
    output_path = Path(output_dir) / f"word_count_{pd.Timestamp.today().strftime('%Y%m%d')}.parquet"
    
    # Save as Parquet to local filesystem
    df_output.write.mode("overwrite").parquet(str(output_path))
    logger.info(f"Processed data saved to {output_path}")

    # Optionally, print the word counts to the console
    for word, count in word_counts:
        # print(f"Word: {word}, Count: {count}")
        logger.info(f"Word: {word}, Count: {count}")

    # Explicitly flush logs
    for handler in logger.handlers:
        handler.flush()






