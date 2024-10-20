def plot_electoral_map(gdf: gpd.GeoDataFrame, column: str, title: str = "Electoral College Map", 
                       figsize: tuple = (20, 10), edgecolor: str = 'white', linewidth: float = .5,
                       labelcolor: str = 'white', legend=True, year='2024', **kwargs) -> None:
    """
    Plots an electoral college map of the United States using Matplotlib and GeoPandas.
    
    Parameters:
    - gdf: GeoDataFrame containing the electoral college data
    - column: The target column to plot
    - title (str): Title of the plot
    - figsize (tuple): Size of the figure (default: (20, 10))
    - edgecolor: Edgecolor for the states
    - linewidth: Width of the state borders
    - labelcolor: Color of the state labels (default: 'white')
    
    Returns:
    - None
    
    """
    
    fig1, ax1 = plt.subplots(figsize=figsize)

    gdf.plot(ax=ax1, edgecolor=edgecolor, linewidth=linewidth, color=gdf[column].map(party_colors), **kwargs)

    # plot the state labels at each of the state's respective centroids
    for x_centroid, y_centroid, postal_label, elec_votes in zip(gdf['centroid_x'], gdf['centroid_y'], 
                                                            gdf['STUSPS'], gdf['elec_votes']):
    
        ax1.annotate(f"{postal_label}\n{elec_votes}", (x_centroid, y_centroid), ha='center', va='center',
                     textcoords="data", color=labelcolor)
        
    if legend:
        # Get unique values in the specified column of the GeoDataFrame
        unique_parties = gdf[column].unique()
    
        # Create handles for only the parties present in the data
        handles = [mpatches.Patch(color=party_colors[party], label=party) 
                   for party in unique_parties if party in party_colors]

        # Add the legend to the plot
        ax1.legend(handles=handles, loc='lower right')
        
    if int(year) < 1996:
    
        raise ValueError("Year must be 1996 or later")

      
    ax1.axis('off')
    ax1.set_title(title, fontsize=16)
    
    plt.show();
