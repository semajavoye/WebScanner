import flask
from flask import send_from_directory, request, jsonify
import subprocess

app = flask.Flask(__name__)

@app.route('/')
def index():
    return send_from_directory('static', 'index.html')

@app.route('/style.css')
def css():
    return send_from_directory('static', 'style.css')

@app.route('/button-clicked', methods=['POST'])
def button_clicked():
    data = request.json
    button_name = data['button']
    
    if button_name == 'directoryscan':
        domain = request.form['domain']
        output = directory_scan(domain)
        return jsonify(output)
    
    return '', 204

def directory_scan(domain):
    # Perform directory scanning here
    # This function should return the output of the directory scanning process
    # For now, let's assume some dummy output
    output = {'status': 'success', 'message': f'Directory scan completed for domain: {domain}'}
    return output

if __name__ == "__main__":
    app.run(debug=True)
