import geopandas as gpd
from shapely.affinity import scale

# create constants for the state scale factors
ALASKA_SCALE_FACTOR_X = 0.64
HAWAII_SCALE_FACTOR_X = 1.1

# method for applying an affine transformation to a state polygon
def scale_geometry_for_state(gdf: gpd.GeoDataFrame, state_code: str, scale_factor_x: float) -> gpd.GeoDataFrame:
    """
    Apply horizontal scaling transformation to the geometry of a specific state in the GeoDataFrame.
    
    Params:
    - gdf: GeoDataFrame containing geospatial data
    - state_code: 2-letter postal code of the state (e.g., 'AK', 'HI')
    - scale_factor_x: the scale factor to be applied horizontally
    
    Returns:
    - gdf: Updated GeoDataFrame with scaled geometries for the specified state
    """

    state_data = gdf.loc[gdf['STUSPS'] == state_code]
    scaled_geometry = state_data['geometry'].apply(lambda geom: scale(geom, xfact=scale_factor_x, yfact=1.0))
    gdf.loc[gdf['STUSPS'] == state_code, 'geometry'] = scaled_geometry

    return gdf

# method for loading in a shapfile for creating an electoral college map
def load_df(path: str) -> gpd.GeoDataFrame:
    """
    Load a GeoDataFrame for plotting the electoral college and apply scaling to Alaska and Hawaii.
    
    Params:
    - path: The path to the shapefile.
    
    Returns:
    - gdf: A GeoDataFrame containing the electoral college data with Alaska and Hawaii transformed.

    """
    try:
        gdf = gpd.read_file(path)
    except Exception as e:
        print(f"Error loading shapefile: {e}")
        return None

    # apply the appropriate transformations for Alaska and Hawaii
    gdf = scale_geometry_for_state(gdf, 'AK', ALASKA_SCALE_FACTOR_X)
    gdf = scale_geometry_for_state(gdf, 'HI', HAWAII_SCALE_FACTOR_X)
    
    return gdf