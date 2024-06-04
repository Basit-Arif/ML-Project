import sys
import os
from src.logger import logging

from src.exception import CustomException
from src.components.Modeling import ModelTrainer,ModelTrainerConfig


# from src.exception import CustomException
from sklearn.model_selection import train_test_split
from dataclasses import dataclass
import pandas as pd
from .Datatransformation import DataTransformation


@dataclass
class DataIngestionConfig:
    train_data:str=os.path.join("artifacts","train.csv")
    test_data:str=os.path.join("artifacts","test.csv")
    raw_data_dir:str=os.path.join("artifacts","data.csv")

class DataIngestion:
    def __init__(self):
        self.config=DataIngestionConfig()
    def Dataingestion(self):
        logging.info("Entered the data ingestion method or component")
        try:
            df=pd.read_csv("/Users/basitarif/Documents/ML-Project/src/study_data.csv")
            logging.info("DataIngested")
            os.makedirs(os.path.dirname(self.config.raw_data_dir),exist_ok=True)
            df.to_csv(self.config.raw_data_dir,index=False)

            train_data,test_data=train_test_split(df,test_size=0.2,random_state=42)
            # logging.info("splitting_data into train_test")
            train_data.to_csv(self.config.train_data,index=False)
            test_data.to_csv(self.config.test_data,index=False)
            logging.info("DataIngestion completed")
            return (
                self.config.train_data
                ,self.config.test_data
            )

        except Exception as e:
            print("hello")
            raise CustomException(e,sys)




if __name__=="__main__":
    logging.info("Starting the Program")
    data=DataIngestion()
    train,test=data.Dataingestion()
    logging.info("DataIngestion completed")
    transform=DataTransformation()
    train_arr,test_arr,_=transform.initial_data_transforatmion(train,test)
    
    logging.info("Transformation Program completed")
    model_trainer=ModelTrainer()
    model_trainer.initiate_data_model(train_arr,test_arr)
    logging.info("Model Training completed")
    # print("this is ")