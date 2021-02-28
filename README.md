# Twitter Flask
Deploying Hate Speech Detection model on Retrieved Tweets using Flask

This repo is to re-learn the basic semantics of Flask, and to deploy a simple NLP model. The work here is based on the repo: https://github.com/lakshay-arora/Hate-Speech-Classification-deployed-using-Flask/tree/master

Note that you will need to set up a config.py file with the relevant Twitter API keys. 

## Deployment

The basic model is a TFIDF model with Logistic Regression. 

I deployed the model in Flask on Heroku at https://twitter-flask-johncai.herokuapp.com. Check it out! You can search for anything you want, and it will return 50 tweets, and flag the relevant tweets for hate speech.

## Further Steps

As a next step, I will be looking at using word embeddings or transformers.