---
layout: default
title: FAQs
nav_order: 7
---

# Frequently Asked Questions (FAQs)

## General Questions

<details>
  <summary>What is PoliSciPy?</summary>
  PoliSciPy is an open-source Python library designed for political data analysis and visualization, with a particular focus on U.S. elections. It provides tools for creating electoral college maps, analyzing voting results, and visualizing voting trends.
</details>

<details>
  <summary>Who is PoliSciPy for?</summary>
  PoliSciPy is for data analysts, political scientists, educators, students, and anyone interested in analyzing or visualizing U.S. electoral data!
</details>

<details>
  <summary>What does PoliSciPy stand for?</summary>
  PoliSciPy is short for "Political Science Python," reflecting its focus on political science analysis and data visualization using Python.
</details>

---

## Installation Questions

<details>
  <summary><b>What are the system requirements for PoliSciPy?</b></summary>
  <ul>
    <li>Python 3.8 or higher</li>
    <li>Libraries such as GeoPandas and Matplotlib (automatically installed with PoliSciPy)</li>
    <li>Optional: Git for cloning the latest version from the repository</li>
  </ul>
</details>

<details>
  <summary><b>How do I install PoliSciPy?</b></summary>
  You can install PoliSciPy using pip or conda:
  <pre><code>pip install poliscipy</code></pre>
  or
  <pre><code>conda install -c conda-forge poliscipy</code></pre>
  For detailed installation steps, refer to the <a href="https://eolesinski.github.io/poliscipy/installation.html">Installation Guide</a>.
</details>


---

## Usage Questions

<details>
  <summary><b>How do I create an electoral college map?</b></summary>
  Refer to the <a href="https://eolesinski.github.io/poliscipy/quickstart.html">Quickstart Guide</a> for step-by-step instructions, including loading geospatial data, merging it with electoral results, and plotting a map.
</details>

<details>
  <summary><b>What file formats does PoliSciPy support for data input?</b></summary>
  PoliSciPy primarily works with GeoPandas GeoDataFrames but can handle data from CSVs, dictionaries, or pandas DataFrames as long as they can be merged with the GeoDataFrame.
</details>

<details>
  <summary><b>How do I customize the appearance of maps?</b></summary>
  You can customize map titles, colors, labels, and more by using the parameters in the <code>plot_electoral_map()</code> function. Detailed instructions can be found in the <a href="https://eolesinski.github.io/poliscipy/api-reference.html">API Documentation</a>.
</details>

---

## Troubleshooting

<details>
  <summary><b>I’m getting an error when importing GeoPandas. What should I do?</b></summary>
  Ensure that GeoPandas is installed in your environment:
  <pre><code>pip install geopandas</code></pre>
  If issues persist, consult the <a href="https://geopandas.org/install.html">GeoPandas installation guide</a>.
</details>

<details>
  <summary><b>My map isn’t displaying correctly. What could be wrong?</b></summary>
  <ul>
    <li>Check that your data is correctly merged with the GeoDataFrame.</li>
    <li>Verify that the column name passed to <code>plot_electoral_map()</code> exists in your data.</li>
    <li>Review the example in the <a href="https://eolesinski.github.io/poliscipy/quickstart.html">Quickstart Guide</a> to make sure that you are following the correct steps.</li>
  </ul>
</details>

<details>
  <summary><b>How do I report a bug?</b></summary>
  If you encounter a bug while using PoliSciPy, please submit an issue on the <a href="https://github.com/eolesinski/poliscipy/issues">GitHub Issue Tracker</a> with a clear description and steps to reproduce it.
</details>

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

<style>
  details {
    margin-bottom: 0.75em; /* Adjust this value for smaller or larger spacing */
  }
</style>

<br>