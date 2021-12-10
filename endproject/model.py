
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
stop_words = set(stopwords.words('english'))

class algo:
    # initialize the class with the training model
    def __init__(self,model,trained_model):
        self.model = model
        self.trained_model = trained_model
        self.dic = {1:'politics', 2:'business', 3:'tech', 4:'entertainment', 5:'sport'}

    #tokenize the text
    def tokenize(self,text):
        tokens = word_tokenize(text)
        return tokens

    # remove the stopwords
    def remove(self,tokens):
        tokens = [token for token in tokens if token not in stop_words]
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


