# Flask Image Conversion App

This is a Flask web application for uploading images and performing basic image format conversions and grayscale processing. It supports common image formats including JPG, PNG, WEBP, AVIF, ICO, and GIF.

---

## ✅ Features

- Upload an image and apply one of the following operations:
  - Convert to **Grayscale**
  - Convert to **PNG**
  - Convert to **JPG**
  - Convert to **WEBP**
  - Convert to **AVIF**
  - Convert to **ICO**
- AVIF format support using `pillow-avif-plugin`
- Uploaded files are stored in the `uploads/` folder
- Processed images are saved in the `static/` folder
- Displays a flash message with a link to the processed image

---

## 🧰 Tech Stack

- **Python 3**
- **Flask**
- **OpenCV (cv2)**
- **Pillow (PIL)**
- **pillow-avif-plugin**

---

## 📁 Project Structure


project/
├── app.py                 # Main Flask application
├── templates/
│   └── index.html         # Web form for uploading and selecting operation
├── static/                # Stores processed images
├── uploads/               # Temporarily stores uploaded files
└── README.md              # Project documentation


---

## 📦 Installation

1. Clone the project:

````
```bash
git clone https://github.com/Arp1it/image-Editing-using-flask-opencv
cd project
````

2. Install dependencies:

```bash
pip install Flask opencv-python pillow pillow-avif-plugin
```

---

## ▶️ Running the App

```bash
python main.py
```

Then open your browser and go to:
**http://127.0.0.1:5000**

---

## 📝 Usage

1. On the home page, upload an image file.
2. Select an operation:

   * `cgray`: Convert to grayscale
   * `cpng`: Convert to PNG
   * `cjpg`: Convert to JPG
   * `cwebp`: Convert to WEBP
   * `cavif`: Convert to AVIF
   * `cico`: Convert to ICO
3. Click "Submit" and wait for the response.
4. A download/view link will be shown after processing.

---

## ℹ️ Other Routes

* `/about` → Returns a placeholder text
* `/how` → Returns a placeholder text
* `/contact` → Returns a placeholder text

These routes are currently not functional.

---

## 🔒 Configuration

* The Flask app uses `app.config['SECRET_KEY']`. Replace `'Define_The_Key'` with a secure secret key.

---

## ❗ Notes

* AVIF support requires `pillow-avif-plugin` to be installed.
* Temporary files are saved in `uploads/`; processed files go to `static/`.
* There is no cleanup mechanism for old images. (Future improvement)
* Error handling is minimal and mostly logs to console. (Future improvement)

---
