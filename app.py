import pickle
from flask import Flask,request,render_template,redirect
import numpy as np
import pandas as pd
from src.pipeline.predict_pipeline import CustomData,Predictpipline

app=Flask(__name__)

@app.route("/")
def main_page():
    return render_template('index.html')

@app.route("/home",methods=["GET","POST"])
def predict_page():
    if request.method=="GET":
        return render_template("home.html")
    else:
        try:
            print(request.form.get("parental_level_of_education"))
            data=CustomData(
            gender=request.form.get("gender"),
            race_ethnicity=request.form.get("ethnicity"),
            parental_level_of_education=request.form.get("parental_level_of_education"),
            lunch=request.form.get("lunch"),
            test_preparation_course=request.form.get("test_preparation_course"),
            reading_score=int(request.form.get("reading_score")),
            writing_score=int(request.form.get("writing_score")),
            )

            pred_df=data.convert_data_to_dataframe()
            predicted_data=Predictpipline().predict(pred_df)
            return render_template("home.html",results=predicted_data)
        except Exception as es:
           
            return render_template("home.html",results=es)






if __name__=="__main__":
    app.run(host="0.0.0.0",port=5005,debug=True)