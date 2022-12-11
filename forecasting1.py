import pandas as pd

df = pd.read_csv("AirPassengers.csv")

print(df.tail())

# Jawaban soal pertama
lastDate = df["Month"].tail().max()
print("Data terakhir berada pada tahun:", lastDate)

# Jawaban soal kedua
maxPassengers = df[["Month", "#Passengers"]].tail().max()
print("Penumpang terbanyak berada pada tahun:", maxPassengers)


# Jawaban soal ketiga
totalPassenger = df['#Passengers'].tail().sum()

print("Total keseluruhan penumpang berjumlah:", totalPassenger)
