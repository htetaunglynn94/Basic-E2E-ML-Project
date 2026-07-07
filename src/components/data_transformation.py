import sys
import os
import numpy as np 
import pandas as pd 
from dataclasses import dataclass

from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

from src.exception import CustomException
from src.utils import save_object
from src.logger import logging

@dataclass
class DataTransformationConfig:
    preprocessor_path: str = os.path.join('artifacts', 'preprocessor.pkl')

class DataTransformation:
    def __init__(self):
        self.data_transformation_config = DataTransformationConfig()

    def get_data_transformer(self):
        """
        This function is dedicated for data transformation (preprocessing).
        """
        try:
            numerical_cols = ['writing_score','reading_score']
            categorical_cols = ['gender', 'race_ethnicity', 'parental_level_of_education',
                                 'lunch', 'test_preparation_course']

            num_pipeline = Pipeline(steps=[("Imputer", SimpleImputer(strategy='median')),
                                           ("Scaler", StandardScaler())])                       

            logging.info("Numerical columns scaling completed.")

            cat_pipeline = Pipeline(steps=[("Imputer", SimpleImputer(strategy='most_frequent')),
                                           ("One-hot Encoder", OneHotEncoder(sparse_output=False)),
                                           ("Scaler", StandardScaler())])
            logging.info("Categorical columns encoding completed.")

            preprocessor = ColumnTransformer([("numerical pipeline", num_pipeline, numerical_cols),
                                              ("categorical pipeline", cat_pipeline, categorical_cols)])
            logging.info("Data preprocessing completed.")

            return preprocessor

        except Exception as e:
            raise CustomException(e, sys)

    def initiate_data_transformation(self, train_path, test_path):
        try:
            train_df = pd.read_csv(train_path)
            test_df  = pd.read_csv(test_path)
            logging.info("Read train and test data.")
            logging.info("Obtaining preprocessing objects.")

            preprocessing_obj = self.get_data_transformer()
            target_col = "math_score"
            numerical_cols = ['writing_score','reading_score']

            input_features_train_df = train_df.drop(columns=target_col) # get train independent features
            target_feature_train_df = train_df[target_col]              # get train dependent feature
            input_features_test_df  = test_df.drop(columns=target_col)  # get test independent features
            target_feature_test_df  = test_df[target_col]               # get test dependent feature
            logging.info("Applying preprocessing object on training and testing dataframe.")
            
            # Feature scaling
            input_features_train_arr = preprocessing_obj.fit_transform(input_features_train_df)
            input_features_test_arr  = preprocessing_obj.transform(input_features_test_df)
            
            # Stack independent and dependent feature in column-wise
            train_arr = np.c_[input_features_train_arr, np.array(target_feature_train_df)]
            test_arr  = np.c_[input_features_test_arr , np.array(target_feature_test_df)]
            logging.info("Saved preprocessing objects.")

            save_object(file_path=self.data_transformation_config.preprocessor_path, 
                        obj=preprocessing_obj)

            return (train_arr, test_arr, self.data_transformation_config.preprocessor_path)

        except Exception as e:
            raise CustomException(e, sys)