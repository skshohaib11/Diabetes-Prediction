import streamlit as st
import pandas as pd
import pickle

model = pickle.load(open(r"Finalized_model.pkl","rb"))


def main():
    st.title("Diabetes Detection Test")
    st.header("Fill the details below to check if you are diabetic or not.")

    #sidebar configuration:
    st.sidebar.header("Know More about Diabetes")
    st.sidebar.markdown("[Click Here](https://www.niddk.nih.gov/about-niddk/research-areas/diabetes)") 

    #adding feature inputs:
    col1, col2 = st.columns(2)
    with col1:
        pregnancies = st.number_input("Number of Pregnancies",0,20)
    with col2:
        glucose = st.number_input("Select Your Glucose Level",0,250)
    
    col3, col4 = st.columns(2)
    with col3:
        Blood_Presure = st.number_input("Select Your Blood Pressure Level",0,150)
    with col4:
        Skin_thickness = st.number_input("Select your skin thickness",0,120,30)
    
    col5,col6 = st.columns(2)
    with col5:
        insulin_level = st.number_input("Select your insulin level",0,1000,30)
    with col6:
        bmi = st.number_input("Select your BMI",0,100,30)
    
    col7, col8 =st.columns(2)
    with col7 :
        Diabetes_Pedigree_Function = st.number_input("Select your Diabetes Pedigree Function",0,3)
    with col8:
        age  = st.number_input("Please enter your age", 18, 90)

    # Gathering the Data so that we can collect user entered inputs:
    data = {"Pregnancies":pregnancies,"Glucose":glucose,"BloodPressure":Blood_Presure,"SkinThickness":Skin_thickness,"Insulin":insulin_level,'BMI':bmi,"DiabetesPedigreeFunction":Diabetes_Pedigree_Function,'Age':age}
    df = pd.DataFrame(data, index=[0])   
    return df

data = main()

if st.button("Check"):                                                                
    result = model.predict(data)                                                        
    proba=model.predict_proba(data)                                                        

    if result[0] == 1:
        st.write("You Are Diabetic")
        st.write("Click Below To Control Your Diabetes.")  
        st.write("https://www.mayoclinic.org/diseases-conditions/type-2-diabetes/in-depth/diabetes-prevention/art-20047639")
    else:
        st.write("You Are Not Diabetic")
        st.write("Click Below To Prevent Diabetes by changing your life style, Its Never Too Late!.")  
        st.write("https://www.mayoclinic.org/diseases-conditions/type-2-diabetes/in-depth/diabetes-prevention/art-20047639")
        

# Prepared By.
st.subheader('Prepared By')
st.write("Shohaib Shaikh")




