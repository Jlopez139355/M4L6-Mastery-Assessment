from pathlib import Path
import csv
import plotly.express as px

# Path to my CSV file
path = Path("C:\\Users\\jlopez139355\\Downloads\\MCD64A1_burned_area_full_dataset_2002-2023.csv")

# Read the file with a specific encoding (try 'utf-8-sig' or 'latin1' if utf-8 doesn't work)
with path.open('r', encoding='utf-8-sig') as file:
    lines = file.read().splitlines()

# Create a CSV reader
reader = csv.reader(lines)
header_row = next(reader)

# Print out the header to verify column names
print("Header row:", header_row)

# Extract the relevant columns based on the new structure
# Assumes columns are: year, month, gid_0, country, gid_1, region, forest, savannas, shrublands_grasslands, croplands, other
years, months, countries, regions, forests, savannas, shrublands, croplands, others = [], [], [], [], [], [], [], [], []

# Iterate through the rows and extract data
for row in reader:
    try:
        year = int(row[0])        # Year of the fire event
        month = int(row[1])       # Month of the fire event
        region = row[5]           # Region of the fire event
        forest = float(row[6])    # Forest area affected (assuming this is a proxy for fire intensity)
        savanna = float(row[7])   # Savannas affected (similarly)
    except ValueError:
        # Handle any missing or corrupt data
        print(f"Invalid data for row: {row}")
    else:
        # use the data
        years.append(year)
        months.append(month)
        regions.append(region)
        forests.append(forest)
        savannas.append(savanna)

# At this point, you will have lists of the data you want to plot (years, regions, fire areas)
# Since we don't have latitude and longitude directly, we will focus on visualizing based on regions

# Plot the fire impact data on a world map
title = "Global wildfire activity impact by region"
fig = px.scatter_geo(
    lat=regions,    # For now, we use regions, but you might need lat-lon if available
    lon=regions,    # This assumes you have latitude and longitude (update this accordingly)
    size=forests,   # Size of points based on the 'forest' column (or 'savanna', etc.)
    title=title,
    color=forests,  # Color by 'forest' area (can change to another category like 'savanna')
    color_continuous_scale='Viridis',
    labels={'color': 'Forest Area (Affected by Fires)'},
    projection='natural earth'
)

# Show the map
fig.show()
