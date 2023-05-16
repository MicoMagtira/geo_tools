import geopandas as gpd
from shapely.geometry import Point, Polygon


def get_centroid(gdf, geometry_column):

    # Create a new column for the centroid
    gdf['centroid'] = None
    
    # Iterate over the rows of the GeoDataFrame
    for i, row in gdf.iterrows():
        # Get the multipolygon geometry
        multipoly = row[geometry_column]
        
        # Calculate the centroid
        centroid = multipoly.centroid
        
        # Set the centroid in the new column
        gdf.at[i, 'centroid'] = centroid
        
    # Convert the 'centroid' column to a GeoSeries
    centroid_series = gpd.GeoSeries(gdf['centroid'], crs=gdf.crs)
    
    # Create a new GeoDataFrame with the centroids
    centroid_gdf = gpd.GeoDataFrame(geometry=centroid_series)
    
    return centroid_gdf

def get_area(gdf, geometry_col):
    
    # Convert the geometries to Mercator projection
    gdf[geometry_col] = gdf[geometry_col].to_crs(epsg=3857)
    
    # Create a new column for the area
    gdf['area'] = None
    
    # Iterate over the rows of the GeoDataFrame
    for i, row in gdf.iterrows():
        
        # Get the geometry in the specified column
        geom = row[geometry_col]
        
        # Check if the geometry is valid
        if geom.is_valid:
            # Calculate the area
            area = geom.area

            # Set the area in the new column
            gdf.at[i, 'area'] = area
            
        else:
            # If the geometry is not valid, set the area to None
            gdf.at[i, 'area'] = None
    
    # Filter out non-geometry objects from the 'area' column
    area_geom = gdf[gdf['area'].apply(lambda x: isinstance(x, Polygon) or isinstance(x, Point))]['area']
    
    # Convert the 'area' column to a GeoSeries
    area_series = gpd.GeoSeries(area_geom, crs=gdf.crs)
    
    # Create a new GeoDataFrame with the areas
    area_gdf = gpd.GeoDataFrame(geometry=area_series, crs=gdf.crs)
    
    return area_gdf
