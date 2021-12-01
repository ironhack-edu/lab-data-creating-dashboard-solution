![logo_ironhack_blue 7](https://user-images.githubusercontent.com/23629340/40541063-a07a0a8a-601a-11e8-91b5-2f13e4e6b441.png)

# Lab | Data - Creating a dashboard


Create a streamlit application for the Sakila database. This application must contain three pages:

- Home
- EDA
- Prediction


### Instructions

#### Home page

Must contain a title and an image of your choice.

#### EDA page

Must contain the following plots:

- A line plot of daily rentals by each store in 2005
- A bar plot with the total benefit by each store
- A dataframe with the top five most rented movies by each store in 2005. Hint: use `st.dataframe(df)`

#### Prediction page

Must contain a `st.text_area()` that will allow the user to input a movie description and get a prediction from the movie rating prediction model created yesterday.
It also must contain an `st.button("Get Your Prediction")` button.