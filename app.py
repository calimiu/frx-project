from flask import Flask, render_template, request, jsonify, redirect, url_for
import json
import os
from jsonschema import validate, ValidationError
from pathlib import Path

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

SCHEMA_FILE = "frx_schema.json"
FRX_DIR = "frx_files"

if not os.path.exists(FRX_DIR):
    os.makedirs(FRX_DIR)

def load_schema():
    with open(SCHEMA_FILE, 'r', encoding='utf-8') as f:
        return json.load(f)

def get_all_frx_files():
    files = []
    for file in Path(FRX_DIR).glob('*.frx'):
        files.append(file.name)
    for file in Path(FRX_DIR).glob('*.json'):
        files.append(file.name)
    return sorted(files)

@app.route('/')
def index():
    files = get_all_frx_files()
    return render_template('index.html', files=files)

@app.route('/api/files')
def list_files():
    files = get_all_frx_files()
    return jsonify(files)

@app.route('/api/file/<filename>')
def get_file(filename):
    filepath = os.path.join(FRX_DIR, filename)
    if not os.path.exists(filepath):
        return jsonify({'error': 'File not found'}), 404
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = json.load(f)
    return jsonify(content)

@app.route('/api/file/<filename>', methods=['POST'])
def save_file(filename):
    try:
        data = request.json
        schema = load_schema()
        
        validate(instance=data, schema=schema)
        
        filepath = os.path.join(FRX_DIR, filename)
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        
        return jsonify({'success': True, 'message': 'File saved successfully'})
    except ValidationError as e:
        return jsonify({'success': False, 'error': f'Validation error: {e.message}'}), 400
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

@app.route('/api/file/<filename>', methods=['DELETE'])
def delete_file(filename):
    filepath = os.path.join(FRX_DIR, filename)
    if not os.path.exists(filepath):
        return jsonify({'error': 'File not found'}), 404
    
    os.remove(filepath)
    return jsonify({'success': True, 'message': 'File deleted successfully'})

@app.route('/api/validate', methods=['POST'])
def validate_data():
    try:
        data = request.json
        schema = load_schema()
        validate(instance=data, schema=schema)
        return jsonify({'valid': True, 'message': 'Valid FRX file'})
    except ValidationError as e:
        return jsonify({'valid': False, 'error': e.message}), 400

@app.route('/editor')
@app.route('/editor/<filename>')
def editor(filename=None):
    return render_template('editor.html', filename=filename)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
