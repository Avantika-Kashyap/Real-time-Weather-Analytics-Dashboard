import streamlit as st
import pandas as pd
import plotly.express as px

# 1. Page Title and Configuration
st.set_page_config(page_title="Real-Time Weather Dashboard", layout="wide", page_icon="🌤️")

st.title("🌤️ Real-Time Weather Analytics Dashboard")
st.markdown("---")

# 2. Read the CSV Data
try:
    df = pd.read_csv("live_weather_data.csv")
    
    # 3. Top Metrics Section (KPIs)
    st.subheader("📌 Key Weather Metrics")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        highest_temp_city = df.loc[df['Temperature (°C)'].idxmax()]['City']
        highest_temp = df['Temperature (°C)'].max()
        st.metric(label="🔥 Hottest City", value=f"{highest_temp}°C", delta=highest_temp_city)
        
    with col2:
        lowest_temp_city = df.loc[df['Temperature (°C)'].idxmin()]['City']
        lowest_temp = df['Temperature (°C)'].min()
        st.metric(label="❄️ Coolest City", value=f"{lowest_temp}°C", delta=lowest_temp_city)
        
    with col3:
        avg_humidity = round(df['Humidity (%)'].mean(), 2)
        st.metric(label="💧 Average Humidity", value=f"{avg_humidity}%")
        
    st.markdown("---")
    
    # 4. Charts Section (Visualizations)
    st.subheader("📊 Data Visualizations")
    chart_col1, chart_col2 = st.columns(2)
    
    with chart_col1:
        # Bar Chart for Temperature Comparison
        st.markdown("#### Temperature Comparison across Cities")
        fig_temp = px.bar(df, x='City', y='Temperature (°C)', color='Temperature (°C)',
                          color_continuous_scale='Bluered', text_auto=True)
        st.plotly_chart(fig_temp, use_container_width=True)
        
    with chart_col2:
        # Line Chart for Wind Speed
        st.markdown("#### Wind Speed Analytics")
        fig_wind = px.line(df, x='City', y='Wind Speed (m/s)', markers=True,
                           labels={'Wind Speed (m/s)': 'Wind Speed'})
        st.plotly_chart(fig_wind, use_container_width=True)
        
    st.markdown("---")

    # 5. Interactive Data Table Section
    st.subheader("📋 Raw Live Data View")
    st.dataframe(df, use_container_width=True)

except FileNotFoundError:
    st.error("❌ 'live_weather_data.csv' file nahi mili. Pehle pipeline chala kar file generate kijiye.")
except Exception as e:
    st.warning(f"Something went wrong: {e}")