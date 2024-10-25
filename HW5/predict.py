import pickle

with open('model1.bin', 'rb') as f_in:
    model = pickle.load(f_in)

with open('dv.bin', 'rb') as f_in1:
    dv = pickle.load(f_in1)

customer = {"job": "management", "duration": 400, "poutcome": "success"}

X = dv.transform([customer])

y_pred = model.predict_proba(X)[0, 1]

print(f' PROBABILITY OF CUSTOMER {customer} SUBSCRIBING IS : {y_pred}')