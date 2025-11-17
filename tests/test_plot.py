import pytest
from poliscipy.plot import plot_electoral_map
from poliscipy.colors import default_party_colors
from poliscipy.shapefile_utils import load_shapefile


@pytest.fixture
def loaded_gdf():
    """Fixture for loading the 2024 shapefile once for multiple tests."""
    gdf = load_shapefile("2024")

    # assign a winning party for each state
    winning_party_map = {state: 'Republican' for state in gdf['STUSPS']}
    gdf['winning_party'] = gdf['STUSPS'].map(winning_party_map)

    return gdf


def test_plot_electoral_map_runs(loaded_gdf):
    # just ensure that plotting does not raise an exception
    plot_electoral_map(loaded_gdf, column='winning_party', title="Test Map", legend=True, vote_bar=True)


def test_plot_with_missing_party_color(loaded_gdf):
    loaded_gdf['party'] = 'UnknownParty'
    with pytest.raises(ValueError):
        plot_electoral_map(loaded_gdf, column='party', party_colors=default_party_colors)
