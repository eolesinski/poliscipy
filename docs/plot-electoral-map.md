---
layout: default
title: plot_electoral_map()
parent: API Reference
---

## plot_electoral_map

Plots an electoral college map of the United States using Matplotlib and GeoPandas.

---

### Method Signature

```python
plot_electoral_map(
    gdf: gpd.GeoDataFrame, column: str, title: str = "Electoral College Map", 
    figsize: tuple = (20, 10), edgecolor: str = 'white', linewidth: float = 0.5, 
    labelcolor: str = 'white', legend: bool = False, year: str = '2024', 
    vote_bar: bool = False, **kwargs
) -> None
```

### Parameters

**gdf *(GeoDataFrame)*:**

A GeoPandas GeoDataFrame containing the geographic and electoral data.
Required columns include:
- `centroid_x` and `centroid_y`: Coordinates for state labels.
- `STUSPS`: State postal codes.
- `elec_votes`: Electoral votes for each state.

**column *(str)*:**
The target column in gdf that determines the fill color of states, typically representing political party data.

**title *(str, optional)*:**
The title of the plot. Defaults to "Electoral College Map".

**figsize *(tuple, optional)*:**
The size of the plot. Defaults to (20, 10).

**edgecolor *(str, optional)*:**
The color of the state boundary lines. Defaults to 'white'.

**linewidth *(float, optional)*:**
The width of the state boundary lines. Defaults to 0.5.

**labelcolor *(str, optional)*:**
The color of the text for state labels. Defaults to 'white'.

**legend *(bool, optional)*:**
Whether to display a legend mapping political parties to colors. Defaults to False.

**year *(str, optional)*:**
The election year for the map. Must be 1992 or later and a valid election year (e.g., divisible by 4). Defaults to '2024'.

**vote_bar *(bool, optional)*:**
Whether to include a vote bar at the top of the plot. Defaults to False.

**kwargs:**
Additional keyword arguments to customize the GeoPandas plot method.

---

## Returns

None
The function directly renders the electoral college map using Matplotlib.

---

## Raises

ValueError:
Raised if year is not a valid election year (e.g., less than 1992 or not divisible by 4).

---

## Example Usage

```python
# Import required libraries
import poliscipy

from poliscipy.shapefile_utils import load_shapefile
from poliscipy.plot import plot_electoral_map

# Load the GeoDataFrame
gdf = load_shapefile()

# Add election data to the GeoDataFrame
gdf['winning_party'] = gdf['STUSPS'].map({
    'CA': 'Democrat', 
    'TX': 'Republican',
    # Add mappings for other states
}).fillna('No Data')

# Plot the electoral map
plot_electoral_map(
    gdf, 
    column='winning_party', 
    legend=True, 
    vote_bar=True
)
```