#Import Dependencies 
import geopandas
import csv
import matplotlib.pyplot as plt
import pandas as pd
from pandas_function import make_df
from descartes.patch import PolygonPatch

#Reads all of the data csvs into pandas dataframes.
pop_df = pd.read_csv('Output/international_air.csv')
good_air = pd.read_csv('Output/good_air.csv')
med_air = pd.read_csv('Output/med_air.csv')
bad_air = pd.read_csv('Output/bad_air.csv')
terrible_air = pd.read_csv('Output/terrible_air.csv')

#Converts those pandas dataframes into geopandas dataframes
good_gdf = geopandas.GeoDataFrame(
    good_air, geometry=geopandas.points_from_xy(good_air['Longitude'], good_air['Latitude']))

med_gdf = geopandas.GeoDataFrame(
    med_air, geometry=geopandas.points_from_xy(med_air['Longitude'], med_air['Latitude']))

bad_gdf = geopandas.GeoDataFrame(
    bad_air, geometry=geopandas.points_from_xy(bad_air['Longitude'], bad_air['Latitude']))

terrible_gdf = geopandas.GeoDataFrame(
    terrible_air, geometry=geopandas.points_from_xy(terrible_air['Longitude'], terrible_air['Latitude']))

#Imports a world map.
world = geopandas.read_file(geopandas.datasets.get_path('naturalearth_lowres'))

#Tells the program that we are plotting on the world map for every continent except Antarctica
ax = world[world.continent != 'Antarctica'].plot(
    color='white', edgecolor='gray')

#Plots our points, dictating the size and color of the points based on that city's air quality.
good_gdf.plot(ax=ax, color='green', markersize=(good_gdf['Air Quality'])/4)
med_gdf.plot(ax=ax, color='yellow', markersize=(med_gdf['Air Quality'])/4)
bad_gdf.plot(ax=ax, color='orange', markersize=(bad_gdf['Air Quality'])/4)
terrible_gdf.plot(ax=ax, color='red', markersize=(terrible_gdf['Air Quality'])/4)


#Labels our graphs and saves the files.
plt.title("Air Quality of The World's Largest Cities (10/8/19)")
plt.xlabel("Longitude")
plt.ylabel("Latitude")
#I could not get the legend to work unfortunately. Geopandas doesn't seem to really cater towards that from what I've seen.
# plt.legend((good_gdf, med_gdf, bad_gdf, terrible_gdf), ('label1', 'label2', 'label3', 'terrible air'), loc = 'best')
plt.savefig("Output/Biggest_Cities_Air_Quality.png")

plt.show()

