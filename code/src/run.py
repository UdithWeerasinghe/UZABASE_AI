import argparse
import logging
from pyspark.sql import SparkSession
import yaml
from process_data import process_selected_words
from process_data_all import process_all_words

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("logs/run_logs.txt"),  # Save logs to a .txt file
        logging.StreamHandler()  # Print logs to the console
    ]
)
logger = logging.getLogger(__name__)

def load_config(config_path: str) -> dict:
    """
    Load configuration from a YAML file.

    Args:
        config_path (str): Path to the YAML configuration file.

    Returns:
        dict: Configuration as a dictionary.
    """
    logger.info(f"Loading configuration from {config_path}")
    with open(config_path, "r") as file:
        return yaml.safe_load(file)

def main():
    """
    Main function to process AG News dataset based on command-line arguments.
    """
    parser = argparse.ArgumentParser(description="Process AG News dataset.")
    subparsers = parser.add_subparsers(dest="command")

    # Parser for process_data
    parser_process = subparsers.add_parser("process_data")
    parser_process.add_argument("--cfg", required=True, help="Path to config file")
    parser_process.add_argument("--dirout", required=True, help="Output directory")
    parser_process.add_argument("-dataset", required=True, help="Dataset name (news)")

    # Parser for process_data_all
    parser_process_all = subparsers.add_parser("process_data_all")
    parser_process_all.add_argument("--cfg", required=True, help="Path to config file")
    parser_process_all.add_argument("--dirout", required=True, help="Output directory")
    parser_process_all.add_argument("-dataset", required=True, help="Dataset name (news)")

    args = parser.parse_args()
    spark = SparkSession.builder.appName("WordProcessing").getOrCreate()





    if args.command == "process_data":
        logger.info("Running process_data command")
        config = load_config(args.cfg)
        process_selected_words(spark, config["dataset_name"], config["selected_words"], args.dirout)
    elif args.command == "process_data_all":
        logger.info("Running process_data_all command")
        config = load_config(args.cfg)
        process_all_words(spark, config["dataset_name"], args.dirout)

if __name__ == "__main__":
    main()


