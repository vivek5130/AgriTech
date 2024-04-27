import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
import sklearn.metrics as metrics 
from sklearn.linear_model import LogisticRegression 
import numpy as np 
# 1. Data Exploration
data = pd.read_csv('Crop_recommendation.csv')
# print(data.head())

# 2. Data Preprocessing
# Handle missing values, outliers, etc.

# 3. Feature Selection/Engineering
# X = data[['N','P','K','ph', 'temperature', 'humidity']]  # Features
# y = data['label']  # Target variable

features = data[['N', 'P', 'K', 'temperature', 
                 'humidity', 'ph']] 
  
# Put all the output into labels array 
labels = data['label'] 

# 4. Model Selection
model = DecisionTreeClassifier()

# 5. Model Training
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
X_train, X_test, Y_train, Y_test = train_test_split(features, 
                                       labels, 
                                       test_size=0.2, 
                                       random_state=42) 
LogReg = LogisticRegression(random_state=42).fit(X_train, Y_train) 
# model.fit(X_train, y_train)

# 6. Model Evaluation
# y_pred = model.predict(X_test)
predicted_values = LogReg.predict(X_test)
# print("Accuracy:", accuracy_score(y_test, y_pred))
accuracy = metrics.accuracy_score(Y_test, 
                                  predicted_values) 
# Find the accuracy of the model 
print("Logistic Regression accuracy: ", accuracy)


# 7. Deployment - You can create a function for crop recommendation
def recommend_crop(N, P, K,ph, temperature, humidity):
    try:
        print(type(N))
        print(type(P))
        print(type(K))
        print(type(ph))
        print(type(temperature))
        print(type(humidity))
        N = int(N)
        P = int(P)
        K = int(K)
        ph = int(ph)
        
        temperature = float(temperature)
        print("after type casting")
        print(type(N))
        print(type(P))
        print(type(K))
        print(type(ph))
        print(type(temperature))
        print(type(humidity))
        input_data = [[N, P, K , temperature, humidity,ph]]
        predicted_crop = LogReg.predict(input_data)
        # predicted_crop = model.predict(input_data)
        print(predicted_crop[0])
        print("Recommended Crop is:", predicted_crop[0])
        return predicted_crop[0]
    except Exception as e:
        print(e)
        return "error"


# Example usage:
# recommended_crop = recommend_crop(6.5, 25, 70)
# print("Recommended Crop:", recommended_crop)
