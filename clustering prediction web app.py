# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 12:37:06 2024

@author: Siddhi
"""

import numpy as np
import pickle
import streamlit as st


# loading the saved model
#loaded_model = pickle.load(open('D:/Work/Machine Learning/Deploying Machine Learning model/trained_model.sav', 'rb'))
#C:\Users\askpr\ExR\Project_Deployment\Weekday
loaded_model = pickle.load(open('C:/Users/Siddhi/datascience/project/train_model.sav', 'rb'))
# creating a function for Prediction

def clustering_prediction(input_data):
    

    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)

    if (prediction == 0):
      return 'The person will buy the new product'
    else:
      return 'The person will not buy the new product'
  
    
  
def main():
    
    
    # giving a title
    st.title('customer segmentation Web App')
    
    
    # getting the input data from the user
    
    
    Age = st.text_input('Age of a person')
    
    Marital_status= st.text_input('type 0 if in relationship type 1 if single')
    Total_children = st.text_input('number of children ')
    Income = st.text_input('Income value')
    num_visits = st.text_input('number of visits')
    complain = st.text_input('number of complains')
    Total_spending = st.text_input('amount spent')
    Total_Purchased = st.text_input('Item purchased')
    
    
    # code for Prediction
    cluster_result = ''
    
    # creating a button for Prediction
    
    if st.button('Customer segmentation result'):
        cluster_result = clustering_prediction([Age,Marital_status,Total_children,Income,num_visits,complain,Total_spending,Total_Purchased])
        
        
    st.success(cluster_result)
    
    
    
    
    
if __name__ == '__main__':
    main()