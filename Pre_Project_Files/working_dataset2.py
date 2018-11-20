import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import glob
import os
path = '4_year_stints'

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

concatenated_df = pd.concat(edited_df_from_each_file, ignore_index=True)
concatenated_new_df = pd.concat(edited_new_df_from_each_file, ignore_index=True)


#for i in range(len(concatenated_df.index)):
concatenated_df['combined'] = concatenated_df.loc[:, 'GP':'CF% QoC'].values.tolist()
concatenated_new_df['combined'] = np.nan
list = []
for i in range(len(concatenated_new_df)):
    list.append((concatenated_df.loc[4*int(i),'combined'] + concatenated_df.loc[4*int(i) + 1,'combined'] + concatenated_df.loc[4*int(i) + 2,'combined']))

concatenated_new_df['combined'] = list

good_df = concatenated_new_df[['Player', 'combined']]

expanded_df = pd.DataFrame(good_df['combined'].values.tolist())

list2 = []
for i in range(len(concatenated_new_df)):
    list2.append((concatenated_df.loc[4*int(i) + 3, 'P']))

expanded_df['Target'] = list2

