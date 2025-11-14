---
title: Home
layout: home
nav_order: 1
---

# **Welcome to PoliSciPy's Documentation**

PoliSciPy is a Python package for creating customizable electoral college maps of the United States, making it easy to visualize and analyze electoral data.
{: .fs-5 .fw-300 }

[Get started now](https://eolesinski.github.io/poliscipy/quickstart.html){: .btn .btn-blue .fs-4 .mb-4 .mb-md-0 .mr-2 }
[View on GitHub](https://github.com/eolesinski/poliscipy){: .btn .fs-4 .mb-4 .mb-md-0 .mr-2 }

---

With Python installed, you can quickly set up PoliSciPy and start generating electoral maps. This lets you experiment with data, visualize results instantly, and test customizations before sharing or publishing.

PoliSciPy is especially useful for:

- Creating customized, high-quality electoral college maps of the United States
- Conducting political data analysis and tracking changes in voting history and patterns
- Exploring historical election results and visualizing trends

Feel free to customize maps however you like, check out the [Getting Started](https://eolesinski.github.io/poliscipy/quickstart.html) guide above, share your results, and post any questions or issues that you run into on the [GitHub](https://github.com/eolesinski/poliscipy) repository.

<div align="center">
    <img src="assets/election_2024.png" alt="Electoral College Map" width="974">
    <div style="text-align: center;"><em>Example: Figure with results from the 2024 U.S. election.</em></div>
</div>

## About the Project

PoliSciPy is &copy; 2024-{{ "now" | date: "%Y" }} by [Ethan Olesinski](https://eolesinski.github.io).

### License

PoliSciPy is distributed under an [MIT license](https://github.com/just-the-docs/just-the-docs/tree/main/LICENSE.txt).

### Contributors

Thank you to everyone who helps make PoliSciPy better! You can see the full list of contributors below or on [GitHub](https://github.com/eolesinski/poliscipy/graphs/contributors):

<ul class="list-style-none">
{% for contributor in site.github.contributors %}
  <li class="d-inline-block mr-1">
     <a href="{{ contributor.html_url }}"><img src="{{ contributor.avatar_url }}" width="32" height="32" alt="{{ contributor.login }}"></a>
  </li>
{% endfor %}
</ul>

We welcome contributors of all levels whether it’s fixing bugs, adding features, or improving documentation! If you are interested in helping improve PoliSciPy, visit the [Contribution Guide](https://eolesinski.github.io/poliscipy/contributing.html) for more information.

### Code of Conduct

PoliSciPy is committed to fostering a welcoming and inclusive community.  

[View the Code of Conduct](https://github.com/eolesinski/poliscipy/blob/main/CODE_OF_CONDUCT.md) on the GitHub repository.

----

[^1]: [It can take up to 10 minutes for changes to your site to publish after you push the changes to GitHub](https://docs.github.com/en/pages/setting-up-a-github-pages-site-with-jekyll/creating-a-github-pages-site-with-jekyll#creating-your-site).

[Just the Docs]: https://just-the-docs.github.io/just-the-docs/
[GitHub Pages]: https://docs.github.com/en/pages
[README]: https://github.com/just-the-docs/just-the-docs-template/blob/main/README.md
[Jekyll]: https://jekyllrb.com
[GitHub Pages / Actions workflow]: https://github.blog/changelog/2022-07-27-github-pages-custom-github-actions-workflows-beta/
[use this template]: https://github.com/just-the-docs/just-the-docs-template/generate
