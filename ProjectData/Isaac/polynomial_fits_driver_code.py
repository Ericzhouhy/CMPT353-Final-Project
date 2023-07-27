import pandas as pd
import unemployment_rate_fit as usual
import during_pandemic_fit as during_pandemic
import os
names = ['Alberta',
         'British Columbia',
         'Canada',
         'Manitoba',
         'New Brunswick',
         'Newfoundland and Labrador',
         'Nova Scotia',
         'Ontario',
         'Prince Edward Island',
         'Quebec',
         'Saskatchewan'
]
os.makedirs('./usual', exist_ok = True)
os.makedirs('./pandemic', exist_ok = True)
usual_results_df = pd.DataFrame(columns=['GEO',
                                         'result 1 pvalue',
                                         'result 2 pvalue',
                                         'result 3 score',
                                         'result 4 score'])
during_pandemic_df = usual_results_df
for name in names:
    usual_result = usual.fit(name)
    usual_results_df = pd.concat([usual_results_df, usual_result],
                                 axis = 0,
                                 ignore_index= True)
    during_pandemic_result = during_pandemic.fit(name)
    during_pandemic_df = pd.concat([during_pandemic_df, during_pandemic_result],
                                   axis = 0,
                                   ignore_index = True)

usual_results_df.to_csv('usual_polynomial_fits.csv', index = False)
during_pandemic_df.to_csv('during_pandemic_polynomial_fits.csv', index = False)

