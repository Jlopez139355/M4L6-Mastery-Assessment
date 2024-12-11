import requests
import pandas as pd
import matplotlib.pyplot as plt

# Download earthquake data from USGS
url = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_hour.geojson"
response = requests.get(url)

# make sure response works
if response.status_code == 200:
    earthquake_data = response.json()
else:
    print(f"Failed to fetch data: {response.status_code}")
    earthquake_data = None

# get information
magnitude = []
latitude = []
longitude = []
location = []

# use data if it works
if earthquake_data:
    for feature in earthquake_data['features']:
        properties = feature['properties']
        geometry = feature['geometry']

        # get magnitude, location, and coordinates
        magnitude.append(properties['mag'])
        latitude.append(geometry['coordinates'][1])  
        longitude.append(geometry['coordinates'][0])
        location.append(properties['place'])

    # Create a DataFrame to organize the data
    df = pd.DataFrame({
        'Magnitude': magnitude,
        'Latitude': latitude,
        'Longitude': longitude,
        'Location': location
    })

    # Create a visualization
    plt.figure(figsize=(10, 6))

    # move plot with longitude, latitude, and magnitude as the size of the points
    scatter = plt.scatter(df['Longitude'], df['Latitude'], s=df['Magnitude'] * 20, c=df['Magnitude'], cmap='viridis', alpha=0.7)

    # use a colorbar to represent the magnitude scale
    plt.colorbar(label='Magnitude')

    # add labels and title
    plt.title('Earthquakes in the Last Hour', fontsize=14)
    plt.xlabel('Longitude')
    plt.ylabel('Latitude')

    # names the locations on the plot/graph
    for i, row in df.iterrows():
        plt.annotate(row['Location'], 
                     (row['Longitude'], row['Latitude']),
                     fontsize=8, 
                     alpha=0.7, 
                     xytext=(5, 5), 
                     textcoords='offset points')

 
plt.show()
