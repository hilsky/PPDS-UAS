import pandas as pd

df = pd.read_csv("AirPassengers.csv")

print(df.tail())

#Jawaban ketiga
totalPassenger = df['#Passengers'].tail().sum()

print(totalPassenger)