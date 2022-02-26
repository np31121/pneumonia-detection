from app import app
import os
import tempfile
from flask import render_template, flash, send_from_directory, request
from app.forms import uploadForm
from werkzeug.utils import secure_filename
from .headers import *

@app.route("/")
def hello_main():
    return render_template('index.html', ids=ids)

@app.route("/url", methods=["GET", "POST"])
def hello_url():
    form=uploadForm()
    output=''
    if request.method=="POST":
        try:
            result1 = predictor.classify_image_url(project_id, publish_iteration_name, form.imgurl.data)
        except:
            flash("Bad Request! Please enter a proper image URL.")
        else:
            output=result1.predictions[0].tag_name
            if output=='Pneumonia':
                output+=' Detected'
            output+='!'
    return render_template('imageurl.html', form=form, output=output)

@app.route("/upload", methods=["GET", "POST"])
def hello_upload():
    form=uploadForm()
    output=''
    filename=''
    if request.method=="POST":
        try:
            filename=secure_filename(form.imgfile.data.filename)
            f=os.path.join(tempfile.gettempdir(), filename)
            form.imgfile.data.save(f)
            with open((f), "rb") as image_contents:
                result1 = predictor.classify_image(project_id, publish_iteration_name, image_contents.read())
        except:
            flash("Bad Request! Please input an image.")
        else:
            output=result1.predictions[0].tag_name
            if output=='Pneumonia':
                output+=' Detected'
            output+='!'
    return render_template('uploadimage.html', form=form, output=output, filename=filename)

@app.route('/upload/<filename>')
def send_uploaded_file(filename=''):
    return send_from_directory(tempfile.gettempdir(), filename)

@app.route('/<id>')
def getTheId(id):
    try:
        result1 = predictor.classify_image_url(project_id, publish_iteration_name, ids[int(id)-1])
    except:
        flash("Bad Request! An error occurred.")
        output=''
    else:
        output=result1.predictions[0].tag_name
        if output=='Pneumonia':
            output+=' Detected'
        output+='!'
    return render_template('index.html', ids=ids, output=output)