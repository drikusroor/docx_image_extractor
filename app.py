from flask import Flask, render_template, request, send_from_directory, jsonify
import os
import zipfile
from werkzeug.utils import secure_filename
from uuid import uuid4

app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
EXTRACT_FOLDER = "extracted"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(EXTRACT_FOLDER, exist_ok=True)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/upload", methods=["POST"])
def upload():
    if "file" not in request.files:
        return jsonify({"error": "No file part"}), 400

    file = request.files["file"]
    if file.filename == "":
        return jsonify({"error": "No selected file"}), 400

    if file and file.filename.endswith(".docx"):
        uid = str(uuid4())
        upload_path = os.path.join(UPLOAD_FOLDER, uid + ".docx")
        extract_path = os.path.join(EXTRACT_FOLDER, uid)
        os.makedirs(extract_path, exist_ok=True)
        file.save(upload_path)

        with zipfile.ZipFile(upload_path, "r") as docx_zip:
            for file_info in docx_zip.infolist():
                if file_info.filename.startswith("word/media/"):
                    filename = os.path.basename(file_info.filename)
                    with docx_zip.open(file_info.filename) as source, open(os.path.join(extract_path, filename), "wb") as target:
                        target.write(source.read())

        images = os.listdir(extract_path)
        return jsonify({
            "id": uid,
            "images": images
        })
    return jsonify({"error": "Invalid file type"}), 400

@app.route("/images/<uid>/<filename>")
def get_image(uid, filename):
    return send_from_directory(os.path.join(EXTRACT_FOLDER, uid), filename)

if __name__ == "__main__":
    app.run(debug=True)
