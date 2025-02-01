---
layout: default
title: Data and Shapefiles
nav_order: 6
---

# Working with Data and Shapefiles

This section covers how to use shapefiles and related data with PoliSciPy to create custom maps for visualizing historical and current elections. You will learn how to load, manipulate, and merge shapefiles with election data to generate meaningful visualizations.

---

### Faithless electors

Similar to representing electoral votes for the Congressional districts in Maine and Nebraska, it can also be useful to use defecting voters to represent faithless electors. Faithless electors are electoral college voters that, despite the popular vote of the respective states, choose to vote a differnt candidate than thier state selected. While rare, these faitheless electors may vote for the other candidate or a candidate that does not even appear on the ballot. While rare, the most recent example of this occured in 2016 when there were 7 electors that cast votes against the will of thier respetive states.

While faithless electors are rare, it can be useful to be able to represent them in electoral college maps. The appraoch for handling faithless electors is the same as for handling Congressional districts above. To add a faithless electors to any state simply set the value in the `defecting_voter` column and the respective `defector_party` for the respective state. If you do not select a defecting party they will be placed into the `Other` category by default.

Note: While defecting voters may sometimes vote for the opposing party, they may also vote for candidates not listed in the current eletction. In this case it may be useful to group them into an `Other` party rather than assigning them thier own color value in the colormap. To do this, simply leave the `defector_party` value blank in the `GeoDataFrame` blank and it will be assinged to the `Other` category by default. You can see an example of how to plot electoral college maps with faithless electors by taking a look at Example 2 in the Examples section.

### Split states

Another case when it could be usefuly to be able to plot defecting voters is when plotting historical elections. Many historical elections, especially those between 1700-1800 often invovled cases where states frequently split electoral votes leading to cases where many candidates won a portion of the total number of electoral votes from that state. Similar to how Nebraska and Maine operate today, it can be useful to plot these defecting electoral votes as an alternative way to represent multople canddiatew winning parts of a single state.

### Absent/missing electors

The last case where it might be useful to be able to plot defecting voters is where an electoral voter may be unable to cast thier vote entirely even if they had intended to vote for the cnadidate who had won the state. One example of this was during the 1864 election (the third example shown on the Examples page) where despite having 3 electoral votes, Nevada only cast 2 votes for Presdient Lincoln. This was a result of the fact that the third electoral voter was snowbound, and there was not yet a practice put in place to deal with absent voters. Not spceifying a poltical party for these defecting voters places them in a default, dark grey colored box to signify and represent an 'Other' catagory.

Note: any defector that does not have a value provided in the `defector_party` column will default to the `Other/Unspecified` catagory.

---

## Representing Territories

Some elections include territories or regions that, while part of the United States at the time, did not cast electoral votes. Representing these territories on the map can provide historical accuracy and help visualize the broader political or geographic context of an election.

## Handling Reconstruction

During the reconstruction period there were some Southern states that were part of the United States, but did not have any electoral college votes. These states are often shown with zero electoral college votes. To represent this on a map using PoliSciPy, you can create a separate category in the colormap to represent these states. Despite haveing no electoral votes, you can still include this additional category in the `winning_party` column when merging in the data. This will plot the color over the respective state without counting any of thier votes in the final results.

## Handling merged States
