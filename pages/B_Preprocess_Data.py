import streamlit as st
import pandas as pd

#############################################

st.markdown("# Practical Applications of Machine Learning (PAML)")

#############################################

st.markdown("### Homework 0 - Introduction to Streamlit")

#############################################

st.markdown('# Preprocess Dataset')

###################### FETCH or RESTORE DATASET #######################

# Display original dataframe
uploaded_file = st.file_uploader("Upload a CSV file", type="csv")
# Read csv file in Panda DataFrame
dataset=pd.read_csv("/Users/rajshrijain/Documents/Cornell/Spring2024/PAML/Homework0/homework0/datasets/housing_paml.csv")
# Store the dataset dataframe as a session_state variable
st.session_state.dataset = dataset

# Restore dataset if already in memory
if 'dataset' in st.session_state:
# Display feature names and descriptions 
    st.markdown("### Dataset Features:")
    st.write(st.session_state.dataset.columns)
# Display dataframe as table
    st.markdown("### Dataset Inspection:")
    st.dataframe(st.session_state.dataset)
    # X = df 
    # (assign the dataset to variable X)
    X = st.session_state.dataset
    
# Show summary of missing values including 
#   1) number of categories with missing values, 
    num_categories_missing = dataset.isna().any().sum()
    st.markdown(f"1) Number of categories with missing values: {num_categories_missing}")
#   2) average number of missing values per category
    avg_missing_per_category = dataset.isna().sum().mean()
    st.markdown(f"2) Average number of missing values per category: {round(avg_missing_per_category, 2)}")
#   3) Total number of missing values
    total_missing_values = dataset.isna().sum().sum()
    st.markdown(f"3) Total number of missing values: {total_missing_values}")

    ############################################# MAIN BODY #############################################
    
    # Descriptive Statistics 
    ## Display the dataset
    st.dataframe(dataset)
    # Fetch numerical columns from the dataset
    numeric_columns = list(dataset.select_dtypes(['float','int']).columns)
    ## Create a menu for selecting multiple features
    selected_features = st.multiselect("Select features", options=numeric_columns)

    ## Create a second menu for selecting multiple statistics
    selected_statistics = st.multiselect("Select statistics",options=["Mean", "Median", "Max", "Min"])

    # Compute Descriptive Statistics including mean, median, min, max
    ## Function to compute selected statistics
    def compute_statistics(dataframe, features, statistics):
        result = {}
        for stat in statistics:
            if stat == "Mean":
                result[stat] = dataframe[features].mean()
            elif stat == "Median":
                result[stat] = dataframe[features].median()
            elif stat == "Max":
                result[stat] = dataframe[features].max()
            elif stat == "Min":
                result[stat] = dataframe[features].min()
        return result

    ## Compute selected statistics
    statistics_result = compute_statistics(dataset, selected_features, selected_statistics)

    ## Display the statistics
    for stat, values in statistics_result.items():
        st.write(f"{stat}:")
        st.write(values.round(2))