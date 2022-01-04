
 
import streamlit as st
import requests
import json

 
def fetch_api(article):
    url = 'https://classifyarticle.herokuapp.com/predict/{}'.format(article)
    response = requests.get(url)
    data =  response.json()
    output = data['results']
    return output

def prediction():
    st.title('BBC News Article Classification')
    st.write('This is a simple web app that predicts the category of an article based on the text of the article.')
    st.write('The model is trained on the BBC News dataset and is based on MLP classifier.')
    
    article  = st.text_input('Enter the article text:')

    if st.button('Predict'):
        pred_val =  fetch_api(article)
        st.success( pred_val['text'])

if __name__ == '__main__':
    prediction()