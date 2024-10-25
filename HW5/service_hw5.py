import pickle

import numpy as np
from flask import Flask
from flask import request
from flask import jsonify


app = Flask('predserv')

@app.route('/predict', methods=['POST'])
def predict():

    with open('model2.bin', 'rb') as f_in:
        model = pickle.load(f_in)

    with open('dv.bin', 'rb') as f_in1:
        dv = pickle.load(f_in1)
    
    customer = request.get_json()
    print(f'Serving prediction request for customer {customer}')
    
    X = dv.transform([customer])

    y_pred = model.predict_proba(X)[0,1]

    result = {"Subscription Probability": float(np.round(y_pred,3)) }
    
    return jsonify(result)
 
## waitress-serve --listen=0.0.0.0:9696 bankpredservice:app
# here bankpredservice is the name of this python file

# Below if block is required if we want to run flask inbuilt servernot,  required if we use waitress
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port = 9696) 
