

from model import algo
import pickle
import streamlit as st

# load pickle file
with open('model.pickle', 'rb') as handle:
    model = pickle.load(handle)
with open('trained_model.pickle', 'rb') as handle:
    trained_model = pickle.load(handle)
pred_model = algo( model = model , trained_model = trained_model )

def prediction():
    st.title('BBC News Article Classification')
    st.write('This is a simple web app that predicts the category of an article based on the text of the article.')
    st.write('The model is trained on the BBC News dataset and is based on MLP classifier.')

    article  = st.text_input('Enter the article text:')


    if st.button('Predict'):
        pred_val = pred_model.predict_tag(article).upper()
        st.success('The article is classified as {}'.format( pred_val))

if __name__ == '__main__':
    prediction()