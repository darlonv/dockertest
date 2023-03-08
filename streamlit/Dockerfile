FROM python

RUN pip install --upgrade pip
RUN pip install streamlit
RUN git clone https://github.com/darlonv/dockertest.git

CMD ["streamlit","run", "--server.address", "0.0.0.0","dockertest/app_st.py"]
