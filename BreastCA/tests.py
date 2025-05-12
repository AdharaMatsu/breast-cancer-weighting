import pandas as pd

df = pd.DataFrame({
    'edad': [20, 25, 30, 35, 40],
    'ingresos': [2000, 2500, 3000, 3500, 4000]
})

print(df['edad'].corr(df['ingresos']))
