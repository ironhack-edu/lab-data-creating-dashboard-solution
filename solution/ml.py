import pickle
import numpy as np
import pandas as pd
import streamlit as st
from PIL import Image

def ml():
 
    st.image('images/ml.jpg')             
    st.title("Model to predict movie rating based on movie description")
    
    # loading the model
    models_path = 'models/'
    model_name = models_path + 'logistic_model.pkl'
    loaded_model = pickle.load(open(model_name, 'rb'))

    # loading the vectorizer
    transformers_path = 'transformers/'
    
    vectorizer_name = transformers_path + 'vectorizer.pkl'
    loaded_vectorizer = pickle.load(open(vectorizer_name, 'rb'))
    
    tf_transformer_name = transformers_path + 'tf_transformer.pkl'
    loaded_tf_transformer = pickle.load(open(tf_transformer_name, 'rb'))

    # Get movie info
    description = st.text_area("Please enter the movie description: ")
               
    # when 'Predict' is clicked, make the prediction and store it 
    if st.button("Get Your Prediction"): 
    
        X = pd.DataFrame({'description':[description]})
        X = X['description']
    
        X_counts = loaded_vectorizer.transform(X)
        X_counts_df = pd.DataFrame(X_counts.toarray(), columns=loaded_vectorizer.get_feature_names_out().tolist())
        X_tfidf = loaded_tf_transformer.transform(X_counts_df)

        # Making predictions 
        prediction = loaded_model.predict(X_tfidf)
        prediction_probs = loaded_model.predict_proba(X_tfidf)             
       
        if ( prediction == 'Yes'):
            st.success("The model predicts a status of {} with a probability of {:.2f}".format('Yes',prediction_probs[0,1]))
        else:
            st.error("The model predicts a status of {} with a probability of {:.2f}".format('No',prediction_probs[0,0]))