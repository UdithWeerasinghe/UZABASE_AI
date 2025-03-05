import unittest
import os
from pyspark.sql import SparkSession
from process_data import process_selected_words
from process_data_all import process_all_words
from pathlib import Path

class TestWordProcessing(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.spark = SparkSession.builder.appName("TestWordProcessing").getOrCreate()
        cls.test_output_dir = "test_outputs/"
        os.makedirs(cls.test_output_dir, exist_ok=True)

    @classmethod
    def tearDownClass(cls):
        cls.spark.stop()
    
    def test_process_selected_words(self):
        test_data = self.spark.createDataFrame(
            [("The president spoke today.",), ("The weather is nice.",)], ["description"]
        )
        process_selected_words(self.spark, test_data, ["president", "the"], self.test_output_dir)
        
        parquet_files = list(Path(self.test_output_dir).glob("word_count_*.parquet"))
        self.assertGreater(len(parquet_files), 0, "Parquet file was not created for selected words!")

    def test_process_all_words(self):
        test_data = self.spark.createDataFrame(
            [("Today is a good day.",), ("Learning is fun.",)], ["description"]
        )
        process_all_words(self.spark, test_data, self.test_output_dir)
        
        parquet_files = list(Path(self.test_output_dir).glob("word_count_all_*.parquet"))
        self.assertGreater(len(parquet_files), 0, "Parquet file was not created for all words!")

if __name__ == "__main__":
    unittest.main()
