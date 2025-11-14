---
layout: default
title: Shapefiles
parent: Data and Shapefiles
nav_order: 1
---

# Shapefiles

This page provides an in-depth guide to using shapefiles in PoliSciPy to create election maps. You’ll learn what shapefiles are, how to load them, and how to integrate them with election data for visualization.

---

## Working with Shapefiles in PoliSciPy

Shapefiles are the foundation of electoral college map visualizations in PoliSciPy. They contain the geographic and boundary information necessary to render the polygons representing states, territories, and other regions of the map. This section explains the structure of shapefiles, how to load and process them, and how to integrate election data for subsequent visualization. *First it might be helpful to understand:*

### What is a Shapefile?

A shapefile is a widely used geospatial vector data format for geographic information system (GIS) software. It represents geographic features (e.g., states, counties) and their attributes. A shapefile typically consists of several files with the same name but different extensions, including:

- `.shp`: Contains geometry data (shapes of features).

- `.shx`: An index file to improve access to geometry data.

- `.dbf`: A database file storing attribute data for each feature (e.g., state names, FIPS codes).

**Note on Shapefiles:**

PoliSciPy uses modified shapefiles originally provided by the United States Census Bureau through the [TIGER/Line](https://www.census.gov/geographies/mapping-files/time-series/geo/tiger-line-file.html) dataset. For more information about the original shapefiles and how to access them, please visit the [citation page](https://eolesinski.github.io/poliscipy/citation.html).


### Inspecting the Shapefile

You can inspect the shapefile once you've loaded it using the `load_shapefile()` method. If you type the following:

```
gdf = load_shapefile()
gdf.head(2)
```

You can then inspect the shapefile shown below. A full list of all of the columns included in the shapefile is shown below.

| STATEFP | NAME          | STUSPS | elec_votes_2024 | defectors  | defector_party | centroid_x | centroid_y | geometry       |
|---------|---------------|--------|-----------------|------------|----------------|------------|------------|----------------|
| 28      | Mississippi   | MS     | 6               | 0          | None           | -89.6652   | 32.7509    | MULTIPOLYGON   |
| 37      | North Carolina| NC     | 16              | 0          | None           | -79.3724   | 35.5415    | MULTIPOLYGON   |

### Understanding the Shapefile's Columns

For more information on the columns in the shapefile and their meanings, you can inspect the shapefile’s schema. Each row in the shapefile represents a U.S. state or territory and includes the following columns:

| Column      | Type          | Description |
|------------|--------------|-------------|
| `STATEFP`    | `str:2`        | The two-digit [FIPS code](https://transition.fcc.gov/oet/info/maps/census/fips/fips.txt) assigned to the state. |
| `STATENS`    | `str:8`        | A unique identifier for the state in the [GNIS database](https://www.usgs.gov/tools/geographic-names-information-system-gnis). |
| `AFFGEOID`   | `str:11`       | An 11-character unique geographic identifier. |
| `GEOID`      | `str:2`        | The numeric FIPS code (same as STATEFP). See: [*What are GEOIDs?*](https://www.census.gov/programs-surveys/geography/guidance/geo-identifiers.html) |
| `STUSPS`     | `str:2`        | The two-letter postal abbreviation for the state (e.g., CA, TX). |
| `NAME`       | `str:100`      | The full state name (e.g., "California"). |
| `LSAD`       | `str:2`        | Legal/statistical area description (usually empty or generic for states). |
| `ALAND`      | `int:14`       | Land area of the state in square meters. |
| `AWATER`     | `int:14`       | Water area of the state in square meters. |
| `centroid_x` | `float:19.11`  | Longitude coordinate of the state’s centroid. |
| `centroid_y` | `float:19.11`  | Latitude coordinate of the state’s centroid. |
| `elec_votes` | `int:5 `       | The number of electoral votes assigned to the state. |
| `geometry`   | `Polygon`      | The geographic shape of the state as a polygon. |

This table serves as a reference for understanding the attributes in the shapefile and how they can be used when merging data or visualizing maps.

## Next Step: Merging Election Data with the Shapefile

Next, we’ll explore how to merge additional election data with the shapefile for visualization. Head over to the next section on [Merging Data](https://eolesinski.github.io/poliscipy/merging-data.html) to learn more about integrating datasets for analysis and creating visualizations.