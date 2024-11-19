
import pickle
import numpy as np
import pandas as pd

from sklearn.model_selection import train_test_split, KFold

from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.feature_extraction import DictVectorizer

df = pd.read_csv('satisfaction.csv')

#Column name standarization
df.columns = df.columns.str.lower().str.replace(' ','_')
df = df.dropna()

#Split data into train, val and test sets
df_full_train, df_val = train_test_split(df, test_size=0.2, random_state=42)
df_train, df_test = train_test_split(df_full_train, test_size=0.25, random_state=42)

df_train = df_train.reset_index(drop=True)
df_test = df_test.reset_index(drop=True)
df_val = df_val.reset_index(drop=True)

y_train = df_train.satisfaction_v2
y_test = df_test.satisfaction_v2
y_val = df_val.satisfaction_v2

#Remove target variable from train, test and val data sets
del df_train['satisfaction_v2']
del df_test['satisfaction_v2']
del df_val['satisfaction_v2']

def train(X, y) :
    dicts = X.to_dict(orient='records')

    dv = DictVectorizer(sparse=False)
    X_train = dv.fit_transform(dicts)

    model = DecisionTreeClassifier()
    model.fit(X_train, y)
    return dv, model

def predict(df, dv, model) :
    val_dicts = df.to_dict(orient='records')
    X_val = dv.transform(val_dicts)

    y_pred = model.predict(X_val)
    return y_pred


dv, model = train(df_train, y_train)
y_pred = predict(df_val, dv, model)

score = np.round(accuracy_score(y_pred, y_val), 3)

print(f'SCORE : {score}')

y_pred_test = predict(df_test, dv, model)

test_score = np.round(accuracy_score(y_test, y_pred_test))
print(f'SCORE : {test_score}')

# Save model & dv to a file using pickle
output_file = 'midterm.bin'

with open(output_file, 'wb') as f_out:
    pickle.dump((dv, model), f_out)

print(f'The model is saved to file {output_file}')