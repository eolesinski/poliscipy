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

If Jekyll is installed on your computer, you can also build and preview the created site locally. This lets you test changes before committing them, and avoids waiting for GitHub Pages.1 And you will be able to deploy your local build to a different platform than GitHub Pages.

PoliSciPy is great for:

- Creating customized, high-quality electoral college maps of the United States
- Conducting political data analysis and tracking changes in voting history and patterns

Other than that, you’re free to customize sites that you create with this template, however you like. You can easily change the versions of just-the-docs and Jekyll it uses, as well as adding further plugins.

<div align="center">
    <img src="assets/election_2024.png" alt="Electoral College Map" width="974">
    <div style="text-align: center;"><em>Example: Figure with results from the 2024 U.S. election.</em></div>
</div>

## About the Project

PoliSciPy is &copy; 2024-{{ "now" | date: "%Y" }} by [Ethan Olesinski](https://eolesinski.github.io).

### License

PoliSciPy is distributed under an [MIT license](https://github.com/just-the-docs/just-the-docs/tree/main/LICENSE.txt).

### Contributors

<ul class="list-style-none">
{% for contributor in site.github.contributors %}
  <li class="d-inline-block mr-1">
     <a href="{{ contributor.html_url }}"><img src="{{ contributor.avatar_url }}" width="32" height="32" alt="{{ contributor.login }}"></a>
  </li>
{% endfor %}
</ul>

Other than that, you're free to customize sites that you create with this template, however you like. You can easily change the versions of `just-the-docs` and Jekyll it uses, as well as adding further plugins.

### Code of Conduct

Just the Docs is committed to fostering a welcoming community.

[View our Code of Conduct](https://github.com/just-the-docs/just-the-docs/tree/main/CODE_OF_CONDUCT.md) on our GitHub repository.

----

[^1]: [It can take up to 10 minutes for changes to your site to publish after you push the changes to GitHub](https://docs.github.com/en/pages/setting-up-a-github-pages-site-with-jekyll/creating-a-github-pages-site-with-jekyll#creating-your-site).

[Just the Docs]: https://just-the-docs.github.io/just-the-docs/
[GitHub Pages]: https://docs.github.com/en/pages
[README]: https://github.com/just-the-docs/just-the-docs-template/blob/main/README.md
[Jekyll]: https://jekyllrb.com
[GitHub Pages / Actions workflow]: https://github.blog/changelog/2022-07-27-github-pages-custom-github-actions-workflows-beta/
[use this template]: https://github.com/just-the-docs/just-the-docs-template/generate
