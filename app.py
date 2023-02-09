from flask import Flask, request
from flask_restful import Api, Resource, reqparse
import os

import basic_OCR

app = Flask(__name__)
api = Api(app)

'''
Creating API for POST method
'''
@app.route('/invoice', methods=['POST'])
def invoice():
    headers = request.headers
    for key, file in request.files.items():
        if file.filename != '':
            dest = os.path.join('./api_uploaded_files', file.filename)
            file.save(dest)
            data = basic_OCR.result_data(dest)
            return data


if __name__ == '__main__':
    app.run(host="0.0.0.0",port=5000)   
    #debug=True       


