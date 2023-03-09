import streamlit as st

st.title("Dockertest v 2.1")

val = st.text_input('Valor')
if val:
    val = int(val)

    quad = val**2
    st.write(f'Quadrado: {quad}')


