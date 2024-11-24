from flask import Flask, jsonify, send_from_directory
from flask_cors import CORS
import os

app = Flask(__name__)
BASE_DIR = "images"  # Base directory for images

CORS(app)  # Allow all origin

@app.route('/')
def serve_index():
    """Serve the index.html file."""
    return send_from_directory('.', 'index.html')

@app.route('/images/<hour>/')
def list_images(hour):
    """List all images in the specified hour's folder."""
    directory = os.path.join(BASE_DIR, hour)
    if os.path.exists(directory):
        images = [file for file in os.listdir(directory) if file.lower().endswith(('.jpg', '.jpeg', '.png', '.gif'))]
        return jsonify(images)
    else:
        return jsonify([])  # Return an empty list if directory doesn't exist

@app.route('/images/<hour>/<filename>')
def serve_image(hour, filename):
    """Serve an image file from the specified hour's folder."""
    directory = os.path.join(BASE_DIR, hour)
    if os.path.exists(directory) and filename in os.listdir(directory):
        return send_from_directory(directory, filename)
    else:
        return "File not found", 404

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)






