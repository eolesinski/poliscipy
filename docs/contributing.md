---
layout: default
title: Contributing
nav_order: 7
---

# **Contributing to PoliSciPy**

Thank you for your interest in contributing to **PoliSciPy**! Your contributions help make this project better for the community. Whether you're reporting a bug, proposing new features, writing documentation, or improving the codebase, we welcome your support.

This guide outlines the process for contributing effectively.

---

## **How to Contribute**

### 1. **Report Bugs**
If you encounter a bug while using PoliSciPy:
- **Check Existing Issues**: Look through [GitHub Issues](https://github.com/username/poliscipy/issues) to see if it's already reported.
- **Submit a New Issue**: If it's not listed, create a new issue with:
  - A clear and concise title.
  - Steps to reproduce the issue.
  - Expected vs. actual behavior.
  - Relevant screenshots, code snippets, or error messages.

---

### 2. **Propose Features**
Have an idea for a new feature or improvement?  
- **Check Existing Requests**: See if your idea has already been suggested.  
- **Open a Feature Request**: Use the [Feature Request Template](https://github.com/username/poliscipy/issues/new?template=feature_request.md) to share:
  - What problem the feature solves.
  - A description of the feature.
  - Any examples or relevant references.

---

### 3. **Contribute Code**
If you're ready to write code for PoliSciPy, follow these steps:

#### **Step 1: Fork the Repository**
1. Navigate to [PoliSciPy's GitHub Repository](https://github.com/username/poliscipy).
2. Click the **Fork** button in the top-right corner.
3. Clone your fork:
   ```bash
   git clone https://github.com/your-username/poliscipy.git
   cd poliscipy
   ```

#### Step 2: Set Up Your Environment
1. Ensure you have Python 3.x installed.
2. Install required dependencies:
```
pip install -r requirements.txt
```
3. Run tests to ensure the environment is set up correctly:
```
pytest
```

#### Step 3: Make Changes
1. Create a new branch for your changes:
```
git checkout -b feature-name
```
2. Write clean, well-documented code.
3. Add or update tests for your changes if necessary.

#### Step 4: Commit and Push

1. Commit your changes with a meaningful message:
```
git add .
git commit -m "Description of changes"
```
2. Push the branch to your fork:
```
git push origin feature-name
```

#### Step 5: Open a Pull Request

1. Go to the Pull Requests tab in the main repository.
2. Click New Pull Request and follow the template.
3. Clearly explain:
- What problem your changes solve.
- The approach you used.
- Any additional context or screenshots.


### 4. Write or Improve Documentation
Documentation is critical for any project. You can:
- Fix typos or clarify instructions.
- Add examples for functions and methods.
- Extend tutorials or write new ones.

All documentation is located in the `docs/`c directory.

