import streamlit as st
import plotly.express as px
from backend import get_data

st.title('Weather Forecast for the Next Days')
place = st.text_input('Place: ')
days = st.slider('Forecast Days', 
                    min_value=1, 
                    max_value=5, 
                    help='Select the number of forecast days')
option = st.selectbox('Select data to view',
                         ('Temperature', 'Sky'))
st.subheader(f'{option} the next {days} days in {place}')

if place:
    try:
        filtered_data = get_data(place, days)

        if option == 'Temperature':
            temperatures = [dict['main']['temp'] - 273.15 for dict in filtered_data]
            dates = [dict['dt_txt'] for dict in filtered_data] 
            figure = px.line(x=dates,
                                y=temperatures,
                                labels={'x': 'Date', 'y': 'Temperature (C)'})
            st.plotly_chart(figure)

        if option == 'Sky':
            sky_conditions = [dict['weather'][0]['main'] for dict in filtered_data]
            images = {'Clear': 'images/clear.png',
                        'Clouds': 'images/cloud.png',
                        'Rain': 'images/rain.png',
                        'Snow': 'images/snow.png'}
            img_paths = [images[condition] for condition in sky_conditions]
            st.image(img_paths, width=80)
    
    except KeyError:
        st.warning('Wrong place')