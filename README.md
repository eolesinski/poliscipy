# PoliSciPy

**PoliSciPy** is an open-source Python library designed for political data analysis and visualization, particularly for U.S. elections. It offers simple, flexible, and high-quality methods to visualize the electoral college, voting results, and demographic trends using libraries such as **GeoPandas** and **Matplotlib**.

## Key Features

- **Visualize Electoral Maps**: Easily create visualizations of the U.S. electoral college, including state borders, electoral votes, and party affiliations.
- **Customizable Plots**: Adjust figure size, title, edge color, label colors, and more to tailor each plot to your needs.
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

## Contributing

## Quickstart and Example

Creating electoral college maps using PoliSciPy can be done in only three simple steps:

1. Load in the geodataframe that contains all of the electoral college geospatial data
2. Load in the specific data that you would like to plot and merge it with the geodataframe
3. Call the `plot_electoral_map()` function and pass in your geodataframe and target column to plot

That's it!

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

<img width="974" alt="Screenshot 2024-10-19 at 1 07 37 AM" src="https://github.com/user-attachments/assets/f096e339-b4f2-4890-82e7-6f923d48a1bd">

## Documentation

The documentation for PoliSciPy can be found here.

## Citation

If you find PoliSciPy useful in your research, academic projects, or software, please cite it using the premade bibtex citation in the CITATION.md file.

