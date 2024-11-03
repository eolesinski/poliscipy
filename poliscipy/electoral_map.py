import geopandas as gpd

import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import matplotlib.patches as mpatches

from matplotlib.colors import ListedColormap
from shapely.affinity import scale
from mpl_toolkits.axes_grid1.inset_locator import inset_axes
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
    scale_factor_x = 1.1

    # apply an affine transformation to conduct horizontal scaling
    scaled_geometry_2 = hawaii['geometry'].apply(lambda geom: scale(geom, xfact=HAWAII_SCALE_FACTOR_X, yfact=1.0))
    
    gdf.loc[gdf['STUSPS'] == 'HI', 'geometry'] = scaled_geometry_2
     
    return gdf


# create a dictionary to map the colors of the political parties
party_colors = {
    'Democrat': '#4875b1',    
    'Republican': '#b82b2b',  
    'No Data': 'lightgray',
    'Green': '#519e3e',
    'Independent': '#8d69b8'
}


def _add_vote_bar(gdf: gpd.GeoDataFrame, ax: plt.Axes, column: str, party_colors: dict, 
                  vote_scale_factor: int = 20, initial_bar_position: float = -113.5) -> None:
    """
    Adds a vote bar containing the total votes for a party at the top of the plot.
    
    Parameters:
    - gdf (GeoDataFrame): The GeoDataFrame containing the election data
    - ax (Axes): The Axes object used in the figure
    - column (str): The column that is being plotted
    - party_colors (dict): A dictionary containing the party color mappings
    - vote_scale_factor (int): Factor to scale the total votes for plotting (default: 20)
    - initial_bar_position (float): Starting position for the bars (default: -113.5)
    
    Returns:
    - None
    """
    
    # Create a dictionary to store the total vote counts for each party
    total_votes = {party: gdf.loc[gdf[column] == party, 'elec_votes'].sum() 
                    for party in party_colors.keys()}

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
