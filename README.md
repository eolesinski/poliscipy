# PoliSciPy

[![License: MIT](https://img.shields.io/badge/License-MIT-red.svg)](https://opensource.org/licenses/MIT)
![PyPI Version](https://img.shields.io/pypi/v/<poliscipy>?color=blue)
![Package tests](https://github.com/eolesinski/poliscipy/actions/workflows/tests.yml/badge.svg)

**PoliSciPy** is an open-source Python library designed for political data analysis and visualization, particularly for U.S. elections. It offers simple, flexible, and high-quality methods to visualize the electoral college, voting results, and demographic trends using libraries such as **GeoPandas** and **Matplotlib**.

## Key Features

- **Visualize Electoral Maps:** Create customizable U.S. electoral college maps, including state borders, electoral votes, and party affiliations.
- **Customize Plots:** Adjust figure size, title, edge color, label colors, and other visual elements for tailored plots.
- **Supports GeoPandas**: Seamlessly integrates with **GeoPandas** for handling geospatial data plotting and analysis.

<div align="center">
    <img src="docs/assets/election_2024.png" alt="Electoral College Map" width="974">
    <div style="text-align: center;"><em>Example: Figure with results from the 2024 U.S. election.</em></div>
</div>

## Installation

PoliSciPy requires Python 3.x and can be installed using `pip`:

```
pip install poliscipy
```

PoliSciPy is also availalbe on conda via:

```
conda install -c conda-forge poliscipy
```

*Dependencies: Note that PoliSciPy requires GeoPandas and matplotlib*

## Quickstart and Example

Creating electoral college maps using PoliSciPy can be done in only three simple steps:

1. Load the geodataframe that contains electoral college geospatial data
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

Complete documentation for PoliSciPy can be found [here](https://eolesinski.github.io/poliscipy/).

## Contributing

PoliSciPy welcomes contributions! Please see the CONTRIBUTING.md for guidelines on how to get involved.

## Citation

If you find PoliSciPy useful in your research, academic projects, or software, please cite it using the pre-made BibTeX entry in the CITATION.md file located in the root directory of this repository.

