import pandas as pd

data = [
    ("Toyota", "Corolla", "Blue"), 
    ["Ford", "K", "Yellow"], 
    ["Porche", "Cayenne", "White"]]

df = pd.DataFrame(data=data,columns=['Make','Model','Color'])

print(df)


