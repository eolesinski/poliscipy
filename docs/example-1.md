---
layout: default
title: Current and Future Elections
parent: Examples
nav_order: 1
---

# Visualizing U.S. Elections: Current and Future Elections with PoliSciPy

In this example, we’ll explore how to visualize current and upcoming U.S. elections using PoliSciPy. By leveraging historical shapefiles and election results data, you can plot electoral maps that showcase political landscapes for various election years, including the upcoming 2024 election.

---

## Understanding U.S. Elections

The United States holds presidential elections every four years, where each state participates in the Electoral College system to determine the winner. The political landscape and voting patterns evolve over time, which is why visualizing these elections helps us understand the trends and shifts in political power.

## Step 1: Install PoliSciPy

To get started, you’ll need to install PoliSciPy, a Python package designed for electoral data visualization and analysis. You can install it via pip:

```
pip install poliscipy
```

For more installation details, refer to the PoliSciPy Installation Guide.

## Step 2: Import Necessary Libraries

Once you have PoliSciPy installed, begin by importing it, along with other essential libraries:

```
import poliscipy as ps
import pandas as pd
```

This will allow you to work with the election data and generate maps using the available shapefiles.

## Step 3: Load Historical Shapefiles

PoliSciPy provides shapefiles for various historical election years. For the current and upcoming elections, you can load the shapefile for the most recent election year. For example, for the 2024 presidential election:

```
# Load the shapefile for the 2024 election
gdf = ps.load_shapefile(year=2024)
```

This function loads a GeoDataFrame containing the geometries and attributes of states as they existed in 2024, based on the latest available data.

## Step 4: Prepare Election Data

Next, prepare the election results for the chosen year. For example, for the 2024 U.S. presidential election, create a DataFrame with the results:

```
# Example data for the 2024 election
data = {
    'state': ['California', 'Texas', 'Florida', 'New York', 'Pennsylvania', 'Illinois', 'Ohio', 'Georgia', 'North Carolina', 'Michigan'],
    'winner': ['Democratic', 'Republican', 'Republican', 'Democratic', 'Democratic', 'Democratic', 'Republican', 'Republican', 'Republican', 'Democratic']
}

df = pd.DataFrame(data)
```

This DataFrame includes the states that participated in the 2024 election and the party that won in each state.

## Step 5: Merge Election Data with Shapefile

To visualize the election results, you’ll need to merge your election data with the shapefile’s GeoDataFrame. This ensures that the geographical boundaries of each state are matched with the corresponding election results.

```
# Merge the election data with the GeoDataFrame
gdf = gdf.merge(df, left_on='NAME', right_on='state', how='left')
```

## Step 6: Plot the Electoral Map

Now that you’ve merged the data, you can visualize the electoral results by plotting the map:

```
# Plot the 2024 electoral map
ps.plot_electoral_map(gdf, column='winner', title='2024 U.S. Presidential Election')
```

This function generates a map of the 2024 election results, coloring each state based on the winner. States that did not participate in the election can be marked as "No Votes".