import streamlit as st                  
import pandas as pd
import plotly.express as px

#############################################

st.markdown("# Practical Applications of Machine Learning (PAML)")

#############################################

st.markdown("### Homework 0 - Introduction to Streamlit")

#############################################

st.markdown('# Explore Dataset')

###################### FETCH DATASET #######################

# Dataset upload
uploaded_file = st.file_uploader("Upload a CSV file", type="csv")
# Read csv file in Panda DataFrame
# dataset=pd.read_csv("/Users/rajshrijain/Documents/Cornell/Spring2024/PAML/Homework0/homework0/datasets/housing_paml.csv")
if uploaded_file:
    dataset = pd.read_csv(uploaded_file)
    # Store the dataset dataframe as a session_state variable
    st.session_state.dataset = dataset

###################### EXPLORE DATASET #######################

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
###################### VISUALIZE DATASET #######################

# Collect user plot selection
def sidebar(dataset, label):
    if label:
        minimum_value = dataset[label].min()
        maximum_value = dataset[label].max()

        selected_range = st.sidebar.slider(
            f"Select range for {label}",
            minimum_value, maximum_value, (minimum_value, maximum_value)
        )

        filter = dataset[(dataset[label] >= selected_range[0]) & (dataset[label] <= selected_range[1])]
        return filter
    else:
        return dataset
# Specify Input Parameters
st.sidebar.header("Create Histogram Plot")
st.sidebar.header("Specify Input Parameters")
# selected_feature = st.sidebar.selectbox("Select a feature for inspection",options=list(dataset.columns))

# # Plot Histogram
# fig = px.histogram(dataset, x=selected_feature, title=f"Histogram for {selected_feature}")
# st.plotly_chart(fig)

if 'dataset' in st.session_state and st.session_state['dataset'] is not None:
    data = st.session_state['dataset']

    numeric_columns = list(data.select_dtypes(['float', 'int']).columns)

    selected_feature = st.sidebar.selectbox('Select Feature for Histogram', numeric_columns)

    filtered = sidebar(data, selected_feature)
    
    # Plot Histogram
    if selected_feature:
        fig = px.histogram(filtered, x=selected_feature)
        st.plotly_chart(fig)