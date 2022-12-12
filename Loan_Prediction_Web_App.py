# -*- coding: utf-8 -*-
"""
Created on Sun Nov 27 2022

@author: Mai Anh Võ
"""

import numpy as np
import pickle
import streamlit as st


# loading the saved model
loaded_model = pickle.load(open('./Loan_prediction.pkl', 'rb'))


# creating a function for Prediction

def loan_prediction(input_data):

    # changing the input_data to numpy array
    input_data_array = np.asarray(input_data, dtype=np.float64)
    
    # normalize data
    input_data_array[8] = np.log(input_data_array[8])
    input_data_array[9] = np.log(input_data_array[9])
    input_data_array[10] = np.log(input_data_array[10])
    input_data_array[10] = str(input_data_array[10]).replace('-inf', '0')
    
    # change dtype to object
    input_data_array = input_data_array.astype('object')

    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_array.reshape(1,-1)

    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)
    

    if (prediction[0] == 0):
      return 'Loan disapproved'
    else:
      return 'Loan approved'
  
    
  
def main():
    
    
    # giving a title
    st.title('Loan Prediction Web App')
    
    
    # getting the input data from the user
    
    
    Gender = st.text_input('Gender (Female=0, Male=1)')
    Married = st.text_input('Maritual Status (Not Married=0, Married=1)')
    Dependents = st.text_input('Number of dependents')
    Education = st.text_input('Education (Graduate=0, Not graduate=1)')
    Self_Employed = st.text_input('Self Employment (No=0, Yes=1)')
    Loan_Amount_Term = st.text_input('Term of a loan in months')
    Credit_History = st.text_input('Credit history meets guidelines')
    Property_Area = st.text_input('Property Area (Rural=0, Semi-Urban=1, Urban=2)')
    LoanAmount = st.text_input('Loan amount in thousands')
    ApplicantIncome = st.text_input('Applicant income')
    CoapplicantIncome = st.text_input('Coapplicant income')
    
    
    
    # code for Prediction
    classification = ''
    
    # creating a button for Prediction
    
    if st.button('Loan Prediction Result'):
        classification = loan_prediction([Gender, Married, Dependents, Education, Self_Employed, Loan_Amount_Term, Credit_History, Property_Area, LoanAmount, ApplicantIncome, CoapplicantIncome])
        
        
    st.success(classification)
    
    
    
    
    
if __name__ == '__main__':
    main()
