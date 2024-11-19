import pickle

from flask import Flask, request, jsonify

with open('midterm.bin','rb') as f_in:
    dv, model = pickle.load(f_in)

app = Flask('midterm')

@app.route('/predict', methods=['POST'])
def predict():
    customer = request.get_json()
    print(f' REQ CUSTOMER : {customer}')
    X = dv.transform(customer)
    y_pred = model.predict(X)
    
    result = {
        "Customer Satisfaction": f'{y_pred[0]}'
    }

    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=9696)
