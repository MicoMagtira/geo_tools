import geopandas as gpd
from geo_tools import get_centroid
from geo_tools import get_area

# Create a GeoDataFrame with a column containing multipolygons
gdf = gpd.read_file('src/All residential buildings in Manila, Metropolitan Manila.shp')
get_centroid(gdf,"geometry")
get_area(gdf,"geometry")

print(gdf)