#Load English tokenizer, tagger, parser, NER and word vectors
import json
import spacy  
import en_core_web_sm
nlp = en_core_web_sm.load()
#sp = spacy.load('en_core_web_sm')

class algo_spacy:
    # initialize the class with the training model
    def __init__(self,model,trained_model):
        self.model = model
        self.trained_model = trained_model
        self.dic = {1:'politics', 2:'business', 3:'tech', 4:'entertainment', 5:'sport'}

    def load_json(self,filename = 'dic.json'):
        with open(filename, 'r') as f:
            data = json.load(f)
        return data

    def preprocess_spacy(self,para):
        lis =  []
        stop_words = self.load_json('dic.json')['stopwords']
        for sent in para.split("."):
            doci = nlp( sent )
            for token in doci:
                if token.text not in stop_words:
                    lis.append(token.lemma_)
        return lis

    # convert the doc to vector
    def doc2vec(self,article):
        doc = self.preprocess_spacy(article)
        return self.trained_model.infer_vector(doc)

    # predict the type of the article
    def predict_tag(self,article):
        predction = self.model.predict([self.doc2vec(article)])
        return self.dic[predction[0]]
























'''

import nltk
nltk.download()
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
import json

class algo_nltk:
    # initialize the class with the training model
    def __init__(self,model,trained_model):
        self.model = model
        self.trained_model = trained_model
        self.dic = {1:'politics', 2:'business', 3:'tech', 4:'entertainment', 5:'sport'}
        self.stop_words = self.load_json('dic.json')['stopwords']

    # load json stopwords in list variable
    def load_json(self,filename = 'dic.json'):
        with open(filename, 'r') as f:
            data = json.load(f)
        return data

    #tokenize the text
    def tokenize(self,text):
        tokens = word_tokenize(text)
        return tokens

    # remove the stopwords
    def remove(self,tokens):
        tokens = [token for token in tokens if token not in  self.stop_words]
        return tokens

    #lemmatize the text
    def lemma(self,tokens):
        lemmatizer = WordNetLemmatizer()
        lemmas = [lemmatizer.lemmatize(token) for token in tokens]
        return lemmas

    # preprocess the document text
    def preprocess(self,doc):
        lis=[]
        for text in doc.split("."):
            text = text.lower()
            tokens = self.tokenize(text)
            tokens = self.remove(tokens)
            tokens = self.lemma(tokens)
            lis+=tokens
        return lis

    # convert the doc to vector
    def doc2vec(self,article):
        doc = self.preprocess(article)
        return self.trained_model.infer_vector(doc)

    # predict the type of the article
    def predict_tag(self,article):
        predction = self.model.predict([self.doc2vec(article)])
        return self.dic[predction[0]]

'''