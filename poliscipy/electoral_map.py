import geopandas as gpd

import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import matplotlib.patches as mpatches

from matplotlib.colors import ListedColormap
from shapely.affinity import scale
from mpl_toolkits.axes_grid1.inset_locator import inset_axes
from matplotlib.patches import Rectangle


# create a dictionary to map the colors of the political parties
party_colors = {
    'Democrat': '#4875b1',    
    'Republican': '#b82b2b',  
    'No Data': 'lightgray',
    'Green': '#519e3e',
    'Independent': '#8d69b8'
}


def _add_vote_bar(gdf: gpd.GeoDataFrame, ax, column: str, party_colors: dict) -> None:
    """
    Adds a vote bar containing the total votes for a party at the top of the plot.
    Plots a total vote bar at the top of the plot in 'ax'
    type: matplotlib.axes.Axes

    Params:
    - gdf (GeoDataFrame): The GeoDataFrame containing the election data
    - ax (Axes): the Axes object used in the figure
    - column (str): the column that is being plotted
    - party_colors (dict): a dictionary containing the party color mappings
    
    Returns:
    - None
    
    """
    
    # create a dictionary to store the total vote counts for each party
    total_votes = {party: gdf.loc[gdf[column] == party, 'elec_votes'].sum() 
                   for party in party_colors.keys()}
    
    print(total_votes)

    # set constant values
    VOTE_SCALE_FACTOR = 20
    START_POSITION = -113.5
    
    current_left = START_POSITION

    # List of parties to plot, ensuring "Republican" is first and "No Data" is second if present
    parties_to_plot = []

    if "Republican" in party_colors.keys():
        parties_to_plot.append("Republican")

    if "No Data" in party_colors.keys():
        parties_to_plot.append("No Data")

    # Append other parties, excluding "Republican" and "No Data"
    for party in party_colors.keys():
        if party not in parties_to_plot:
            parties_to_plot.append(party)

    # Plot each party's votes
    for party in parties_to_plot:
        color = party_colors[party]
        width = total_votes.get(party, 0) / VOTE_SCALE_FACTOR  # Use .get() to handle missing parties
        ax.barh(y=52, width=width, color=color, align='center', height=1.2, left=current_left)

        # Annotate the bar with the total votes
        #ax.annotate(f"{int(total_votes.get(party, 0))}", 
                     #xy=(current_left + (width / 40), 51.65),
                     #xytext=(0, 0), textcoords='offset points', 
                     #ha='center', va='bottom', color='white', fontsize=10)
    
        # Update the current left position for the next bar
        current_left += width


def plot_electoral_map(gdf: gpd.GeoDataFrame, column: str, title: str = "Electoral College Map", 
                       figsize: tuple = (20, 10), edgecolor: str = 'white', linewidth: float = .5,
                       labelcolor: str = 'white', legend=False, year='2024', vote_bar = False, 
                       **kwargs) -> None:
    """
    Plots an electoral college map of the United States using Matplotlib and GeoPandas.
    
    Parameters:
    - gdf: GeoDataFrame containing the electoral college data
    - column: The target column to plot
    - title (str): Title of the plot
    - figsize (tuple): Size of the figure (default: (20, 10))
    - edgecolor (str): Edgecolor for the state boundary lines (default: 'white')
    - linewidth (float): Width of the state boundary lines (default: 0.5)
    - labelcolor (str): Color of the state labels (default: 'white')
    - legend (bool): Whether to display a legend or not (default: True)
    
    Returns:
    - None
    
    """
    
    fig1, ax1 = plt.subplots(figsize=figsize)

    gdf.plot(ax=ax1, edgecolor=edgecolor, linewidth=linewidth, color=gdf[column].map(party_colors), **kwargs)

    # plot the state labels at each of the state's respective centroids
    for x_centroid, y_centroid, postal_label, elec_votes in zip(gdf['centroid_x'], gdf['centroid_y'], 
                                                            gdf['STUSPS'], gdf['elec_votes']):
    
        ax1.annotate(f"{postal_label}\n{elec_votes}", (x_centroid, y_centroid), ha='center', va='center',
                     textcoords="data", color=labelcolor, fontname='Arial', fontsize=9)
        
        
    if legend:
        # Get unique values in the specified column of the GeoDataFrame
        unique_parties = gdf[column].unique()
    
        # Create handles for only the parties present in the data
        handles = [mpatches.Patch(color=party_colors[party], label=party) 
                   for party in unique_parties if party in party_colors]

        # Add the legend to the plot
        ax1.legend(handles=handles, bbox_to_anchor=(.975, .22))
        
    if vote_bar:
        
        # add a vote bar to the top of the plot
        _add_vote_bar(gdf, ax1, column, party_colors)
        
        # add vertical line markers for winning condition
        plt.plot([-100, -100], [52.66, 52.73], '-', color='black')
        plt.plot([-100, -100], [51.30, 51.37], '-', color='black') 
        
    # check to make sure that the input year is a valid election year
    if int(year) < 1992 or (int(year) - 1996) % 4 != 0:
    
        raise ValueError("Year must be 1992 or later and a valid election year")

      
    ax1.axis('off')
    ax1.set_title(title, fontsize=16, fontname='Arial')
    
    plt.show();
