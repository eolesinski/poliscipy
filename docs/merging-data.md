---
layout: default
title: Merging Data
parent: Data and Shapefiles
nav_order: 2
---

# Data

This section explains how to merge election data with shapefiles in PoliSciPy for creating visualizations of electoral college results. You will learn how to integrate election data into a geoDataFrame, handle non-winner-takes-all states like Nebraska and Maine, and account for defecting or faithless electors in your maps.

---

## Merging Election Data

Plotting electoral college data using PoliSciPy is very easy. All you need to do is create a dictionary with the data that you woudl like to plot, and then merge it into the geoDataFrame above.

### Adding the data

To merge the election results into your geoDataFrame, create or import a dictionary with the election data for each state, then map the results to the appropriate state abbreviations in the geoDataFrame.

```python
winning_party_2024 = {
    'AL': 'Republican', 'AK': 'Republican', 'AZ': 'Republican', 'AR': 'Republican', 'CA': 'Democrat',
    'CO': 'Democrat', 'CT': 'Democrat', 'DE': 'Democrat', 'FL': 'Republican', 'GA': 'Republican',
    'HI': 'Democrat', 'ID': 'Republican', 'IL': 'Democrat', 'IN': 'Republican', 'IA': 'Republican',
    'KS': 'Republican', 'KY': 'Republican', 'LA': 'Republican', 'ME': 'Democrat', 'MD': 'Democrat',
    'MA': 'Democrat', 'MI': 'Republican', 'MN': 'Democrat', 'MS': 'Republican', 'MO': 'Republican',
    'MT': 'Republican', 'NE': 'Republican', 'NV': 'Republican', 'NH': 'Democrat', 'NJ': 'Democrat',
    'NM': 'Democrat', 'NY': 'Democrat', 'NC': 'Republican', 'ND': 'Republican', 'OH': 'Republican',
    'OK': 'Republican', 'OR': 'Democrat', 'PA': 'Republican', 'RI': 'Democrat', 'SC': 'Republican',
    'SD': 'Republican', 'TN': 'Republican', 'TX': 'Republican', 'UT': 'Republican', 'VT': 'Democrat',
    'VA': 'Democrat', 'WA': 'Democrat', 'WV': 'Republican', 'WI': 'Republican', 'WY': 'Republican',
    'DC': 'Democrat'
}
```

Then merge the dictionary with the `geoDataFrame` like this:

```python
# add the winning party and fill any missing data with 'No Data'
gdf['winning_party'] = gdf['STUSPS'].map(winning_party_2024).fillna('No Data')
```

This should merge the data so that you can start plotting it.

---

## Adding defectors

The ability to account for defecting or faithless electors is a crucial feature for electoral college maps. 

### Non-winner-takes-all states (Nebraska and Maine)

While most states use a "winner-takes-all" system, there are two notable exceptions: Nebraska and Maine. These states allocate their electoral votes differently, apportioning them based on the percentage of votes each candidate receives in each congressional district, in addition to awarding two electors based on the winner of the overall state-wide popular vote. This system can result in cases where, despite having five electoral votes, multiple candidates may be awarded electoral votes in Nebraska, leading to a "split" state.

If you would like to represent this "split" state for Nebraska and Maine, you can use the `defectors` and `defector_party` columns in the `geoDataFrame`. To do this, simply input the number of defectors for each state and their respective party affiliation.

```python
# set the number of defectors for each state to one
gdf['defectors'][10] = 1 # nebraska
gdf['defectors'][38] = 1 # maine

# set the party affiliation of the defecting voter
gdf['defector_party'][10] = 'Democrat'
gdf['defector_party'][38] = 'Republican'
```

Note: To identify the correct index for each state in the `geoDataFrame`, you can filter it by the `STUSPS` column using the following line: `gdf['STUSPS']`

This will return a list of state abbreviations you can use:

```python
0     MS
1     NC
2     OK
3     VA
...
```

For a full example of creating Electoral College maps with non-winner-takes-all states included in the map see Example 1 in the Tutorials and Examples section.
