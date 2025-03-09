import unittest
from pyspark.sql import SparkSession
import os
from pathlib import Path
import sys

# Add the src directory to the Python path
sys.path.append(os.path.join(os.path.dirname(__file__), "..", "code", "src"))

# Now import the module
from process_data_all import process_all_words

class TestProcessDataAll(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.spark = SparkSession.builder.appName("TestWordProcessingAll").getOrCreate()

    @classmethod
    def tearDownClass(cls):
        cls.spark.stop()

    def test_process_all_words(self):
        # Create a temporary JSONL file for testing
        test_data = [
            {"description": "The president is in Asia."},
            {"description": "The president is not in Asia."},
            {"description": "Asia is a continent."}
        ]
        test_df = self.spark.createDataFrame(test_data)
        test_path = "test_data_all.jsonl"
        test_df.write.json(test_path)

        # Define output directory
        output_dir = "ztmp/data"
        os.makedirs(output_dir, exist_ok=True)

        # Process all words
        process_all_words(self.spark, test_path, output_dir)

        # Check if the output file exists
        output_path = Path(output_dir) / "word_count_all_20231010.parquet"
        self.assertTrue(output_path.exists())

        # Clean up
        os.remove(test_path)
        for file in os.listdir(output_dir):
            os.remove(os.path.join(output_dir, file))
        os.rmdir(output_dir)

if __name__ == "__main__":
    unittest.main()