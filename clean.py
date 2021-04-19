import os
import pandas as pd
import csv

cc_to_name = {'ar': 'Argentina',
 'au': 'Australia',
 'at': 'Austria',
 'be': 'Belgium',
 'bo': 'Bolivia',
 'br': 'Brazil',
 'bg': 'Bulgaria',
 'cl': 'Chile',
 'co': 'Colombia',
 'cy': 'Cyprus',
 'cz': 'Czech Republic',
 'dk': 'Denmark',
 'sv': 'El Salvador',
 'fi': 'Finland',
 'fr': 'France',
 'de': 'Germany',
 'hn': 'Honduras',
 'hk': 'Hong Kong',
 'hu': 'Hungary',
 'is': 'Iceland',
 'ie': 'Ireland',
 'it': 'Italy',
 'lv': 'Latvia',
 'lu': 'Luxembourg',
 'my': 'Malaysia',
 'mx': 'Mexico',
 'ni': 'Nicaragua',
 'no': 'Norway',
 'py': 'Paraguay',
 'pe': 'Peru',
 'ph': 'Philippines',
 'pl': 'Poland',
 'pt': 'Portugal',
 'sg': 'Singapore',
 'sk': 'Slovakia',
 'es': 'Spain',
 'se': 'Sweden',
 'ch': 'Switzerland',
 'tw': 'Taiwan',
 'tr': 'Turkey',
 'gb': 'United Kingdom',
 'uy': 'Uruguay',
 'us': 'United States',
 'jp': 'Japan',
 'id': 'Indonesia',
 'ca': 'Canada'}

folder_names = ['2017', '2018', '2019']
rows = {}
for f in folder_names:
    directory = 'data/'+f
    for filename in os.listdir(directory):
        if filename.endswith(".csv"):
            df = pd.read_csv(directory + '/' + filename)
            country_code = filename.split('_')[1]
            country_name = cc_to_name[country_code]
            if country_name not in rows:
                rows[country_name] = []
                rows[country_name].append(country_name)
            rows[country_name].append(df['Danceability'].mean())
            rows[country_name].append(df['Valence'].mean())
            rows[country_name].append(df['Energy'].mean())

happy17 = {}
happy18 = {}
happy19 = {}
h_names = ['2017.csv', '2018.csv', '2019.csv']
h_dicts = [happy17, happy18, happy19]

directory = 'happiness_data/'
for i in range(0,3):
    df_happy = pd.read_csv(directory+h_names[i])
    di = h_dicts[i]
    for j in range(0,df_happy['Country'].size):
        di[df_happy['Country'][j]] = [df_happy['Score'][j], df_happy['Rank'][j]]

for d in h_dicts:
    for country in rows:
        rows[country] += d[country]

print(happy18)

final_df = pd.DataFrame(columns=['Country', '17 Danceability', '17 Valence', '17 Energy',
                                 '18 Danceability', '18 Valence', '18 Energy',
                                 '19 Danceability', '19 Valence', '19 Energy',
                                 '17 Happiness', '17 Rank',
                                 '18 Happiness', '18 Rank',
                                 '19 Happiness', '19 Rank'])
index = 0
for cc in rows:
    if len(rows[cc]) == 16:
        final_df.loc[index] = rows[cc]
        index += 1

final_df.to_csv('./final.csv', index=False)