import streamlit as st
import pandas as pd

# Initialize the session state with demo data if not already initialized
if 'patients' not in st.session_state:
    st.session_state['patients'] = pd.DataFrame({
        'Patient ID': [1, 2, 3, 4, 5],
        'Name': ['John Doe', 'Jane Smith', 'Alice Johnson', 'Bob Brown', 'Charlie Black'],
        'Age': [70, 65, 80, 75, 60],
        'Gender': ['Male', 'Female', 'Female', 'Male', 'Male'],
        'Health Condition': ['Hypertension', 'Diabetes', 'Arthritis', 'Heart Disease', 'COPD'],
        'Living Situation': ['Alone', 'With Family', 'With Spouse', 'Alone', 'With Family'],
        'Social Support': ['Good', 'Poor', 'Good', 'Average', 'Poor'],
        'Mobility (TUG Test)': [12.5, 14.0, 13.0, 15.5, 16.0],  # in seconds
        'Cognitive Function (Mini-Cog)': [4, 3, 5, 2, 3]  # Mini-Cog score
    })

# Function to add a new patient
def add_patient(patient_id, name, age, gender, health_condition, living_situation, social_support, mobility, cognitive_function):
    new_patient = pd.DataFrame({
        'Patient ID': [patient_id],
        'Name': [name],
        'Age': [age],
        'Gender': [gender],
        'Health Condition': [health_condition],
        'Living Situation': [living_situation],
        'Social Support': [social_support],
        'Mobility (TUG Test)': [mobility],
        'Cognitive Function (Mini-Cog)': [cognitive_function]
    })
    st.session_state['patients'] = pd.concat([st.session_state['patients'], new_patient], ignore_index=True)

# Function to delete a patient
def delete_patient(patient_id):
    st.session_state['patients'] = st.session_state['patients'][st.session_state['patients']['Patient ID'] != patient_id]

# Function to update a patient
def update_patient(patient_id, name, age, gender, health_condition, living_situation, social_support, mobility, cognitive_function):
    st.session_state['patients'].loc[st.session_state['patients']['Patient ID'] == patient_id, ['Name', 'Age', 'Gender', 'Health Condition', 'Living Situation', 'Social Support', 'Mobility (TUG Test)', 'Cognitive Function (Mini-Cog)']] = [name, age, gender, health_condition, living_situation, social_support, mobility, cognitive_function]

# App description
st.title("Home Health Assessment")
st.write("This app collects information for a home health assessment. You can create, delete, and update patient information.")

# Display the patient data
st.header("Patient Data")
st.dataframe(st.session_state['patients'])

# Sidebar for patient operations
st.sidebar.header("Manage Patients")

# Add new patient
st.sidebar.subheader("Add New Patient")
with st.sidebar.form("add_patient_form"):
    new_patient_id = st.number_input("Patient ID", min_value=1, value=1)
    new_patient_name = st.text_input("Name")
    new_patient_age = st.number_input("Age", min_value=0, max_value=120, value=0)
    new_patient_gender = st.selectbox("Gender", ["Male", "Female", "Other"])
    new_patient_health_condition = st.text_input("Health Condition")
    new_patient_living_situation = st.selectbox("Living Situation", ["Alone", "With Family", "With Spouse", "Other"])
    new_patient_social_support = st.selectbox("Social Support", ["Good", "Average", "Poor"])
    new_patient_mobility = st.number_input("Mobility (TUG Test in seconds)", min_value=0.0, value=0.0, step=0.1)
    new_patient_cognitive_function = st.number_input("Cognitive Function (Mini-Cog score)", min_value=0, max_value=5, value=0)
    add_patient_submitted = st.form_submit_button("Add Patient")
    if add_patient_submitted:
        add_patient(new_patient_id, new_patient_name, new_patient_age, new_patient_gender, new_patient_health_condition, new_patient_living_situation, new_patient_social_support, new_patient_mobility, new_patient_cognitive_function)
        st.sidebar.success(f"Patient {new_patient_name} added successfully!")

# Delete patient
st.sidebar.subheader("Delete Patient")
delete_patient_id = st.sidebar.number_input("Patient ID to Delete", min_value=1, value=1)
delete_patient_button = st.sidebar.button("Delete Patient")
if delete_patient_button:
    delete_patient(delete_patient_id)
    st.sidebar.success(f"Patient ID {delete_patient_id} deleted successfully!")

# Update patient
st.sidebar.subheader("Update Patient")
with st.sidebar.form("update_patient_form"):
    update_patient_id = st.number_input("Patient ID to Update", min_value=1, value=1)
    update_patient_name = st.text_input("Updated Name")
    update_patient_age = st.number_input("Updated Age", min_value=0, max_value=120, value=0)
    update_patient_gender = st.selectbox("Updated Gender", ["Male", "Female", "Other"])
    update_patient_health_condition = st.text_input("Updated Health Condition")
    update_patient_living_situation = st.selectbox("Updated Living Situation", ["Alone", "With Family", "With Spouse", "Other"])
    update_patient_social_support = st.selectbox("Updated Social Support", ["Good", "Average", "Poor"])
    update_patient_mobility = st.number_input("Updated Mobility (TUG Test in seconds)", min_value=0.0, value=0.0, step=0.1)
    update_patient_cognitive_function = st.number_input("Updated Cognitive Function (Mini-Cog score)", min_value=0, max_value=5, value=0)
    update_patient_submitted = st.form_submit_button("Update Patient")
    if update_patient_submitted:
        update_patient(update_patient_id, update_patient_name, update_patient_age, update_patient_gender, update_patient_health_condition, update_patient_living_situation, update_patient_social_support, update_patient_mobility, update_patient_cognitive_function)
        st.sidebar.success(f"Patient ID {update_patient_id} updated successfully!")
