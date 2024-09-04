import pandas as pd
data=pd.read_csv(r"E:\Dataset\auto-mpg.csv")
print(data)
hp_mean=data['Horsepower'].mean()
print("mean horsepower\n",hp_mean)
acc_std=data['Acceleration'].std()
print("standard deviation of acceleration\n",acc_std)
manufacture_by_year=data['Model Year'].value_counts().sort_index()
print("no of cars manufacturd in each year\n",manufacture_by_year)