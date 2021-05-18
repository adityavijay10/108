import pandas as pd
import csv

df=pd.read_csv('./108.csv')

import plotly.figure_factory as ff

fig=ff.create_distplot([df['Avg Rating'].tolist()],['Avg Rating'],show_hist=False)
fig.show()
