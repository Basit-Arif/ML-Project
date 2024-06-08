import sys
from src.utils import Save_object,evaluate_model
import os 
from sklearn.metrics import r2_score
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import AdaBoostRegressor,RandomForestRegressor,GradientBoostingRegressor
from sklearn.neighbors import KNeighborsRegressor
from src.exception import CustomException
from src.logger import logging
from sklearn.linear_model import LinearRegression
from dataclasses import dataclass
from xgboost import XGBRegressor


@dataclass
class ModelTrainerConfig:
    model_trainer_file_path:str=os.path.join("artifacts","model.pkl")

class ModelTrainer:
    def __init__(self):
        self.model_file_path=ModelTrainerConfig()

    def initiate_data_model(self,train_arr,test_arr):
        try:
            X_train,y_train,X_test,y_test=(
                train_arr[:,:-1],
                train_arr[:,-1],
                test_arr[:,:-1],
                test_arr[:,-1]
            )
            model_name={
                "LinearRegression1":LinearRegression(),
                "Decision Tree":DecisionTreeRegressor(),
                "AdaBoostRegressor":AdaBoostRegressor(),
                "RandomForestRegressor":RandomForestRegressor(),
                "GradientBoostingRegressor":GradientBoostingRegressor(),
                "KNeighborsRegressor":KNeighborsRegressor(),
                "XGBRegressor":XGBRegressor(),
            }
            params={
                "Decision Tree":{
                'criterion':['squared_error', 'friedman_mse', 'absolute_error', 'poisson']  
                },
                "AdaBoostRegressor":{
                    'learning_rate':[0.3,0.6,0.8,1.2],
                },
                "RandomForestRegressor":{
                    'n_estimators':[10,20,30,40,50],
                },
                "GradientBoostingRegressor":{
                    'subsample':[0.6,0.7,0.75,0.8,0.85,0.9],
                    },
                "LinearRegression1":{
                    "n_jobs":[1,3,4]
                },
                "KNeighborsRegressor":{
                    'n_neighbors':[3,5,7,9,11],
                },
                "XGBRegressor":{
                    'learning_rate':[.1,.01,.05,.001],
                    'n_estimators': [8,16,32,64,128,256]
                },
                }

            model_report:dict=evaluate_model(X_train,y_train,X_test,y_test,models=model_name,param=params)
            print(type(model_report))
            print(model_report)
            best_model_score=max(sorted(model_report.values()))
            best_model_name=list(model_report.keys())[
                list(model_report.values()).index(best_model_score)
            ]
            best_model=model_name[best_model_name]
            print(best_model)
            if best_model_score<0.6:
                raise CustomException("Model score is less than 0.6")
            logging.info("best model found")
            Save_object(
                file_path=self.model_file_path.model_trainer_file_path,
                obj=best_model
            )

            predicted=best_model.predict(X_test)

            r2_square = r2_score(y_test, predicted)
            return r2_square
            



            
        except Exception as e:
            raise CustomException(e,sys)

        except CustomException as Es:
            CustomException(Es,sys)

