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
    labelcolor: str = 'white', fontsize: float = 9, legend: bool = False, year: str = '2024', 
    vote_bar: bool = False, party_colors: dict = None, legend_order: list = None, **kwargs
) -> None
```

### Parameters

**gdf *(GeoDataFrame)*:**

A GeoPandas GeoDataFrame containing the geographic and electoral data.
Required columns include:
- `centroid_x` and `centroid_y`: Coordinates for state labels.
- `STUSPS`: State postal codes.
- `elec_votes_{year}`: Electoral votes for each state.
- `defectors` and `defector_party` (optional): For defecting voters, used when defector boxes are plotted.

**column *(str)*:**
The target column in `gdf` that determines the fill color of states, typically representing political party affiliation.

**title *(str, optional)*:**
The title of the plot. Defaults to `"Electoral College Map"`.

**figsize *(tuple, optional)*:**
The figure size in inches (width, height). Defaults to `(20, 10)`.

**edgecolor *(str, optional)*:**
The color of state boundary lines. Defaults to `'white'`.

**linewidth *(float, optional)*:**
The width of state boundary lines. Defaults to `0.5`.

**labelcolor *(str, optional)*:**
The color of the text for state labels. Defaults to 'white'.

**fontsize *(float, optional)*:**
Font size for state labels. Defaults to `9`.

**legend *(bool, optional)*:**
Whether to display a legend mapping political parties to colors. Defaults to `False`.

**year *(str, optional)*:**
The election year to plot. Must be 1789 or later and a valid election year (every 4 years). Defaults to `'2024'`.

**vote_bar *(bool, optional)*:**
Whether to include a horizontal vote bar at the top of the plot summarizing total votes by party. Defaults to `False`.

**party_colors *(dict, optional)*:**
A mapping of party names to colors. If `None`, defaults to `default_party_colors`. Parties in the column but missing from this mapping will raise a `ValueError`.

**legend_order *(list, optional)*:**
Custom ordering of parties in the legend. If `None`, parties appear in the order they are found in the data.

**kwargs:**
Additional keyword arguments passed to the `GeoDataFrame.plot()` method, such as `alpha`.

---

## Returns

None
The function directly renders the electoral college map using Matplotlib.

---

## Raises

ValueError:
Raised if year is not a valid election year (1789 or later, every 4 years).

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