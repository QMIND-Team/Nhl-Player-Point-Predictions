import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import glob
import os
path = '4_year_stints'

#get path for all csv files within folder designated above.
all_files = glob.glob(os.path.join(path, "*.csv"))     # advisable to use os.path.join as this makes concatenation OS independent

df_from_each_file = (pd.read_csv(f) for f in all_files)

count = 0
edited_df_from_each_file = []
edited_new_df_from_each_file = []


for df in df_from_each_file:
    # Groups by player name and counts the frequency.
    players = df.groupby(df.Player).count()
    players = players[players.Season >= 4]

    # Removes players that havent played 4 seasons
    df = df[df.Player.isin(players.index)]
    df['Player'] = str(count) + df['Player'].astype(str)

    new_df = df.drop_duplicates('Player', keep='first')

    edited_df_from_each_file.append(df)
    edited_new_df_from_each_file.append(new_df)

    count += 1

# Combine all the seasons into one file (contains duplicate player rows
concatenated_df = pd.concat(edited_df_from_each_file, ignore_index=True)
# Combine all seasons into one file (just the first player row from each 4 year stint)
concatenated_new_df = pd.concat(edited_new_df_from_each_file, ignore_index=True)

# Create new attribute called combined, which is a list of all the numerical columns
concatenated_df['combined'] = concatenated_df.loc[:, 'GP':'CF% QoC'].values.tolist()
concatenated_new_df['combined'] = np.nan
list = []

# loop through the dataframe with duplicates removed and add the 3 consecutive years stats as columns
for i in range(len(concatenated_new_df)):
    list.append((concatenated_df.loc[4*int(i),'combined'] + concatenated_df.loc[4*int(i) + 1,'combined'] + concatenated_df.loc[4*int(i) + 2,'combined']))

# Store that list in the combine column of dataframe, pick out the important columns and expand combined into individual elements
concatenated_new_df['combined'] = list
good_df = concatenated_new_df[['Player', 'combined']]
expanded_df = pd.DataFrame(good_df['combined'].values.tolist())

list2 = []
for i in range(len(concatenated_new_df)):
    list2.append((concatenated_df.loc[4*int(i) + 3, 'P']))

expanded_df['Target'] = list2

