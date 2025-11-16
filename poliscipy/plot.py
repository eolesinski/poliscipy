import geopandas as gpd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import Rectangle
from poliscipy.colors import default_party_colors


def _add_defector_box(ax, x_centroid, y_centroid, defectors, defector_party, party_colors, label_color, fontsize):
    """
    Adds a colored box to a Matplotlib plot representing defectors for a specific state.

    Parameters:
        ax (matplotlib.axes.Axes): The axes to which the box will be added.
        x_centroid (float): The x-coordinate of the state's centroid.
        y_centroid (float): The y-coordinate of the state's centroid.
        defectors (int): The number of defectors in the state.
        defector_party (str): The party affiliation of the defectors.
        party_colors (dict): A mapping of party names to colors.
        label_color (str): Color of the text label inside the box.
        fontsize (int or float): Font size of the text label.

    Returns:
        None

    Notes:
        - If `defector_party` is not found in `party_colors`, a default color `#444444` is used.
    """

    face_color = party_colors.get(defector_party, '#444444')

    # Define box properties
    box_width = 0.7
    box_height = 0.6
    box_color = face_color

    # Calculate the position for the box
    box_x = x_centroid + 0.84 - box_width / 2
    box_y = y_centroid - 0.555

    # Add the rectangle (box) to the plot
    rect = Rectangle((box_x, box_y), box_width, box_height, linewidth=0, edgecolor=None, facecolor=box_color)
    ax.add_patch(rect)

    # Add the text label for the number of defectors
    ax.annotate(f"\n{defectors}", (x_centroid + 0.8, y_centroid), ha='center', va='center', textcoords="data", 
        color=label_color, fontname='Arial', fontsize=fontsize)


def _add_vote_bar(gdf: gpd.GeoDataFrame, ax: plt.Axes, column: str, party_colors: dict, year: str,
                  vote_scale_factor: int = 20, initial_bar_position: float = -113.5) -> None:
    """
    Adds a horizontal vote bar to the plot representing the total votes for each party,
    accounting for defecting voters.

    The vote bar is placed near the top of the plot and shows each party's total votes
    scaled by `vote_scale_factor`. Defectors are subtracted from their original party
    and added to the party they defected to.

    Parameters:
        gdf (GeoDataFrame): The GeoDataFrame containing election data.
        ax (matplotlib.axes.Axes): The axes to which the vote bars will be added.
        column (str): The column in `gdf` indicating the original party affiliation.
        party_colors (dict): Mapping of party names to colors for the bars.
        year (str): The election year used to access vote counts (e.g., "2024").
        vote_scale_factor (int, optional): Factor to scale total votes for plotting (default: 20).
        initial_bar_position (float, optional): Starting x-axis position for the first bar (default: -113.5).

    Returns:
        None

    Notes:
        - Parties with no data should be included in `party_colors` as "No Data" if needed.
        - Parties are plotted in descending order of votes, with some exceptions for
          visualization (e.g., second-largest party moved to the end).
        - Only parties with votes greater than 20 are annotated with vote counts.
    """

    # Create a dictionary to store the total vote counts for each party
    total_votes = {party: 0 for party in party_colors.keys()}

    for _, row in gdf.iterrows():
        original_party = row[column]
        elec_votes = row[f"elec_votes_{year}"]
        defectors = row["defectors"]
        defector_party = row["defector_party"]

        # Subtract defectors from the original party
        if original_party in party_colors:
            total_votes[original_party] += max(elec_votes - defectors, 0)

        # Add defectors to the defector party if it exists in party_colors
        if defector_party in party_colors:
            total_votes[defector_party] += defectors

    current_left = initial_bar_position

    # Sort parties by total votes, excluding "No Data"
    sorted_parties = sorted(
        ((party, votes) for party, votes in total_votes.items() if party != "No Data"),
        key=lambda x: x[1],
        reverse=True
    )

    # Identify the second-largest party
    second_largest_party = sorted_parties[1][0] if len(sorted_parties) > 1 else None

    parties_to_plot = ["Republican"] if "Republican" in party_colors else []

    # Append other parties in the sorted order, excluding "Republican" and handling second-largest
    for party, _ in sorted_parties:
        if party not in parties_to_plot:
            parties_to_plot.append(party)

    # Append "No Data" at the end if it exists
    if "No Data" in party_colors:
        parties_to_plot.append("No Data")

    # Move the second-largest party to the end if it is not "No Data"
    if second_largest_party and second_largest_party != "No Data":
        parties_to_plot.remove(second_largest_party)
        parties_to_plot.append(second_largest_party)

    # Plot each party's votes
    for party in parties_to_plot:

        color = party_colors[party]
        width = total_votes.get(party, 0) / vote_scale_factor  # Use .get() to handle missing parties
        ax.barh(y=52, width=width, color=color, align='center', height=1.2, left=current_left)

        center_position = current_left + width / 2
        vote_count = total_votes.get(party, 0)

        if vote_count > 20:
            # Annotate the bar with the total votes, centered within the bar
            ax.annotate(f"{int(vote_count)}",
                        xy=(center_position, 51.9),
                        ha='center', va='center', color='white', fontsize=10)

        # Update the current left position for the next bar
        current_left += width


