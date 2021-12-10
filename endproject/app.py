from model import algo
import pickle

# load pickle file
with open('model.pickle', 'rb') as handle:
    model = pickle.load(handle)
with open('trained_model.pickle', 'rb') as handle:
    trained_model = pickle.load(handle)

def prediction():
    pred_model = algo( model = model , trained_model = trained_model )
    article = open( "article.txt" , 'r',encoding = "utf-8" )
    article = article.read()
    print(article)
    pred_val = pred_model.predict_tag(article).upper()
    print("\nThis article is about", pred_val)

if __name__ == '__main__':
    prediction()