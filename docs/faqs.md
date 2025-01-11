---
layout: default
title: FAQs
nav_order: 7
---

# Frequently Asked Questions (FAQs)

## General Questions

**What is PoliSciPy?**
PoliSciPy is an open-source Python library designed for political data analysis and visualization, with a particular focus on U.S. elections. It provides tools for creating electoral college maps, analyzing voting results, and visualizing voting trends.

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

`pip install poliscipy`
or

`conda install -c conda-forge poliscipy`
For detailed installation steps, refer to the Installation Guide.


---

## Usage Questions

**How do I create an electoral college map?**
Refer to the [Quickstart Guide](https://eolesinski.github.io/poliscipy/quickstart.html) for step-by-step instructions, including loading geospatial data, merging it with electoral results, and plotting a map.

**What file formats does PoliSciPy support for data input?**
PoliSciPy primarily works with GeoPandas GeoDataFrames but can handle data from CSVs, dictionaries, or pandas DataFrames as long as they can be merged with the GeoDataFrame.

**How do I customize the appearance of maps?**
You can customize map titles, colors, labels, and more by using the parameters in the `plot_electoral_map()` function. Detailed instructions can be found in the [API Documentation](https://eolesinski.github.io/poliscipy/api-reference.html).

---

## Troubleshooting

**I’m getting an error when importing GeoPandas. What should I do?**
Ensure that GeoPandas is installed in your environment:

```
pip install geopandas
```

If issues persist, consult the GeoPandas installation guide.

**My map isn’t displaying correctly. What could be wrong?**
- Check that your data is correctly merged with the GeoDataFrame.
- Verify that the column name passed to `plot_electoral_map()` exists in your data.
- Review the example in the [Quickstart Guide](https://eolesinski.github.io/poliscipy/quickstart.html) to make sure that you are following the correct steps.

**How do I report a bug?**
If you encounter a bug while using PoliSciPy, please submit an issue on the [GitHub Issue Tracker](https://github.com/eolesinski/poliscipy/issues) with a clear description and steps to reproduce it.

---

## Contributing Questions

<details>
  <summary><b>How can I contribute to PoliSciPy?</b></summary>
  Contributions are always welcome! See the <a href="https://eolesinski.github.io/poliscipy/contributing.html">Contributing Guide</a> for detailed instructions.
</details>

<details>
  <summary><b>Do I need to be an expert to contribute?</b></summary>
  Not at all! There are a variety of ways that you can contribute, including reporting issues, suggesting features, improving documentation, or writing code. Every bit helps!
</details>

---

## Miscellaneous

<details>
  <summary><b>Can I use PoliSciPy for non-U.S. elections?</b></summary>
  While PoliSciPy is optimized for U.S. electoral data, in theory, it can be adapted for other datasets/shapefiles with similar structure (as long as you use the same set of column names). Feel free to experiment with this and share your results!
</details>

<details>
  <summary><b>Where can I find examples and tutorials?</b></summary>
  Visit the <a href="https://eolesinski.github.io/poliscipy/examples.html">Examples section</a> of the documentation site for detailed tutorials and code snippets.
</details>

<details>
  <summary><b>How do I cite PoliSciPy in my research?</b></summary>
  Please refer to the <a href="https://eolesinski.github.io/poliscipy/citation.html">Citation Guide</a> for information on how to cite PoliSciPy in your work.
</details>

<br>