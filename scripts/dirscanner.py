import os
import datetime
import socket
import requests
from flask import Flask, request, jsonify


# connect the route with py and let the dirs get in a callback throughout to html ui
app = Flask(__name__)

MAX_WORKERS = 13
DEF_TIMEOUT = 3
DEFAULT_DIR_LIST_FILE = '../data/directories.dat'
FOUND = []

def _fetch_url(url, headers, ssl_verify=True, write_response=False, timeout=DEF_TIMEOUT):
    global FOUND
    domain = url.split("//")[-1].split("/")[0].split('?')[0].split(':')[0]
    socket.setdefaulttimeout(timeout)
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    try:
        site_request = requests.get(url, headers=headers, verify=ssl_verify)
        FOUND.append([dt_string, url, site_request.status_code, len(site_request.content)])
        if write_response:
            file_name_string = "".join(x for x in url if x.isalnum())
            f = open(os.path.join(domain, file_name_string), 'wb')
            f.write(site_request.content)
            f.close()
    except Exception as e:
        FOUND.append([dt_string, url, "Error: %s" % e, 0])

@app.route('/scan', methods=['POST'])
def scan():
    data = request.json
    domain = data['domain']
    output = main(domain)
    return jsonify(output)

def main(domain):
    # Your existing code for directory scanning functionality goes here
    # You can modify it as necessary to receive domain as a parameter and return the output
    # For demonstration purposes, let's assume some dummy output
    output = {'status': 'success', 'message': 'Directory scan completed for domain: {}'.format(domain)}
    return output

if __name__ == "__main__":
    app.run(debug=True)
