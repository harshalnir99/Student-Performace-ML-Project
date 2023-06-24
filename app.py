from flask import Flask, render_template, request, jsonify
from src.pipelines.predication_pipeline import PredictionPipeline, CustomClass

app = Flask(__name__)

@app.route("/",methods = ["GET", "POST"])
def prediction_data():
    if request.method == "GET":
        return render_template("home.html")
    
    else:
        data=CustomClass(
            gender=str(request.form.get('gender')),
            race_ethnicity=str(request.form.get('race_ethnicity')),
            parental_level_of_education=str(request.form.get('parental_level_of_education')),
            lunch=str(request.form.get('lunch')),
            test_preparation_course=str(request.form.get('test_preparation_course')),
            reading_score=float(request.form.get('writing_score')),
            writing_score=float(request.form.get('reading_score')))
        

    final_data = data.get_data_as_data_frame()
    pipeline_predication =PredictionPipeline()

    pred = pipeline_predication.predict(final_data)

    return render_template("results.html",final_result = "Your Exam Performance is :{}".format(pred))


if __name__ == "__main__":
     app.run(host = "0.0.0.0", debug = True)