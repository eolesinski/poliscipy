---
layout: default
title: load_shapefile()
parent: API Reference
---

## load_shapefile

This method loads a shapefile containing electoral college data, applies specific scaling transformations to Alaska and Hawaii for proper plotting, and returns the data as a GeoDataFrame, allowing further analysis or visualization.

---

### Method Signature

```python
def load_df(year: int) -> gpd.GeoDataFrame:
```

### Parameters

**year *(int, optional)*:**

The year for which to load the electoral college data. This parameter is currently unused in the method but can be extended to filter or manipulate data for specific years. If a year is not provided the default is set to the year 2024.

### Returns

gdf (gpd.GeoDataFrame):

A GeoDataFrame containing the electoral college data for the specified year. The data includes geographic shapes (polygons) of U.S. states, with special scaling applied to Alaska and Hawaii to account for size distortion in standard maps.

### Transformations Applied

- Alaska: The geometry of Alaska is horizontally scaled by a factor of 0.64 (X-axis), preserving the state’s relative position and size within the map.

- Hawaii: The geometry of Hawaii is horizontally scaled by a factor of 1.1 (X-axis), adjusting its size for visual improvement.

### Example Usage

```python
from poliscipy import load_shapefile

# Load the GeoDataFrame with electoral college data
gdf = load_df(year=1992)
```

### Notes

- The method assumes the shapefile contains data about U.S. states, with a column STUSPS denoting state abbreviations (e.g., 'AK' for Alaska, 'HI' for Hawaii).

- Scaling factors for Alaska and Hawaii were determined to better represent their geographical sizes in a standard map projection.

### Full list of columns

The shapefile used in PoliSciPy contains several columns that provide geographic and attribute data. Below is a brief overview of the columns and their data types:

- **STATEFP (str):** A two-digit state FIPS code.
- **STATENS (str):** An eight-digit state identifier.
- **AFFGEOID (str):** A unique identifier for geographic features.
- **GEOID (str):** A two-digit geographic identifier.
- **STUSPS (str):** The two-letter state postal abbreviation.
- **NAME (str):** The full name of the state or territory.
- **LSAD (str):** A two-character legal/statistical area description.
- **ALAND (int):** Land area in square meters.
- **AWATER (int):** Water area in square meters.
- **centroid_x (float):** Longitude of the state's centroid.
- **centroid_y (float):** Latitude of the state's centroid.
- **elec_votes (int):** Number of electoral votes for the state.
- **geometry (Polygon):** The shape data representing the state boundary.