---
layout: default
title: load_shapefile()
parent: API Reference
---

## load_shapefile

This function loads a shapefile containing U.S. state geometries, applies scaling transformations to Alaska and Hawaii for proper plotting, merges electoral vote data for a specified year, and initializes columns for defecting voters. The resulting GeoDataFrame is ready for analysis or visualization.

---

### Method Signature

```python
load_shapefile(year: str = "2024") -> gpd.GeoDataFrame
```

### Parameters

**year *(str, optional)*:**

The election year for which to load electoral votes. Must match a column in the `electoral_votes.csv` file. Defaults to `"2024"`.

### Returns

**gdf (GeoDataFrame):**

A GeoDataFrame containing:
- State geometries (with Alaska and Hawaii scaled horizontally).
- Electoral votes for the specified year (`elec_votes_<year>`).
- `defectors` column initialized to 0.
- `defector_party` column initialized to `None`.

### Transformations Applied

- **Alaska:** Horizontally scaled by a factor of 0.64 (X-axis).

- **Hawaii:** Horizontally scaled by a factor of 1.1 (X-axis).

### Example Usage

```python
import poliscipy
from poliscipy.shapefile_utils import load_shapefile

# Load the GeoDataFrame with electoral college data for 2024
gdf = load_shapefile(year="2024")
```

### Notes

- The shapefile must contain a `STUSPS` column for state abbreviations (e.g., 'AK', 'HI').
- Scale factors were chosen to adjust Alaska and Hawaii for map visualization.
- Defector-related columns are added to support plotting of defecting voters in electoral maps.
- Data is safely loaded from the `poliscipy.shapefiles` package resources.