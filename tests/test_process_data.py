import unittest
import os
from pathlib import Path
from pyspark.sql import SparkSession
import sys
import pandas as pd

# Add the src directory to the Python path
sys.path.append(os.path.join(os.path.dirname(__file__), "..", "code", "src"))

# Import the modules
from process_data import process_selected_words
from process_data_all import process_all_words

class TestWordProcessing(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """Set up Spark session for testing."""
        cls.spark = SparkSession.builder.appName("TestWordProcessing").getOrCreate()

    @classmethod
    def tearDownClass(cls):
        """Stop Spark session after all tests."""
        cls.spark.stop()

    def test_process_selected_words(self):
        """Test the processing of selected words."""
        test_data = [
            {"description": "The president is in Asia."},
            {"description": "The president is not in Asia."},
            {"description": "Asia is a continent."}
        ]
        test_df = self.spark.createDataFrame(test_data)

        # Save test data as JSONL format
        test_path = "test_data.jsonl"
        test_df.write.mode("overwrite").json(test_path)

        selected_words = ["president", "the", "Asia"]
        output_dir = "ztmp/data/"
        os.makedirs(output_dir, exist_ok=True)

        # Process selected words
        process_selected_words(self.spark, test_path, selected_words, output_dir)

        # Check if output directory exists
        output_folder = Path(output_dir) / f"word_count_{pd.Timestamp.today().strftime('%Y%m%d')}.parquet"
        self.assertTrue(output_folder.exists() and output_folder.is_dir(), f"Expected folder {output_folder} does not exist.")

        # Check for Parquet files inside the folder
        parquet_files = list(output_folder.glob("*.parquet"))
        self.assertTrue(len(parquet_files) > 0, "No Parquet files found in the output directory.")

        # Cleanup
        self._cleanup(output_dir, test_path)

    def test_process_all_words(self):
        """Test the processing of all words in the dataset."""
        test_data = [
            {"description": "The president is in Asia."},
            {"description": "The president is not in Asia."},
            {"description": "Asia is a continent."}
        ]
        test_df = self.spark.createDataFrame(test_data)

        test_dir = "test_data_all"
        os.makedirs(test_dir, exist_ok=True)
        test_df.write.mode("overwrite").json(test_dir)

        # Get the actual JSON file inside the folder
        json_files = [f for f in os.listdir(test_dir) if f.startswith("part-")]
        if not json_files:
            self.fail("No JSON files were written in test_data_all.")
        test_path = os.path.join(test_dir, json_files[0])

        output_dir = "ztmp/data/"
        os.makedirs(output_dir, exist_ok=True)

        # Process all words
        process_all_words(self.spark, test_path, output_dir)

        # Check if output directory exists
        output_folder = Path(output_dir) / f"word_count_all_{pd.Timestamp.today().strftime('%Y%m%d')}.parquet"
        self.assertTrue(output_folder.exists() and output_folder.is_dir(), f"Expected folder {output_folder} does not exist.")

        # Check for Parquet files inside the folder
        parquet_files = list(output_folder.glob("*.parquet"))
        self.assertTrue(len(parquet_files) > 0, "No Parquet files found in the output directory.")

        # Cleanup
        self._cleanup(output_dir, test_path, test_dir)

    def _cleanup(self, output_dir, *paths):
        """Remove test files and directories."""
        for path in paths:
            if os.path.isfile(path):
                os.remove(path)
            elif os.path.isdir(path):
                for file in os.listdir(path):
                    os.remove(os.path.join(path, file))
                os.rmdir(path)

        if os.path.exists(output_dir):
            for item in os.listdir(output_dir):
                item_path = os.path.join(output_dir, item)
                if os.path.isfile(item_path):
                    os.remove(item_path)
                elif os.path.isdir(item_path):
                    for sub_file in os.listdir(item_path):
                        os.remove(os.path.join(item_path, sub_file))
                    os.rmdir(item_path)
            os.rmdir(output_dir)

if __name__ == "__main__":
    unittest.main()
