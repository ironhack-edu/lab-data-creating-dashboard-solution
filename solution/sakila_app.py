#############################################################
# This program lets you                                     #
# - Create a dashboard                                      #
# - Every dashboard page is created in a separate file      #  
#############################################################

import streamlit as st
from ml import ml
from eda import eda
from PIL import Image

def main():
  
    #############  
    # Main page #
    #############   
    
    options = ['Home','EDA','Prediction','Stop']
    choice = st.sidebar.selectbox("Menu", options, key = '1')
    
    if ( choice == 'Home' ):            
      st.title("Welcome to the Sakila web page!!")
      st.image('images/home.jpg')
      pass
      
    elif ( choice == 'EDA' ):
      eda()
      pass
      
    elif ( choice == 'Prediction' ):
      ml()
    
    else:
      st.stop()
      
    
main()