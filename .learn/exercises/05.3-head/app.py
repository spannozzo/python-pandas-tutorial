from IPython.display import display
import pandas as pd


df = pd.read_csv('.learn/assets/pokemon_data.csv')

display(df.head(3))

