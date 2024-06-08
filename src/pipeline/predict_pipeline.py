import sys
from src.exception import CustomException
from src.logger import logging
import numpy as np
import pandas as pd
import os
from src.utils import load_object
class Predictpipline():
    def __init__(self):
        pass
    def predict(self,features):
        try:
            model_path=os.path.join("artifacts",'model.pkl')
            preprosser_path=os.path.join("artifacts",'preprocessing.pkl')
            preprocessor=load_object(preprosser_path)
            model=load_object(model_path)
            data_scaled=preprocessor.transform(features)
            predicted_data=model.predict(data_scaled)
            print(predicted_data)
            return predicted_data


        except Exception as es:
            logging.error(es)
            CustomException(es,sys)



class CustomData:
    def __init__(self,gender,race_ethnicity,parental_level_of_education,lunch,test_preparation_course,reading_score,writing_score):
        self.gender=gender
        self.race_ethnicity=race_ethnicity
        self.parental_level_of_education=parental_level_of_education
        self.lunch=lunch
        self.test_preparation_course=test_preparation_course
        self.reading_score=reading_score
        self.writing_score=writing_score

    def convert_data_to_dataframe(self):
        try:
            custom_data_input_dict = {
                "gender": [self.gender],
                "race_ethnicity": [self.race_ethnicity],
                "parental_level_of_education": [self.parental_level_of_education],
                "lunch": [self.lunch],
                "test_preparation_course": [self.test_preparation_course],
                "reading_score": [self.reading_score],
                "writing_score": [self.writing_score],
            }
            logging.info("converting raw data into DataFrame")
            
            return pd.DataFrame(custom_data_input_dict)
        except Exception as es:
            return CustomException(es,sys)