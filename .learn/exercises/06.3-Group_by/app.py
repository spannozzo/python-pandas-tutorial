from IPython.display import display
import pandas as pd
import io


df = pd.read_csv('.learn/assets/us_baby_names_right.csv',index_col=[0])
df = pd.read_csv(io.StringIO(df.to_csv(index=False)))

#print(df.sample(5))

group = df.groupby('Name')


print(group.sum())
print(len(group))