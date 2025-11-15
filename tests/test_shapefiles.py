import pytest
from poliscipy.shapefile_utils import load_shapefile


@pytest.fixture
def loaded_gdf():
    """Return the shapefile GeoDataFrame for 2024 with electoral votes."""
    return load_shapefile("2024")


def test_load_shapefile_columns():

    gdf = load_shapefile("2024")

    # verify that the correct columns are added to the gdf
    assert 'elec_votes_2024' in gdf.columns
    assert 'defectors' in gdf.columns
    assert 'defector_party' in gdf.columns


def test_load_shapefile_row_count(loaded_gdf):

    gdf = loaded_gdf

    # the gdf should include at least 50 states
    assert len(gdf) >= 50


def test_defectors_columns_initialized(loaded_gdf):

    gdf = loaded_gdf

    # all defectors start at 0 and defector_party at None
    assert all(gdf['defectors'] == 0)
    assert all(gdf['defector_party'].isna())


def test_load_shapefile_invalid_year():

    # raise an error for an invalid election year
    with pytest.raises(ValueError):
        load_shapefile("1600")
