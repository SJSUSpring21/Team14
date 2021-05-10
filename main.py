from flask import Flask, request, render_template, flash, redirect, url_for , session
from flask import send_from_directory
import os
from werkzeug import secure_filename
import subprocess
# Flask constructor
app = Flask(__name__) 
app.secret_key = "super secret key"  
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
  
# A decorator used to tell the application
# which URL is associated function
@app.route('/', methods =["GET", "POST"])
def addName():
    if request.method == "POST":
       # getting input with name = fname in HTML form
       first_name = request.form.get("fname")
       # getting input with name = lname in HTML form 
       last_name = request.form.get("lname") 
       #give path to location where you want to create folder
       
       path = "C:\\Users\\kcnou\\Desktop\\SJSU\\CMPE272\\GroupProject\\privacy-preserving-for-face-recognition-master\\faceImages\\"+first_name+last_name
       os.mkdir(path)
       app.config['UPLOAD_FOLDER'] = path
       return redirect(url_for("uploadpicture") )
    return render_template("index.html")
    
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
 
 
@app.route("/uploadpicture", methods =["GET", "POST"]) 
def uploadpicture():
    if request.method == 'POST':
        # check if the post request has the file part
        """if 'file' not in request.files:
            flash('No file part')
            return redirect(url_for("uploadpicture"))
            """
        #file = request.files['file']
        files = request.files.getlist('file')
        # if user does not select file, browser also
        # submit an empty part without filename
        for file in files:
            if file.filename == '':
                flash('No selected file')
                return redirect(url_for("uploadpicture"))
            if file and allowed_file(file.filename):
                filename = file.filename
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return redirect(url_for("addName"))
    return render_template("uploadpicture.html")

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],filename)   
    
@app.route('/run_embedding')
def run_embedding():
   result = subprocess.check_output("python generateFaceEmbedded.py", shell=True)  
   return render_template('index.html', **locals(), embedding = "Uploaded Images are Embedded")
   
@app.route('/train_model')
def train_model():
   subprocess.getoutput("python encryptedClassification.py")
   return render_template('index.html', **locals(), training = "Model is trained with the uploaded images")
   
@app.route('/recognize_face')
def recognize_face():
   subprocess.getoutput("python faceRecognizer.py")
   return render_template('index.html', **locals())
 
if __name__=='__main__':
   #app.run()
   app.run(debug = True)