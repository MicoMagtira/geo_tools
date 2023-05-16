# geo_tools

This set of functions is designed to perform geospatial analysis on GeoDataFrames using the `geopandas` library.

## `get_centroid(gdf, geometry_column)`

This function takes a GeoDataFrame `gdf` and a string `geometry_column` representing the name of the column in `gdf` that contains the polygon/multipolygon geometries. It calculates the centroid of each polygon/multipolygon geometry in the specified column and returns a new GeoDataFrame containing the centroids.

### Parameters

- `gdf`: A GeoDataFrame containing polygon/multipolygon geometries.
- `geometry_column`: A string representing the name of the column in `gdf` that contains the polygon/multipolygon geometries.

### Returns

A GeoDataFrame containing the centroids of the polygon/multipolygon geometries in the specified column.

### Example Usage

```python
import geopandas as gpd

# Read in a GeoDataFrame containing polygon/multipolygon geometries
gdf = gpd.read_file('my_geodata.shp')

# Calculate the centroids
centroid_gdf = get_centroid(gdf, 'geometry')
```

## `get_area(gdf, geometry_column)`

This function takes a GeoDataFrame `gdf` and a string `geometry_column` representing the name of the column in `gdf` that contains the polygon/multipolygon geometries. It calculates the area of each polygon/multipolygon geometry in the specified column and returns a new GeoDataFrame containing the area.

### Parameters

- `gdf`: A GeoDataFrame containing polygon/multipolygon geometries.
- `geometry_column`: A string representing the name of the column in `gdf` that contains the polygon/multipolygon geometries.

### Returns

A GeoDataFrame containing the area of the polygon/multipolygon geometries in the specified column.

### Example Usage

```python
import geopandas as gpd

# Read in a GeoDataFrame containing polygon/multipolygon geometries
gdf = gpd.read_file('my_geodata.shp')

# Calculate the centroids
centroid_gdf = get_area(gdf, 'geometry')


