import streamlit as st
import joblib
import numpy as np

cols = ['REGULARITY', 'REGION_No Region', 'TOP_PACK', 'REGION_DAKAR']

reg = st.number_input("Enter Regularity", )

regions = ['FATICK', 'No Region', 'DAKAR', 'LOUGA', 'TAMBACOUNDA', 'KAOLACK',
       'THIES', 'SAINT-LOUIS', 'KOLDA', 'KAFFRINE', 'DIOURBEL',
       'ZIGUINCHOR', 'MATAM', 'SEDHIOU', 'KEDOUGOU']
reg_no_reg= st.number_input("if located in No Region  region 1 for yes 0 for no")
top_pac = st.number_input("Enter Top pack")
reg_dak= st.number_input("if located in Dakar region 1 for yes 0 for no")


with open("random_forest_model.pkl", "rb") as file:
    my_model = joblib.load(file)

if st.button("Predict"):
    if reg_no_reg == 1:
        st.success(my_model.predict(np.array([reg, 1, top_pac,0]).reshape(1,-1)), icon="✅")
    elif reg_dak == 1:
        st.success(my_model.predict(np.array([reg, 0, top_pac,1]).reshape(1,-1)), icon="✅")
    else:
        st.success(my_model.predict(np.array([reg, 0, top_pac,0]).reshape(1,-1)), icon="✅")

