---
layout: default
title: Changelog
nav_order: 9
---

# Changelog

Track changes and updates to the project. This page lists improvements, bug fixes, and new features by version.

---

## [1.1.0] - 2024-07-20
### Added
- New `plot_electoral_map` feature to display state-specific electoral votes.
- `vote_bar` parameter to show party distribution in a bar chart above the map.

### Changed
- Improved color-mapping logic for better accessibility.
- Updated error messages for invalid year inputs.

### Fixed
- Resolved an issue where labels overlapped for small states.

---

## [1.0.0] - 2024-07-01
### Added
- Initial release with core features:
  - `plot_electoral_map` function for visualizing electoral data.
  - `load_df` utility for importing GeoDataFrames.