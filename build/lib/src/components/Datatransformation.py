import pandas as pd
import sys
import os 
import numpy as np
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from dataclasses import dataclass
from sklearn.preprocessing import OneHotEncoder,StandardScaler
from src.exception import CustomException
from src.logger import logging
from src.utils import Save_object
# from src.components.Dataingestion import DataIngestion



@dataclass
class DataTransformationConfig:
    """Data Transformation Config Class"""
    preprocessing_file_path:str=os.path.join("artifacts","preprocessing.pkl")

class DataTransformation:
    """Data Transformation Class"""
    def __init__(self):
        self.data_transformation_config=DataTransformationConfig()
    
    def get_data_transformation_object(self):
        """Get Data Transformation Object"""
        try:
            numerical_data=['reading_score', 'writing_score']
            categorical=['gender',
                'race_ethnicity',
                'parental_level_of_education',
                'lunch',
                'test_preparation_course']
            ## first we need to impute the missing values with the mean value 

            num_pipeline=Pipeline(
                steps=[
                    ('imputer',SimpleImputer(strategy='mean')),
                    ('scaler',StandardScaler())
                ]
            )
            logging.info("Numerical Standard Scaler is Completed")
            cat_pipeline=Pipeline(
                steps=[
                    ('imputer',SimpleImputer(strategy='most_frequent')),
                    ('onehot',OneHotEncoder())
                    ]
                
            )
            logging.info("Categorical encoded is Completed")
            preprocessor=ColumnTransformer(
                transformers=[
                    ('num',num_pipeline,numerical_data),
                    ('cat',cat_pipeline,categorical)
                    ]
            )
            return preprocessor

            
        except Exception as es:
            CustomException(es,sys)

    def initial_data_transforatmion(self,train_path,test_path):
        """Initial Data Transformation"""
        try:
            train_df=pd.read_csv(train_path)
            test_df=pd.read_csv(test_path)
            logging.info("Data is loaded")
            preprocessing=self.get_data_transformation_object()
            target_column="math_score"
            numerical_columns=["writing_score","reading_score"]
            input_feature_train_df=train_df.drop(columns=[target_column],axis=1)
            target_feature_train_df=train_df[target_column]

            input_feature_test_df=test_df.drop(columns=[target_column],axis=1)
            target_feature_test_df=test_df[target_column]
            logging.info("Now Applying Preprocessing")


            train_preprocess=preprocessing.fit_transform(input_feature_train_df)
            test_preprocess=preprocessing.transform(input_feature_test_df)

            train_arr=np.c_[train_preprocess,np.array(target_feature_train_df)]
            test_arr=np.c_[test_preprocess,np.array(target_feature_test_df)]
            logging.info("save_preprocessing_object")
            Save_object(self.data_transformation_config.preprocessing_file_path,preprocessing)

            return (
                train_arr,
                test_arr,
                self.data_transformation_config.preprocessing_file_path,
            )
            
        except Exception as es :
            print(CustomException(es,sys))
            logging.info("Data Transformation is Failed")

