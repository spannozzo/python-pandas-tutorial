import pandas as pd

data = [
    { 
        "make": "Toyota", 
        "model": "Corolla",
        "color": "Blue"
    },
    {
        "make": "Ford", 
        "model": "K",
        "color": "Yellow"
    },
    {
        "make": "Porche", 
        "model": "Cayenne",
        "color": "White"
    }
]

df = pd.DataFrame(data)
df = df.append({
    "make": "Tesla", 
    "model": "Model S",
    "color": "Red"
},ignore_index=True)

print(df.iloc)


