
from flask import Flask, request, render_template, redirect
import os

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/upload", methods=["POST"])
def upload():
    file = request.files["file"]

    if file.filename:
        file.save(os.path.join(UPLOAD_FOLDER, file.filename))
        return "File uploaded successfully!"

    return "Please select a file."


@app.route("/files")
def files():
    filenames = os.listdir(UPLOAD_FOLDER)
    return render_template("files.html", files=filenames)


@app.route("/delete/<filename>")
def delete(filename):
    path = os.path.join(UPLOAD_FOLDER, filename)

    if os.path.isfile(path):
        os.remove(path)
        return "File deleted successfully!"

    return "File not found."


if __name__ == "__main__":
    app.run(debug=True)
