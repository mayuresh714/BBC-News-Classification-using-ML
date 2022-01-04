from flask import Flask, request, jsonify
from model import algo_spacy
import pickle

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/prime/<int:n>')
def is_prime(n):
    if n == 1:
        print("not a prime no.")
        return "False"
    for i in range(2, n):
        if n % i == 0:
            print("not a prime no.")
            return "False"
    print("yes it's prime no.")
    return "True"

@app.route('/predict/<string:sr>')
def predict(sr):
    # load pickle files
    with open('model.pickle', 'rb') as handle:
        model = pickle.load(handle)
    with open('trained_model.pickle', 'rb') as handle:
        trained_model = pickle.load(handle)
         
    # create object and predict the sentiment
    pred_model = algo_spacy( model = model , trained_model = trained_model )
    pred_val = pred_model.predict_tag(sr).upper()

    # return the prediction
    dic = {'results':{
        'sentiment':pred_val,
        'text':'The article is related to {}'.format( pred_val),
        'status':'success'
    }}

    return dic


if __name__ == '__main__':
    app.run(debug=True)