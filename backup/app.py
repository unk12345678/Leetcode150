from flask import Flask, jsonify, render_template
import requests

app = Flask(__name__)

BASE_URL = "https://api.github.com/repos/unk12345678/Leetcode150/contents/python"
# "https://api.github.com/repos/neetcode-gh/leetcode/contents/python"
# https://github.com/neetcode-gh/leetcode/tree/main/python

def get_error_response(message, code=400):
    return jsonify({"error": message}), code

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_filenames')
def get_filenames():
    response = requests.get(BASE_URL)
    if response.status_code == 200:
        files = response.json()
        filenames = [file['name'] for file in files if file['type'] == 'file' and file['name'].endswith('.py')]
        return jsonify(filenames)
    return get_error_response("Failed to fetch filenames from GitHub", response.status_code)

@app.route('/get_file_content/<filename>')
def get_file_content(filename):
    response = requests.get(f"{BASE_URL}/{filename}")
    if response.status_code == 200:
        file_content = response.json().get('content', '')
        return jsonify({"content": file_content})
    return get_error_response("Failed to fetch file content from GitHub", response.status_code)

if __name__ == "__main__":
    app.run(debug=True)
