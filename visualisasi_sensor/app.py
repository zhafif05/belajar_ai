import streamlit as st
from streamlit_autorefresh import st_autorefresh
import pandas as pd
import mysql.connector
import matplotlib.pyplot as plt
import seaborn as sns
def load_data():
 conn = mysql.connector.connect(
 host="localhost",
 user="root",
 password="",
 database="iot_dashboard"
 )
 query = "SELECT esp_suhu, esp_kelembapan,co,waktu FROM datasensor ORDER BY waktu ASC"
 df = pd.read_sql(query, conn)
 conn.close()
 return df

st.title("Dashboard Data Sensor Realtime dengan Dropdown")

st_autorefresh(interval=5000, key="refresh")

st.title("Contoh Autorefresh Streamlit")
st.write("Halaman ini akan refresh setiap 5 detik.")

df = load_data()

sensor_options = ["esp_suhu", "esp_kelembapan", "co"]
selected_sensor = st.selectbox("Pilih sensor yang ingin ditampilkan:", sensor_options)
st.subheader(f"Data {selected_sensor.capitalize()} Terbaru")
st.dataframe(df[["waktu", selected_sensor]].tail(10))
st.subheader(f"Grafik {selected_sensor.capitalize()}")
fig, ax = plt.subplots()
sns.lineplot(x="waktu", y=selected_sensor, data=df, ax=ax,
marker="o")
plt.xticks(rotation=45)
st.pyplot(fig)
