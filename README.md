# Unzip My Docs: The DOCX Image Liberation Station

A playful, modern web app to extract and download all images from your .docx files. Upload your document, preview your images, and download them all at once—liberate your visuals!

---

## 🚀 Features

- Upload .docx files and extract all embedded images
- Preview images instantly in your browser
- Download all images as a single zip file
- Stylish, responsive UI powered by Tailwind CSS

---

## 🛠️ Getting Started

### 1. Clone the repository

```bash
git clone git@github.com:drikusroor/docx_image_extractor.git
cd docx_image_extractor
```

### 2. Set up a Python virtual environment (recommended)

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip3 install -r requirements.txt
```

### 4. Run the app

```bash
python3 app.py
```

Visit [http://127.0.0.1:5000](http://127.0.0.1:5000) in your browser.

---

## 🐳 Docker (Optional)

Build and run the app in a container for maximum portability:

```bash
docker build -t docx-image-extractor .
docker run -p 5000:5000 docx-image-extractor
```

---

## 📦 Project Structure

- `app.py` — Flask backend
- `templates/index.html` — Frontend UI
- `uploads/` — Uploaded .docx files
- `extracted/` — Extracted images and zip files

---

## 🧹 Cleaning Up

To remove all uploaded and extracted files:

```bash
rm -rf uploads/* extracted/*
```

---

## 📝 License

MIT or your preferred license.

---

## 💡 Tips

- Always use a virtual environment or Docker for isolation and reproducibility.
- For production, consider using a production-ready WSGI server (e.g., gunicorn) and serving static files via a CDN or reverse proxy.

---

Enjoy liberating your images!
