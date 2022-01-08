from IPython.display import display
import pandas as pd



df = pd.read_csv('.learn/assets/us_baby_names_right.csv')
display(df.head(10))
