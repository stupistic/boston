from flask import Flask
from flask import render_template
from flask import request
import os


@app.route("/",methods=["GET","POST"])
def upload_predict():
    if request.method == "POST":
        image_file = request.files["image"]
        if image_file:
            image_location = os.path.join(
                UPLOAD_FOLDER,
                image_file.filename
            )

            image_file.save(image_location)
            return render_template("index.html",prediction=1)
    return render_template("index.html",prediction=0)

if __name__=="__main__":
    app.run(port=12000,debug=True)