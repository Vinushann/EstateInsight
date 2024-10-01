import pickle
import json
import numpy as np
import streamlit as st
import pandas as pd  # Importing pandas to format the user inputs as a DataFrame

# Global variables
__locations = None
__data_columns = None
__model = None

# Function to load model and columns
def load_saved_artifacts():
    global __data_columns
    global __locations

    # Load columns from JSON
    with open("columns.json", "r") as f:
        __data_columns = json.load(f)['data_columns']
        __locations = __data_columns[3:]  # first 3 columns are sqft, bath, bhk

    # Load the trained model from pickle
    global __model
    if __model is None:
        with open('banglore_home_prices_model_2.pickle', 'rb') as f:
            __model = pickle.load(f)

# Function to estimate the price based on user inputs
def get_estimated_price(location, sqft, bhk, bath):
    try:
        loc_index = __data_columns.index(location.lower())
    except:
        loc_index = -1
    # print(loc_index) #This gives the col number of the "location" which we get, of columns.json

    # Initialize a zero array for the input features
    x = np.zeros(len(__data_columns)) 
    # print(x.shape) #This is a 1d array(row) with 243 cols(ie, the cols in columns.json). The reason to create a zeros array is cuz then only for the passed location parameter, we can assign the one hot encoding this noh
    x[0] = sqft
    x[1] = bath
    x[2] = bhk
    if loc_index >= 0:
        x[loc_index] = 1  # Set the correct location index to 1 (one-hot encoding)
    
    #So, now when print x, it's values are like this(ie if the inputs are for sqft being 1250, bath being 2, bhd being 2, and the location being "1st phase jp nagar")
    # print(x) # [1250.0, 2, 2, 0, 1, 0, ..., 0, 0, 0, 0, 0, 0, 0, 0]
    
    # print(__model.predict([x]))#This gives [198.6669157724992]
    # print(__model.predict([x])[0]) #This gives 198.6669157724992

    # Predict the price and return it
    return round(__model.predict([x])[0], 2)

# Streamlit UI starts here
def main():
    # Load the model and columns
    load_saved_artifacts()

    # Page Title
    st.write("""
    # Bengaluru House Price Prediction App
    Use the sliders to adjust input values and get predictions based on a pre-trained model.
    """)

    # Sidebar for user inputs
    st.sidebar.header('User Input Parameters')

    # Input fields for location, sqft, bhk, bath in the sidebar
    location = st.sidebar.selectbox("Select Location", __locations)
    sqft = st.sidebar.slider('Square Foot Area (sqft)', 300, 10000, 1000)
    bath = st.sidebar.slider('Number of Bathrooms', 1, 13, 2)
    bhk = st.sidebar.slider('Number of Bedrooms (BHK)', 1, 9, 2)

    # Display the user inputs as a table
    user_input_data = {
        'Location': location,
        'Square Foot Area': sqft,
        'Bathrooms': bath,
        'Bedrooms (BHK)': bhk
    }

    st.subheader('User Input Parameters')
    st.write(pd.DataFrame([user_input_data]))  # Display user inputs in a table format

    # Button to predict price
    if st.button("Estimate Price"):
        # Show result only after clicking the button
        price = get_estimated_price(location, sqft, bhk, bath)
        st.success(f"The estimated price for the property is ₹ {price:,.2f} lakh")

if __name__ == '__main__':
    main()
    # print(get_estimated_price("1st block jayanagar", 1000, 2, 1))

