
def eda(): 
    import streamlit as st
    from engine import get_engine
    from functions import get_rentals_by_store_date, get_top5_titles_by_store
    import matplotlib.pyplot as plt
    import seaborn as sns
    import plotly.express as px
    sns.set_theme(style="darkgrid")
    
    st.image('images/eda.jpeg')    
    password = st.text_input("Restricted access, please enter your password: ", type="password")
    if ( password ): 
        data = get_rentals_by_store_date(get_engine(password))       
        fig1 = px.line(data, x="Date", y="Rentals", color = 'store_id', title='Number of daily daily rentals')
        st.plotly_chart(fig1)
        
        data2 = data.groupby(['store_id']).sum('Benefit').reset_index()
        data2['store_id'] = data2['store_id'].astype('str')
        fig2 = px.bar(data2, x='store_id', y='Benefit',text='Benefit')
        st.plotly_chart(fig2)
        
        data3 = get_top5_titles_by_store(get_engine(password))
        st.dataframe(data3)