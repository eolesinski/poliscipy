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

For more information on how to install PoliSciPy see the [Installation page](https://eolesinski.github.io/poliscipy/installation.html).

---

## Step 2: Import PoliSciPy and Load Data

Once you have installed PoliSciPy, you can start by importing the package and loading the electoral college data. You can do this by running:

```
import poliscipy
```

Now, you can load in the shapefile containing the electoral college data in a GeoDataFrame:
```python
# import the poliscipy load_shapefile and plot_electoral_map methods
from poliscipy.shapefile_utils import load_shapefile
from poliscipy.plot import plot_electoral_map

# Load U.S. electoral college geospatial data
gdf = load_shapefile()
```

**Note:** The default year for election data is 2024, but users can pass in a `year` parameter to `load_shapefile(year="2020")` to get a geoDataFrame with historical election data.

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

For additional information on how to merge data with the GeoDataFrame please see the [data and shapefiles](https://eolesinski.github.io/poliscipy/data-and-shapefiles.html) section.

---

## Step 4: Handling Split States

Some states allocate electoral votes by congressional district rather than winner-takes-all. PoliSciPy provides tools to account for these splits, so you can visualize them accurately.

To account for Maine and Nebraska you can edit the defecting voters column that specifies cases with non-winner-takes-all cases:

```python
# add the number of electors that voted for the other candidate
gdf.loc[38, 'defectors'] = 1 # maine
gdf.loc[10, 'defectors'] = 1 # nebraska

# set the political party for each of the congressional district winners
gdf.loc[38, 'defector_party'] = 'Republican'
gdf.loc[10, 'defector_party'] = 'Democrat'
```

For more information on handling split states and defecting voters check out the [Adding Defectors](https://eolesinski.github.io/poliscipy/merging-data.html) section of the Merging data page.

---

## Step 5: Plot the Electoral College Map

Now that the data is prepared, it’s time to plot the electoral college map. You can use the `plot_electoral_map()` function to generate a custom map with the data you’ve provided.

```python
plot_electoral_map(gdf, column='winning_party', year='2024', title='2024 U.S. Electoral College Map')
```

This will generate a map that visualizes the election results by party affiliation for each state. The column parameter indicates the column to plot (in this case, `winning_party`), and the year and title parameters are optional, used to annotate the map with the relevant election year and title.

---

## Step 6: Customize the Plot (Optional)

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

## Step 7: Explore More Features

PoliSciPy offers several other features for working with electoral data. You can visualize demographic trends, explore voting results over time, and more. Check out the full documentation for detailed examples, advanced usage, and more customization options.

---

## Example Output

Here’s an example of what the map should look like after running the above commands:

<div align="center">
    <img src="assets/election_2024.png" alt="Electoral College Map" width="974">
    <div style="text-align: center;"><em>Example: Figure with results from the 2024 U.S. election.</em></div>
</div>

---

## Next Steps

You’ve now created your first electoral college map with PoliSciPy! If you’d like to dive deeper into the library, here are some next steps:

- Explore additional plotting functions for visualizing demographic trends and voting results.
- Learn how to customize your maps further with advanced styling options.
- Check out the API documentation for a complete reference of available functions and classes.

