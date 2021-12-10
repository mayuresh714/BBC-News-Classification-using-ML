# BBC-News-Classification-using-ML
kaggle BBC news classify task

Text documents are one of the richest sources of data for businesses.

We’ll use a public dataset from the BBC comprised of 2225 articles, each labeled under one of 5 categories: business, entertainment, politics, sport or tech.

The dataset is broken into 1490 records for training and 735 for testing. The goal will be to build a system that can accurately classify previously unseen news articles into the right category.
link to the kaggle BBC news classify competition --
https://www.kaggle.com/c/learn-ai-bbc/overview

## Summary of this Repo.
This data was analysed ,processed ,converted to vector form using DOC2VEC gensim model.
Then we trained it on deifferent classification model like MLP,randomforest,logistic regression,etc. 
for different vector sizes 50,100,200,300 and noted that MUltilayer perceptron performed well in 
every case.So we saved the MLP model in .pickle file and used it in endproject (deployment time).

to check if this model works on new article process is as follows --
---1)  pick up some article from google and save it in /endproject/article.txt
---2)  go to /endproject/app.py and run it.

You will get result like this one......
![image](https://user-images.githubusercontent.com/56029669/145579621-9015b88e-e0c5-4226-966a-47c1209ecae0.png)

