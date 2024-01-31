import streamlit as st
import matplotlib.pyplot as plt

if 'data' in st.session_state:
    data = st.session_state.data
    st.text('Loading dataset')
    st.write(data)

    st.bar_chart(data['median_income'])
    st.map(data[['longitude','latitude']])

    # Matplotlib
    fig, ax = plt.subplots()
    ax.hist(data['median_income'], bins=30)

    st.pyplot(fig)


