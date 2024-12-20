---
layout: default
title: Installation
nav_order: 2
---

# Installation

Welcome to the [PoliSciPy](https://github.com/eolesinski/poliscipy) installation guide! This document will help you set up and run PoliSciPy on your own system.

---

## Prerequisites

Before installing, make sure your environment meets the following requirements:

- **Python 3.8 or higher**: [Download Python](https://www.python.org/downloads/)
- **pip**: Python's package manager ([installation guide](https://pip.pypa.io/en/stable/installation/))
- **Git** (optional): For installing directly from the source ([Git installation guide](https://git-scm.com/))

To verify you have Python and pip installed, run these commands in your terminal:

```bash
python --version
pip --version
```

You should see output similar to:

```
Python 3.8.x
pip 21.x
```

---

## Installation Methods

## Option 1: Using pip (Recommended)
If you have pip installed, you can quickly install PoliSciPy with the following command:

```
pip install poliscipy
```

This command will automatically download and install the latest stable version of PoliSciPy and its dependencies from the Python Package Index (PyPI).


## Option 2: Using conda

Alternatively, if you prefer using the conda package manager, you can install PoliSciPy from the conda-forge channel:

```
conda install -c conda-forge poliscipy
```

This method is particularly helpful if you are working in a conda-based environment, as it will also manage dependencies more efficiently.

## Option 3: Installing Directly from Source (For the Latest Version)

If you would like to get the most up-to-date version of PoliSciPy (which may include the latest bug fixes, features, or improvements), you can install it directly from its GitHub repository. This method is especially useful if you would like to contribute to development or try out new/experimental features.

To install PoliSciPy directly from source, run the following commands:

1. Clone the repository:
```
git clone https://github.com/username/poliscipy.git
```
2. Navigate to the repository folder:
```
cd poliscipy
```
3. Install the package using pip:
```
pip install .
```

This will install PoliSciPy from the latest version in the repository.

---

## Dependencies

PoliSciPy requires the following libraries to work correctly:

- **GeoPandas:** Used for handling geospatial data.
- **Matplotlib:** Used for creating static, animated, and interactive plots.

These dependencies will be automatically installed when you use either of the installation methods above. However, if you wish to install them manually, you can do so by running:

pip install geopandas matplotlib
or
conda install geopandas matplotlib

---

## Still Having Trouble?

If you encounter any issues during installation, don’t worry! Here are some steps you can take:

- **Check the FAQs:** We’ve compiled a list of common issues and solutions in our FAQs page.
- **Open an Issue:** If you can't find a solution in the FAQs, please feel free to open a new issue in the Issues page. Be sure to include any relevant error messages and steps to reproduce the issue.
- **Join the Discussion:** If you're stuck, you can also join our community discussions on GitHub Discussions for help.



