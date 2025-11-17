# PoliSciPy

[![License: MIT](https://img.shields.io/badge/License-MIT-red.svg)](https://opensource.org/licenses/MIT)
![PyPI Version](https://img.shields.io/pypi/v/poliscipy?color=blue)
![Conda](https://img.shields.io/conda/v/conda-forge/poliscipy)
![Package tests](https://github.com/poliscipy/poliscipy/actions/workflows/tests.yml/badge.svg)
[![codecov](https://codecov.io/gh/poliscipy/poliscipy/branch/main/graph/badge.svg)](https://codecov.io/gh/poliscipy/poliscipy)

**PoliSciPy** is an open-source Python library that makes it easy to generate electoral maps and explore political data with just a few lines of code. The library is designed for fast experimentation, clear visualizations, and flexible customization, whether you’re analyzing results, presenting findings, or exploring historical trends.

## Key Features

- **Visualize Electoral Maps:** Create U.S. electoral college maps with state labels, electoral votes, and party colors.
- **Customize Plots:** Adjust figure size, title, edge colors, label colors, and other visual elements for customized plots.
- **Flexible Data Handling:** Easily merge your own election results (current, historical, or hypothetical) with the map data for visualization.

<div align="center">
    <img src="https://raw.githubusercontent.com/poliscipy/poliscipy/main/docs/assets/election_2024.png" alt="Electoral College Map" width="974">
    <div style="text-align: center;"><em>Example: Figure with results from the 2024 U.S. election.</em></div>
</div>

## Installation

PoliSciPy requires Python 3.x and can be installed using `pip`:

```
pip install poliscipy
```

PoliSciPy is also available on conda via:

```
conda install -c conda-forge poliscipy
```

*Dependencies: Note that PoliSciPy requires GeoPandas, matplotlib, and Pandas*

## Quickstart and Example

Creating electoral college maps using PoliSciPy can be done in only three simple steps:

1. Load the GeoDataFrame that contains the electoral college geospatial data
2. Load and merge the specific data you'd like to plot with the GeoDataFrame
3. Call the `plot_electoral_map()` function, passing in your GeoDataFrame and the target column for plotting

Below is an example of how to use PoliSciPy to visualize the 2024 U.S. electoral college map shown above.

```
import poliscipy

from poliscipy.shapefile_utils import load_shapefile
from poliscipy.plot import plot_electoral_map

# Load in GeoDataFrame containing U.S. electoral college geospatial data
gdf = load_shapefile()

# Create a dictionary with the data to plot
winning_party = {
    'AL': 'Republican','AK': 'Republican','AZ': 'Republican','AR': 'Republican', ...
}

# Merge your data with the gdf and fill any missing data with 'No Data'
gdf['winning_party'] = gdf['STUSPS'].map(winning_party).fillna('No Data')

# Add the number of electors that voted for the other candidate
gdf.loc[38, 'defectors'] = 1 # maine
gdf.loc[10, 'defectors'] = 1 # nebraska

# Set the political party for each of the congressional district winners
gdf.loc[38, 'defector_party'] = 'Republican'
gdf.loc[10, 'defector_party'] = 'Democrat'

# Plot the electoral college map for the year 2024
plot_electoral_map(gdf, column='winning_party', title='2024 U.S. Electoral College Map')

```

## Documentation

Complete documentation for PoliSciPy can be found [here](https://poliscipy.github.io/poliscipy/).

## Contributing

PoliSciPy welcomes contributions! Please see the [CONTRIBUTING.md](https://github.com/poliscipy/poliscipy/blob/main/CONTRIBUTING.md) for guidelines on how to get involved.

## Citation

If you find PoliSciPy useful in your research, academic projects, or software, please cite it using the [CITATION.cff](https://github.com/poliscipy/poliscipy/blob/main/CITATION.cff) file located in the root directory of this repository.