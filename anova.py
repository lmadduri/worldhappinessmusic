import pandas as pd
import scipy.stats as stats

df = pd.read_csv('final_plus.csv')
indep = '17 Valence'
group = 'Region'

anova1 = stats.f_oneway(df[indep][df[group] == 'Australia and New Zealand'],
                        df[indep][df[group] == 'Central and Eastern Europe'],
                        df[indep][df[group] == 'Eastern Asia'],
                        df[indep][df[group] == 'Latin America and Caribbean'],
                       df[indep][df[group] == 'Middle East and Northern Africa'],
                       df[indep][df[group] == 'North America'],
                       df[indep][df[group] == 'Southeastern Asia'],
                       df[indep][df[group] == 'Western Europe'])

anova2 = stats.f_oneway(df[indep][df[group] == 'Latin America and Caribbean'],
                       df[indep][df[group] != 'Latin America and Caribbean'])

anova3 = stats.f_oneway(df[indep][df['Spanish'] == 'Yes'],
                       df[indep][df['Spanish'] == 'No'])

print(anova1)
print(anova2)
print(anova3)