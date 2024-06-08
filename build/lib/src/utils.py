import os 
import sys
import numpy as np
import pandas as pd
from sklearn.metrics import r2_score
import dill
from src.exception import CustomException
from sklearn.ensemble import AdaBoostRegressor,RandomForestRegressor,GradientBoostingRegressor
from sklearn.model_selection import GridSearchCV
import pickle
def Save_object(file_path,obj):
    try:
        dirname=os.path.dirname(file_path)
        os.makedirs(dirname,exist_ok=True)
        with open(file_path,'wb') as f:
            dill.dump(obj,f)
    except:
        print('Error in saving object')


def evaluate_model(X_train,y_train,X_test,y_test,models,param):
    try:
        model_score={}
        params=param
        for i in range(len(list(models))):
            model=list(models.values())[i]

            para=param[list(models.keys())[i]]
            para
            gs=GridSearchCV(model,para,cv=3)
            gs.fit(X_train,y_train)
            model.set_params(**gs.best_params_)
            model.fit(X_train,y_train)
            y_train_predict=model.predict(X_train)
            y_test_predict=model.predict(X_test)    
            model_score[list(models.keys())[i]]=r2_score(y_test,y_test_predict)
        return model_score   
    except Exception as es:
        CustomException(es,sys)
    
# evaluate_model([[1,2],[4,5]],[1,0],[[2,3],[1,5]],[1,1],models=model)


def load_object(file_path):
    try:
        with open(file_path,'rb') as f:
            return pickle.load(f)
    except Exception as es:
        print(es,sys)
    





