---
layout: default
title: Contributing
nav_order: 8
---

# Contributing to PoliSciPy

Thank you for your interest in contributing to [PoliSciPy](https://github.com/eolesinski/poliscipy)! Your contributions help improve the project for the entire community. Whether you're reporting a bug, proposing a new feature, writing documentation, or improving the codebase, your support is greatly appreciated!

This guide outlines the basic process for contributing effectively.

---
## How to Contribute

There are a variety of ways you can contribute to PoliSciPy. Below are some of the common ways to get involved:

### 1. Report Bugs
If you encounter a bug while using PoliSciPy:
- **Check Existing Issues**: Look through the [GitHub Issues](https://github.com/eolesinski/poliscipy/issues) tab to see if it has already been reported.
- **Submit a New Issue**: If it's not listed, feel free to create a new issue with:
  - A clear and concise title.
  - Steps to reproduce the issue.
  - Expected vs. actual behavior.
  - Relevant screenshots, code snippets, or error messages.

---

### 2. Propose Features
Have an idea for a new feature or improvement? Feel free to create a new feature request.
- **Check Existing Requests**: See if your idea has already been suggested.  
- **Open a Feature Request**: Use the [Feature Request Template](https://github.com/username/poliscipy/issues/new?template=feature_request.md) to share:
  - What problem the feature solves.
  - A description of the feature.
  - Any examples or relevant references.

---

### 3. Contribute Code
If you're ready to write code for PoliSciPy, follow these steps:

**Step 1: Fork the Repository**
1. Navigate to [PoliSciPy's GitHub Repository](https://github.com/eolesinski/poliscipy).
2. Click the **Fork** button in the top-right corner to create your own copy of the repository.
3. Clone your fork to your local machine:
   ```bash
   git clone https://github.com/your-username/poliscipy.git
   cd poliscipy
   ```

**Step 2: Set Up Your Environment**
1. Ensure you have **Python 3.x** installed. You can download it here.
2. Install the required dependencies:
```
pip install -r requirements.txt
```
3. Run the tests to ensure that the environment is set up correctly:
```
pytest
```

**Step 3: Make Changes**
1. Create a new branch for your changes:
```
git checkout -b feature-name
```
2. Write clean, well-documented code.
3. Add or update tests for your changes if necessary.

**Step 4: Commit and Push**

1. Commit your changes with a clear and descriptive message:
```
git add .
git commit -m "Description of changes"
```
2. Push the branch to your fork:
```
git push origin feature-name
```

**Step 5: Open a Pull Request**

1. Go to the [Pull Requests](https://github.com/eolesinski/poliscipy/pulls) tab in the main repository.
2. Click New Pull Request and follow the template.
- **Title:** A clear description of the changes you made.
- **Description:** Explain what problem your changes solve, how you approached the solution, and any additional context or screenshots.

---

### 4. Write or Improve Documentation
Documentation is a critical component of any open-source project. You can help out by:
- Fixing typos or clarifying instructions.
- Adding examples for functions and methods.
- Extending tutorials or writing new ones.

*Note:* All the documentation for PoliSciPy is located in the `docs/` directory.

---

## Code of Conduct

If you would like to contribute to PoliSciPy, please make sure that you adhere to the [Code of Conduct](https://github.com/eolesinski/poliscipy?tab=coc-ov-file#). Please be respectful, kind, and considerate in your interactions with others.

---

## Additional Resources

To help you get started with contributing, here are some useful resources:

- [GitHub Guide to Contributing](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests)
- [Python PEP 8 Guidelines](https://peps.python.org/pep-0008/)

