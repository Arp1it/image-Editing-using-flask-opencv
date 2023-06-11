from flask import Flask, render_template, redirect, request, flash
import cv2
import os
from werkzeug.utils import secure_filename
import random
from PIL import Image
import pillow_avif


UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'webp', 'png', 'jpg', 'jpeg', 'gif', "avif"}

app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

app.config['SECRET_KEY']='Define_The_Key'

def processImage(filename, operation):
    print(f"The operation is {operation} and filename is {filename}")
    img = cv2.imread(f"uploads/{filename}")
    match operation:
        case "cgray":
            f = f"{filename.split('.')[1]}"
            # print(f)
            if f == "avif":
                newfilenamee = f"{filename.split('.')[0]}"
                ran = random.randint(100, 1000)
                Grayimg = Image.open(f"uploads/{newfilenamee}.avif")
                Grayimg.save(f"uploads/{ran}.jpg")
                iom = cv2.imread(f"uploads/{ran}.jpg")
                imgprocessd = cv2.cvtColor(iom, cv2.COLOR_BGR2GRAY)
                newfilename = f"static/{ran}.jpg"
                cv2.imwrite(newfilename, imgprocessd)
                Grayimg = Image.open(f"static/{ran}.jpg")
                Grayimg.save(f"static/{newfilenamee}.avif")
                os. remove(f"uploads/{ran}.jpg")
                os. remove(f"static/{ran}.jpg")
                newfilename = f"static/{newfilenamee}.avif"
                return newfilename

            else:
                imgprocessd = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                newfilename = f"static/{filename}"
                cv2.imwrite(newfilename, imgprocessd)
                return newfilename

        case "cpng":
            f = f"{filename.split('.')[1]}"
            # print(f)
            if f == "avif":
                newfilename = f"{filename.split('.')[0]}"
                PNGimg = Image.open(f"uploads/{newfilename}.avif")
                PNGimg.save(f"static/{newfilename}.png")
                newfilename = f"static/{newfilename}.png"
                return newfilename

            else:
                newfilename = f"static/{filename.split('.')[0]}.png"
                cv2.imwrite(newfilename, img)
                return newfilename

        case "cjpg":
            f = f"{filename.split('.')[1]}"
            # print(f)
            if f == "avif":
                newfilename = f"{filename.split('.')[0]}"
                JPGimg = Image.open(f"uploads/{newfilename}.avif")
                JPGimg.save(f"static/{newfilename}.jpg")
                newfilename = f"static/{newfilename}.jpg"
                return newfilename

            else:
                newfilename = f"static/{filename.split('.')[0]}.jpg"
                cv2.imwrite(newfilename, img)
                return newfilename

        case "cwebp":
            f = f"{filename.split('.')[1]}"
            if f == "avif":
                newfilename = f"{filename.split('.')[0]}"
                WEBPimg = Image.open(f"uploads/{newfilename}.avif")
                WEBPimg.save(f"static/{newfilename}.webp")
                newfilename = f"static/{newfilename}.webp"
                return newfilename

            else:
                newfilename = f"static/{filename.split('.')[0]}.webp"
                cv2.imwrite(newfilename, img)
                return newfilename

        case "cavif":
            f = f"{filename.split('.')[1]}"
            filenamee = f"{filename.split('.')[0]}"
            Avifimg = Image.open(f"uploads/{filenamee}.{f}")
            Avifimg.save(f"static/{filenamee}.avif")
            newfilename = f"static/{filenamee}.avif"
            return newfilename

def allowed_file(filename):
    # print(filename.split(".")[1])
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/edit", methods=["GET", "POST"])
def edit():
    if request.method == "POST":
        operation = request.form.get("operation")
        # check if the post request has the file
        if 'file' not in request.files:
            flash('No file')
            return "error"


        file = request.files['file']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.


        if file.filename == '':
            flash('No selected file')
            return "error"
            

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

            new = processImage(filename, operation)

            flash(f"Your image uploaded <a href='/{new}' target='_blank'>here</a>")
            return render_template("index.html")

    return redirect("/")

@app.route("/about")
def about():
    return "about page. This is page is not working currently."

@app.route("/how")
def Howtouse():
    return "How to use. This is page is not working currently."

@app.route("/contact")
def contact():
    return "Contact us. This is page is not working currently."

if __name__ == "__main__":
    app.run(debug=True)
