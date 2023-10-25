from flask import Flask, jsonify, render_template
import requests

app = Flask(__name__)

BASE_URL = "https://api.github.com/repos/unk12345678/Leetcode150/tree/main/python"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_filenames')
def get_filenames():
    response = requests.get(BASE_URL)
    if response.status_code == 200:
        files = response.json()
        filenames = [file['name'] for file in files if file['type'] == 'file']
        return jsonify(filenames)
    return jsonify([])

@app.route('/get_file_content/<filename>')
def get_file_content(filename):
    response = requests.get(f"{BASE_URL}/{filename}")
    if response.status_code == 200:
        file_content = response.json().get('content', '')
        return jsonify({"content": file_content})
    return jsonify({"content": "Error fetching content"})

if __name__ == "__main__":
    app.run(debug=True)
