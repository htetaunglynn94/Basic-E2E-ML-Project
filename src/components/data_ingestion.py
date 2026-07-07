import os
import sys
from src.exception import CustomException
from src.logger import logging
import pandas as pd
from sklearn.model_selection import train_test_split as TTS
from dataclasses import dataclass # use as decorator

from src.components.data_transformation import DataTransformation, DataTransformationConfig
from src.components.model_trainer import ModelTrainerConfig, ModelTrainer

@dataclass
class DataIngestionConfig:
    train_data_path: str = os.path.join('artifacts', 'train.csv')
    test_data_path : str = os.path.join('artifacts', 'test.csv')
    raw_data_path  : str = os.path.join('artifacts', 'raw.csv')

class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info("Entered data ingestion method or component.")
        try:
            # 1. Read the source dataset into a Pandas DataFrame
            df = pd.read_csv('notebook/data/stud.csv') # locally loaded (later cloud based)
            logging.info("Read dataset as dataframe.")

            # 2. Extract folder name ('artifacts') and create it if it doesn't exist
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok=True)
            # 3. Save the full, untouched dataset into the raw data path
            df.to_csv(self.ingestion_config.raw_data_path, index=False, header=True)

            # 4. Split data: 80% for training, 20% for testing (fixed random seed for consistency)
            logging.info("Train-Test-Split initiated.")
            train_set, test_set = TTS(df, test_size=0.2, random_state=42)

            # 5. Save the split datasets to their respective target paths
            train_set.to_csv(self.ingestion_config.train_data_path, index=False, header=True)
            test_set.to_csv(self.ingestion_config.test_data_path, index=False, header=True)

            logging.info("Data ingestion completed.")

            # 6. Return the file paths so the next pipeline component knows where to look
            return (self.ingestion_config.train_data_path, 
                    self.ingestion_config.test_data_path)

        except Exception as e:
            # If anything goes wrong, catch the error and pass it to your CustomException handler
            raise CustomException(e, sys)

if __name__ == "__main__":
    obj = DataIngestion()
    train_data, test_data = obj.initiate_data_ingestion()
    data_transformation = DataTransformation()
    train_arr, test_arr, _ = data_transformation.initiate_data_transformation(train_data, test_data)
    modeltrainer = ModelTrainer()
    md_name, r2_val = modeltrainer.initiate_model_trainer(train_arr, test_arr)

    print(f"Best Model Name: {md_name} | R2 Score: {r2_val:.2f}")
