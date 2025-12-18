from flask import Flask, request, send_file

app = Flask(__name__)

@app.route('/download')
def download_file():
    # SOURCE: user provides a filename
    filename = request.args.get('file')
    
    # SINK: The path is not validated
    # This should trigger: "Uncontrolled data used in path expression"
    return send_file("/var/www/uploads/" + filename)
