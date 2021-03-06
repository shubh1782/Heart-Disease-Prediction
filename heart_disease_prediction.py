# -*- coding: utf-8 -*-
"""Heart Disease Prediction

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1YQ5zUVL0oV_J10xQmtYNoRTST-jN_x5Y

Step 1 : Data -> Data Pre Processing -> Train Test Split -> Model

Step 2 : New Data -> Trained Model -> Prediction

Importing the Dependencies
"""

import numpy as np # to make some numpy arrays
import pandas as pd # useful for creating dataframe (dataframe are nothing but structured table)
from sklearn.model_selection import train_test_split # to split the original dataset into taining and testing data
from sklearn.linear_model import LogisticRegression # Importing logistic regression model 
from sklearn.metrics import accuracy_score # to evaluate our accuracy

"""Data Collection and Processing """

#loading csv data to pandas dataframe

heart_data = pd.read_csv('/content/data.csv')

#printing first 5 rows of df
heart_data.head()

#printing last 5 rows of df
heart_data.tail()

# number of rows and columns
heart_data.shape

#getting some info
heart_data.info()

#statistical Measures  about the data
heart_data.describe()

#checking sor missing values
heart_data.isnull().sum()
# there is no missing or null values if present then we can use like imputaion

#checking the distibuion of Target variables
heart_data['target'].value_counts() # .value_counts tells us the total counts present for the resp column
#we need to have almost equal distibution in both classes 
#if the distrubution is very unequal then we have to do some processing

"""1 -> defective heart
0 -> healthy heart

Splitting the Features and Target
"""

#features can be used to predict the target

#all the features are stored in variable X and targets are stored in varibale Y
X = heart_data.drop(columns = 'target', axis = 1)#whenever dropping any column we have to mention the axis. axis=1 for column and axis=0 for rows
Y = heart_data['target'] #storing the dropped target into Y

print(Y)

"""Splitting the data into training data and test data"""

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, stratify = Y, random_state = 2)
#X_train = the features of all the training data
#X_test = the features of all the test data
#Y_train = the target of all these features present in the X_train
#Y_test = the target of all these features present in the X_test
#test_size = how much percent of data you want as the test data , here 0.2 refers 20%
#stratify = similar proportion of 0 and 1 in train and test data as it was in the original datset (even distribution throughout training and testing data)
#random_state = controls the shuffling of data

print (X.shape, X_train.shape, X_test.shape)
#as we can see 80% of data has gone to X_train and 20% to X_test

"""Training the Model"""

#here we are using Logistic regression model bcoz it is very useful for binary classification

model = LogisticRegression()

#training the model using training data -> (.fit function is used)

model.fit(X_train, Y_train) # this will find the relationship between features of X_train and target of Y_train

#now we can use this trained model to predict new values

"""Model Evaluation

Accuracy Score
"""

#accuracy on training data using prediction

#in this we will be giving on the X_train(features) alone and ask the model to predict the target
#.predict function predicts the target value
#storing the target value in variable X_train_prediction
X_train_prediction = model.predict(X_train)
#accuracy score function helps to find the accuracy 
#we will be storing the accuray value in this variable training_data_accuracy
training_data_accuracy = accuracy_score(X_train_prediction, Y_train)

print ("Accuracy on training data:", training_data_accuracy)

#accuracy on testing data using prediction

X_test_prediction = model.predict(X_test)
testing_data_accuracy = accuracy_score(X_test_prediction, Y_test)

print ("Accuracy on testing data:", testing_data_accuracy)

#the accuracy score on testing and training data should be almost same. if the differe is way too large then it means our model is overfitted

"""Building a Predictive System"""

input_data = (37,1,2,130,250,0,1,187,0,3.5,0,0,2)
# change the input data to a numpy array
input_data_as_numpy_array = np.asarray(input_data) #asarray converts the tuple into numpy array

#we need to reshape the array it is imp to tell our model that we want to predict for only one instance or else the model will consider the initial shape of dataset
input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

prediction = model.predict(input_data_reshaped)
print(prediction)

if (prediction[0] == 0):
  print ("healthy")
else:
  print ("has heart disease")