import pandas as pd

def divideby2(x):
    return x / 2

my_series = pd.Series([2, 4, 6, 8, 10])
print(my_series.apply(divideby2))

