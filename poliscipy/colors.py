# Default mapping of parties to colors
default_party_colors = {
    "Democrat": "#4875b1",
    "Republican": "#b82b2b",
    "No Data": "lightgray",
    "Green": "#519e3e",
    "Independent": "#8d69b8"
}

# different party shades for solid, likely, and leans
party_shades = {
    # --- Republican (Red) ---
    "Solid Republican": "#b82b2b",
    "Likely Republican": "#e25e5e",
    "Lean Republican": "#f49696",

    # --- Democrat (Blue) ---
    "Solid Democrat": "#4875b1",
    "Likely Democrat": "#7ea5d4",
    "Lean Democrat": "#a9c8ed",

    # --- Green ---
    "Solid Green": "#519e3e",
    "Likely Green": "#77b97a",
    "Lean Green": "#a2d3a9",

    # --- Independent (Purple) ---
    "Solid Independent": "#8d69b8",
    "Likely Independent": "#b297d0",
    "Lean Independent": "#d0c2e6",

    # --- Toss-Up ---
    "Toss-Up": "#e6c84f",

    # --- No Data ---
    "No Data": "lightgray"
}

# default order of party shades colors for legend ordering
default_legend_order = [
    # Republicans
    "Solid Republican", "Likely Republican", "Lean Republican",
    # Democrats
    "Solid Democrat", "Likely Democrat", "Lean Democrat",
    # Green
    "Solid Green", "Likely Green", "Lean Green",
    # Independent / Purple
    "Solid Independent", "Likely Independent", "Lean Independent",
    # Toss-Up
    "Toss-Up",
    # No Data
    "No Data"
]
