# Model to predict Airline customer satisfaction
- Purpose of this project is to predict the satisfaction level of airline passengers
- Sample daatset is availanle in the file satisfacton.csv. It's taken from Kaggle [text](https://www.kaggle.com/datasets/johndddddd/customer-satisfaction)
- Sample dataset contains various data elements like seat comfort, arrival / departure time convienience, food, flight distance, class of travel etc. 
- Target variable is satisfaction_v2

## Instuctions to use the model
Trained model has been saved to midterm.bin file using Pickle. The Dockerfile provided here creates an image that contains the model binary along with a python webservice that runs on 9696 port at the endpoint <b>/predict</b> 
1. Download the repository to local folder, navigate to the folder midterm_prj.
2. Create docker image by running docker build command command `docker build -t midterm-prj .`
3. Once the image midterm-prj is created successfully, create a container from the image exiecting the command `docker run --rm -p 8181:9696 midterm-prj:latest`
4. Above command makes service available on 8181 local port. `http://localhost:8181/predict` Test the service by using predict-test.py. Alternatively it can be tested by other tools postman, HTTPie etc.