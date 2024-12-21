---
layout: default
title: Quickstart
nav_order: 3
---

# Quickstart Guide

Welcome to the quickstart guide for PoliSciPy! This page will help you quickly get started with visualizing U.S. electoral data using PoliSciPy. You’ll learn how to create your first electoral college map in just a few simple steps.

---

## Step 1: Install PoliSciPy

First, you need to install PoliSciPy on your system. You can do this using either pip or conda (or directly from Git if you prefer the latest version). For most users, we recommend using pip.

```
pip install poliscipy
```
Alternatively, you can install it using conda:
```
conda install -c conda-forge poliscipy
```
Or, if you want the most up-to-date version, you can clone the GitHub repository and install it directly:
```
git clone https://github.com/username/poliscipy.git
cd poliscipy
pip install .
```

For more information on how to install PoliSciPy see the Installation page.

---

## Step 2: Import PoliSciPy and Load Data

Once you have installed PoliSciPy, you can start by importing the package and loading the electoral college data. PoliSciPy uses GeoPandas to work with geospatial data, so make sure you have GeoPandas installed as well. If you haven’t installed it, run:

```
pip install geopandas
```

Now, you can import the necessary modules and load the electoral college data into a GeoDataFrame:
```python
# import the poliscipy package
from poliscipy import plot_electoral_map

# Load U.S. electoral college geospatial data (from a predefined dataset or a file)
gdf = poliscipy.load_shapefile()
```

If you don’t have the electoral college shapefile, PoliSciPy provides a utility function to load the dataset for you.

---

## Step 3: Prepare Data for Plotting

Next, you’ll want to load or define the data you want to visualize on the map. This could be voting results, party affiliations, or any other relevant data for each state.

For example, let's define the winning party for each state in the 2024 U.S. election:

```python
winning_party = {
    'AL': 'Republican', 'AK': 'Republican', 'AZ': 'Republican', 'AR': 'Republican',
    # Add data for all states here...
}

# Merge the data with the GeoDataFrame
gdf['winning_party'] = gdf['STUSPS'].map(winning_party).fillna('No Data')
```

In this example, the `winning_party` dictionary maps state codes (like 'AL' for Alabama) to the party that won the election in that state.

For additional information on how to merge data with the GeoDataFrame please see the data and shapefiles section.

---

## Step 4: Plot the Electoral College Map

Now that the data is prepared, it’s time to plot the electoral college map. You can use the `plot_electoral_map()` function to generate a custom map with the data you’ve provided.

```python
plot_electoral_map(gdf, column='winning_party', year='2024', title='2024 U.S. Electoral College Map')
```

This will generate a map that visualizes the election results by party affiliation for each state. The column parameter indicates the column to plot (in this case, `winning_party`), and the year and title parameters are optional, used to annotate the map with the relevant election year and title.

---

## Step 5: Customize the Plot (Optional)

PoliSciPy allows for customization of the map’s appearance. You can modify aspects such as figure size, title, label colors, and borders. Here’s an example of customizing the plot further:

```python
plot_electoral_map(
    gdf,
    column='winning_party',
    year='2024',
    title='2024 U.S. Electoral College Map',
    figsize=(10, 6),
    edgecolor='black',
    labelcolor='white'
)
```

This example customizes the figure size, edge color, and label color to create a more personalized look.

---

## Step 6: Explore More Features

PoliSciPy offers several other features for working with electoral data. You can visualize demographic trends, explore voting results over time, and more. Check out the full documentation for detailed examples, advanced usage, and more customization options.

---

## Example Output

Here’s an example of what the map might look like after running the above commands:

---

## Next Steps

You’ve now created your first electoral college map with PoliSciPy! If you’d like to dive deeper into the library, here are some next steps:

- Explore additional plotting functions for visualizing demographic trends and voting results.
- Learn how to customize your maps further with advanced styling options.
- Check out the API documentation for a complete reference of available functions and classes.

