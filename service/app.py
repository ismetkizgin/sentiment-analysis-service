from flask import Flask, request, jsonify
from dotenv import load_dotenv
from middleware.apiKeyVerify import ApiKeyVerify
from flask_cors import CORS
import pickle
import os
load_dotenv()

app = Flask(__name__) 
CORS(app, resources={r"*": {'origins': os.environ.get('CORS') or '*'}})
app.wsgi_app=ApiKeyVerify(app.wsgi_app)

@app.route('/predict',methods=['POST'])
def predict():
    if not 'text' in request.get_json():
        return jsonify(message = 'Text content must be sent in body!'), 417 

    vect = pickle.load(open('../model/vect.pkl','rb'))
    prediction = model.predict(vect.transform([request.get_json()['text']]))
    if prediction[0]:
        return jsonify(predictState = True)
    else:
        return jsonify(predictState = False)

if __name__  == '__main__':
    model = pickle.load(open('../model/model.pkl','rb'))
    app.run(debug=True)