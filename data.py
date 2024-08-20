import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import folium

%matplotlib inline

df = pd.read_csv('synthetic_traffic_accidents.csv')

print(df.head())

plt.figure(figsize=(10, 6))
sns.countplot(data=df, x='Time_of_Day', palette='viridis')
plt.title('Number of Accidents by Time of Day')
plt.xlabel('Time of Day')
plt.ylabel('Number of Accidents')
plt.show()

plt.figure(figsize=(10, 6))
sns.countplot(data=df, x='Road_Condition', palette='coolwarm')
plt.title('Number of Accidents by Road Condition')
plt.xlabel('Road Condition')
plt.ylabel('Number of Accidents')
plt.show()

plt.figure(figsize=(10, 6))
sns.countplot(data=df, x='Weather_Condition', palette='muted')
plt.title('Number of Accidents by Weather Condition')
plt.xlabel('Weather Condition')
plt.ylabel('Number of Accidents')
plt.show()

map_center = [df['Latitude'].mean(), df['Longitude'].mean()]
accident_map = folium.Map(location=map_center, zoom_start=6)

for i, row in df.iterrows():
    folium.CircleMarker(
        location=(row['Latitude'], row['Longitude']),
        radius=5,
        color='red',
        fill=True,
        fill_color='red'
    ).add_to(accident_map)

accident_map.save('accident_hotspots_map.html')
accident_map
