import geopandas as gpd
import pandas as pd
from shapely.affinity import scale
from poliscipy.shapefiles import state_shapefile
import importlib.resources as pkg_resources

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


def load_shapefile(year: str = "2024") -> gpd.GeoDataFrame:
    """
    Load the US state shapefile with electoral votes for the given year.
    Scales Alaska and Hawaii and adds defectors columns.

    Params:
    - year : str, default "2024"
        The election year to load electoral votes for. Must match a column in
        the electoral_votes.csv file (e.g., "2024", "2016").

    Returns:
    - gdf: GeoDataFrame with electoral votes and defectors columns with Alaska and Hawaii transformed.
    """

    # Load shapefile safely from package
    with pkg_resources.as_file(pkg_resources.files(state_shapefile) / "cb_2018_us_state_500k.shp") as shp_file:
        gdf = gpd.read_file(shp_file)

    # scale Alaska and Hawaii
    gdf = scale_geometry_for_state(gdf, 'AK', ALASKA_SCALE_FACTOR_X)
    gdf = scale_geometry_for_state(gdf, 'HI', HAWAII_SCALE_FACTOR_X)

    # Load electoral votes CSV safely
    with pkg_resources.as_file(pkg_resources.files(state_shapefile) / "electoral_votes.csv") as csv_file:
        ev_df = pd.read_csv(csv_file)

    # create a new column for the electoral college votes
    col_name = f"elec_votes_{year}"
    if col_name not in ev_df.columns:
        raise ValueError(f"No electoral vote data available for year {year}")

    # add the new column to the geoDataFrame
    gdf = gdf.merge(ev_df[['STUSPS', col_name]], on='STUSPS', how='left')
    gdf.rename(columns={col_name: f"elec_votes_{year}"}, inplace=True)

    # add two new columns for defecting voters
    gdf['defectors'] = 0
    gdf['defector_party'] = None

    return gdf
