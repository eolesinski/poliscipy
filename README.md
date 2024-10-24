<div align="center">
  <img width="500" alt="Screenshot 2024-10-23 at 12 04 41 PM" src="https://github.com/user-attachments/assets/05a1a9de-c295-4588-8325-eafb3889415a">
</div>

# PoliSciPy

**PoliSciPy** is an open-source Python library designed for political data analysis and visualization, particularly for U.S. elections. It offers simple, flexible, and high-quality methods to visualize the electoral college, voting results, and demographic trends using libraries such as **GeoPandas** and **Matplotlib**.

## Key Features

- **Visualize Electoral Maps:** Create customizable U.S. electoral college maps, including state borders, electoral votes, and party affiliations.
- **Customize Plots:** Adjust figure size, title, edge color, label colors, and other visual elements for tailored plots.
- **Supports GeoPandas**: Seamlessly integrates with **GeoPandas** for handling geospatial data plotting and analysis.

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
from poliscipy import plot_electoral_map

# Load in GeoDataFrame containing U.S. electoral college geospatial data
gdf = load_electoral_gdf()

# load in the data to plot (either as a dictionary, pandas series, etc.)
winning_party = {
    'AL': 'Republican','AK': 'Republican','AZ': 'Republican','AR': 'Republican', ...
}

# merge your data with the gdf and fill any missing data with 'No Data'
gdf['winning_party'] = gdf['STUSPS'].map(winning_party).fillna('No Data')

# Plot the electoral college map for the year 2024
plot_electoral_map(gdf, column='winning_party', year='2024', title='2024 U.S. Electoral College Map')

```

<div align="center">
    <img src="https://github.com/user-attachments/assets/f096e339-b4f2-4890-82e7-6f923d48a1bd" alt="Electoral College Map" width="974">
    <div style="text-align: center;"><em>Example: Figure with results from the 2024 U.S. election.</em></div>
</div>

## Documentation

Complete documentation for PoliSciPy can be found here.

## Contributing

PoliSciPy welcomes contributions! Please see the CONTRIBUTING.md for guidelines on how to get involved.

## Citation

If you find PoliSciPy useful in your research, academic projects, or software, please cite it using the pre-made BibTeX entry in the CITATION.md file located in the root directory of this repository.

