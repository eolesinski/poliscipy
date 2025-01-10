import geopandas as gpd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from shapely.affinity import scale
from matplotlib.patches import Rectangle

def load_df(path: str) -> gpd.GeoDataFrame:
    """
    Method for loading in a GeoDataFrame for plotting the electoral college.
    
    Params:
    - path: the path to the shapefile 
    
    Returns:
    - gdf: a GeoDataFrame containing the electoral college data for the specified year 
    """
    
    gdf = gpd.read_file(path)
    
    # define the scale factors for Alaska and Hawaii
    ALASKA_SCALE_FACTOR_X = 0.64
    HAWAII_SCALE_FACTOR_X = 1.1
    
    # apply the transformation for Alaska
    alaska = gdf.loc[gdf['STUSPS'] == 'AK']

    # apply an affine transformation to conduct horizontal scaling
    scaled_geometry = alaska['geometry'].apply(lambda geom: scale(geom, xfact=ALASKA_SCALE_FACTOR_X, yfact=1.0))
    
    gdf.loc[gdf['STUSPS'] == 'AK', 'geometry'] = scaled_geometry
    
    # apply the transformation for Hawaii
    hawaii = gdf.loc[gdf['STUSPS'] == 'HI']

    # apply an affine transformation to conduct horizontal scaling
    scaled_geometry_2 = hawaii['geometry'].apply(lambda geom: scale(geom, xfact=HAWAII_SCALE_FACTOR_X, yfact=1.0))
    
    gdf.loc[gdf['STUSPS'] == 'HI', 'geometry'] = scaled_geometry_2
     
    return gdf

# create a dictionary to map the colors of the political parties
default_party_colors = {
    'Democrat': '#4875b1',    
    'Republican': '#b82b2b',  
    'No Data': 'lightgray',
    'Green': '#519e3e',
    'Independent': '#8d69b8'
}

def _add_defector_box(ax, x_centroid, y_centroid, defectors, defector_party, party_colors, labelcolor):
    """
    Adds a colored box to the plot representing defectors for a specific state.

    Parameters:
    - ax: The Matplotlib Axes object where the box will be added.
    - x_centroid: The x-coordinate of the state's centroid.
    - y_centroid: The y-coordinate of the state's centroid.
    - defectors: The number of defectors in the state.
    - defector_party: The party of the defectors.
    - party_colors: A dictionary mapping parties to their corresponding colors.
    - labelcolor: The color for the text label inside the box.

    Returns:
    - None

    Notes:
    - If the defector party is not found or defined in `party_colors`, a default color (`#444444`) will be 
    used to represent an 'Other' category.
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
        color=labelcolor, fontname='Arial', fontsize=9)

def _add_vote_bar(gdf: gpd.GeoDataFrame, ax: plt.Axes, column: str, party_colors: dict, year: str, 
                  vote_scale_factor: int = 20, initial_bar_position: float = -113.5) -> None:
    """
    Adds a vote bar containing the total votes for each party at the top of the plot,
    accounting for defecting voters.

    Parameters:
    - gdf (GeoDataFrame): The GeoDataFrame containing the election data.
    - ax (Axes): The matplotlib Axes object used in the figure.
    - column (str): The column indicating the original party affiliation.
    - party_colors (dict): A dictionary mapping parties to their respective colors.
    - year (str): The election year used to calculate votes (e.g., "2024").
    - vote_scale_factor (int): Factor to scale the total votes for plotting (default: 20).
    - initial_bar_position (float): Starting position for the bars on the x-axis (default: -113.5).
    
    Returns:
    - None
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
                       labelcolor: str = 'white', legend=False, year='2024', vote_bar = False,
                       party_colors=None, **kwargs) -> None:
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
    - year (str, optional): The election year to plot. Must be a valid election year 
      (1789 or later, occurring every 4 years) (default: "2024").
    - party_colors (dict, optional): A dictionary mapping parties to their corresponding colors. 
      If not provided, a default colormap is used.
    - vote_bar (bool): Vote bar, for total votes, displayed at the top of the plot
    
    Raises:
    - ValueError: If any value in the `column` is not defined in `party_colors`.
    - ValueError: If the `year` is not a valid election year.
    
    Returns:
    - None
    """
    
    # allow for passing in custom color maps
    if party_colors is None:
        party_colors = default_party_colors 
    
    # Check to make sure that all of the values in the plotting column have a matching color
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
                     textcoords="data", color=labelcolor, fontname='Arial', fontsize=9)
            
            # add an additional box for defecting voters
            if defectors > 0:
                _add_defector_box(ax1, x_centroid, y_centroid, defectors, defector_party, party_colors, labelcolor)
            
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

    ax1.axis('off')
    ax1.set_title(title, fontsize=16, fontname='Arial')
    
    plt.show()



if __name__ == "__main__":

    gdf = load_df('/Users/ethanolesinski/Desktop/backup_shapefile_2/cb_2018_us_state_500k.shp') 

    winning_party = {
            'AL': 'Republican','AK': 'Republican','AZ': 'Republican','AR': 'Republican','CA': 'Democrat','CO': 'Democrat',
            'CT': 'Democrat', 'DE': 'Democrat', 'FL': 'Republican', 'GA': 'Republican', 'HI': 'Democrat', 
            'ID': 'Republican', 'IL': 'Democrat','IN': 'Republican','IA': 'Republican','KS': 'Republican',
            'KY': 'Republican', 'LA': 'Republican','ME': 'Democrat','MD': 'Democrat','MA': 'Democrat',
            'MI': 'Republican','MN': 'Democrat','MS': 'Republican','MO': 'Republican','MT': 'Republican','NE': 'Republican',
            'NV': 'Republican','NH': 'Democrat','NJ': 'Democrat','NM': 'Democrat','NY': 'Democrat','NC': 'Republican',
            'ND': 'Republican','OH': 'Republican','OK': 'Republican','OR': 'Democrat','PA': 'Republican','RI': 'Democrat',
            'SC': 'Republican','SD': 'Republican','TN': 'Republican','TX': 'Republican','UT': 'Republican','VT': 'Democrat',
            'VA': 'Democrat','WA': 'Democrat','WV': 'Republican','WI': 'Republican','WY': 'Republican', 'DC': 'Democrat'
    }          

    # add the winning party and fill any missing data with 'No Data'
    gdf['winning_party'] = gdf['STUSPS'].map(winning_party).fillna('No Data')

    plot_electoral_map(gdf, 'winning_party',legend=True, vote_bar=True)
