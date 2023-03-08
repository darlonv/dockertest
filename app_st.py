import streamlit as st

st.title("Dockertest v 2.0")

val = st.text_input('Valor')
val = int(val)

quad = val**2
st.write(f'Quadrado: {quad}')


