import pandas as pd
from matplotlib import pyplot as plt
%matplotlib inline
import seaborn as sns

df = pd.read_csv('Pokemon.csv',encoding = "ISO-8859-1", index_col=0)

# df.head()
# sns.lmplot(x="Attack", y="Defense", data=df, fit_reg = False, hue = "Stage")

# plt.ylim(0, None)
# plt.xlim(0, None)
	
# Pre-format DataFrame
# stats_df = df.drop(['Total', 'Stage', 'Legendary'], axis=1)
 
# New boxplot using stats_df
# sns.boxplot(data=stats_df)

sns.set_style('whitegrid') # Set theme
sns.set(rc={'figure.figsize':(15,5)}) # Set size

pkmn_type_colors = ['#78C850',  # Grass
                    '#F08030',  # Fire
                    '#6890F0',  # Water
                    '#A8B820',  # Bug
                    '#A8A878',  # Normal
                    '#A040A0',  # Poison
                    '#F8D030',  # Electric
                    '#E0C068',  # Ground
                    '#EE99AC',  # Fairy
                    '#C03028',  # Fighting
                    '#F85888',  # Psychic
                    '#B8A038',  # Rock
                    '#705898',  # Ghost
                    '#98D8D8',  # Ice
                    '#7038F8',  # Dragon
                   ]


sns.violinplot(x='Type 1', y='Attack', inner = None, data=df)

# Violin plot with Pokemon color palette
sns.violinplot(x='Type 1', y='Attack', data=df, pallette = inner=None ) # Set color palette for violin plot
sns.swarmplot(x='Type 1', y='Attack', data=df, palette=pkmn_type_colors) # Set color palette for swarm plot
