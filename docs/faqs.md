---
layout: default
title: FAQs
nav_order: 7
---

# Frequently Asked Questions (FAQs)

## General Questions

**What is PoliSciPy?**
PoliSciPy is an open-source Python library designed for political data analysis and visualization, with a particular focus on U.S. elections. It provides tools for creating electoral college maps, analyzing voting results, and visualizing demographic trends.

**Who is PoliSciPy for?**
PoliSciPy is for data analysts, political scientists, educators, students, and anyone interested in analyzing or visualizing U.S. electoral data!

**What does PoliSciPy stand for?**
PoliSciPy stands for Political Science Python.

---

## Installation Questions

**What are the system requirements for PoliSciPy?**
Python 3.8 or higher
Libraries such as GeoPandas and Matplotlib (automatically installed with PoliSciPy)
Optional: Git for cloning the latest version from the repository

**How do I install PoliSciPy?**
You can install PoliSciPy using pip or conda:

pip install poliscipy
or

conda install -c conda-forge poliscipy
For detailed installation steps, refer to the Installation Guide.


---

## Usage Questions

**How do I create an electoral college map?**
Refer to the Quickstart Guide for step-by-step instructions, including loading geospatial data, merging it with electoral results, and plotting a map.

**What file formats does PoliSciPy support for data input?**
PoliSciPy primarily works with GeoPandas GeoDataFrames but can handle data from CSVs, dictionaries, or pandas DataFrames as long as they are merged with the GeoDataFrame.

**How do I customize the appearance of maps?**
You can customize map titles, colors, labels, and more by using the parameters in the `plot_electoral_map()` function. Detailed instructions can be found in the API Documentation.