def plot_electoral_map(gdf: gpd.GeoDataFrame, column: str, title: str = "Electoral College Map", 
                       figsize: tuple = (20, 10), edgecolor: str = 'white', linewidth: float = .5,
                       labelcolor: str = 'white', fontsize: float = 9, legend=False, year="2024", vote_bar=False,
                       party_colors=None, legend_order=None, **kwargs) -> None:
    """
    Plots an electoral college map of the United States using GeoPandas and Matplotlib.

    The map colors each state according to the specified party column, adds state labels
    with electoral votes, and optionally includes defecting voters as separate boxes
    and a vote bar summarizing total votes.

    Parameters:
        gdf (GeoDataFrame): GeoDataFrame containing state geometries and electoral data.
        column (str): Name of the column in `gdf` representing party affiliation for coloring.
        title (str, optional): Title of the plot (default: "Electoral College Map").
        figsize (tuple, optional): Figure size in inches (width, height) (default: (20, 10)).
        edgecolor (str, optional): Color of state boundary lines (default: 'white').
        linewidth (float, optional): Width of state boundary lines (default: 0.5).
        labelcolor (str, optional): Color of state labels (default: 'white').
        fontsize (float, optional): Font size of state labels (default: 9).
        legend (bool, optional): Whether to display a legend (default: False).
        year (str, optional): Election year to plot. Must be 1789 or later and a valid election year (every 4 years) (default: "2024").
        vote_bar (bool, optional): Whether to display a vote bar summarizing total votes at the top of the plot (default: False).
        party_colors (dict, optional): Mapping of party names to colors. Defaults to `default_party_colors` if not provided.
        legend_order (list, optional): Custom order of parties in the legend (default: order found in data).
        **kwargs: Additional keyword arguments passed to `GeoDataFrame.plot()`.

    Raises:
        ValueError: If any value in `column` is missing from `party_colors`.
        ValueError: If `year` is not a valid election year (1789 or later, every 4 years).

    Returns:
        None

    Notes:
        - State labels show the postal abbreviation and electoral votes, adjusted for defectors.
        - Defecting voters are represented with additional boxes using `_add_defector_box`.
        - The vote bar, if enabled, shows total votes per party scaled by `_add_vote_bar`.
        - Parties in `party_colors` not present in the data are ignored for plotting.
    """
    
    # allow for passing in custom color maps
    if party_colors is None:
        party_colors = default_party_colors 
    
    # Check to make sure that all the values in the plotting column have a matching color
    missing_colors = [party for party in gdf[column].unique() if party not in party_colors]
    
    if missing_colors:
        raise ValueError(
            f"The following party(ies) found in data, but not "
            f"defined in colormap: {', '.join(missing_colors)}"
        )
                         
    # check to make sure that the input year is a valid election year
    if int(year) < 1789 or (int(year) > 1789 and (int(year) - 1792) % 4 != 0):
        raise ValueError("Year must be 1789 or later and a valid election year")
    
    fig1, ax1 = plt.subplots(figsize=figsize)

    gdf.plot(ax=ax1, edgecolor=edgecolor, linewidth=linewidth, 
             color=gdf[column].map(party_colors), **kwargs)

    # plot the state labels at each of the state's respective centroids
    for x_centroid, y_centroid, postal_label, elec_votes, defectors, defector_party in zip(gdf['centroid_x'],
            gdf['centroid_y'], gdf['STUSPS'], gdf[f"elec_votes_{year}"], gdf['defectors'], gdf['defector_party']):
            
        # check to see if a state was part of the union or not yet
        if elec_votes != -1:

            display_votes = elec_votes - defectors if defectors > 0 else elec_votes
            
            ax1.annotate(f"{postal_label}\n{display_votes}", (x_centroid, y_centroid), ha='center', va='center',
                     textcoords="data", color=labelcolor, fontname='Arial', fontsize=fontsize)
            
            # add additional box for defecting voters
            if defectors > 0:
                _add_defector_box(ax1, x_centroid, y_centroid, defectors, defector_party, party_colors,
                                  labelcolor, fontsize)

    if legend:

        # Use the provided legend_order if given, otherwise default to pandas ordering
        if legend_order is None:
            legend_order = gdf[column].unique()

        handles = [
            mpatches.Patch(color=party_colors[party], label=party)
            for party in legend_order if party in gdf[column].unique()
        ]

        ax1.legend(handles=handles, bbox_to_anchor=(.975, .22))
        
    if vote_bar:
        
        # add a vote bar to the top of the plot
        _add_vote_bar(gdf, ax1, column, party_colors, year)
        
        # add vertical line markers for winning condition
        plt.plot([-100, -100], [52.66, 52.73], '-', color='black')
        plt.plot([-100, -100], [51.30, 51.37], '-', color='black') 

    ax1.axis('off')
    ax1.set_title(title, fontsize=16, fontname='Arial')
    
    plt.show()
