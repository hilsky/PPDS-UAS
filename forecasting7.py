import pandas as pd
from statsmodels.tsa.seasonal import seasonal_decompose
import matplotlib.pyplot as plt

df = pd.read_csv("AirPassengers.csv")
df['Month'] = pd.to_datetime(df["Month"], format='%Y-%m')
df = df.set_index(["Month"])

decompose = seasonal_decompose(df["#Passengers"], model='additive', period=7)
decompose.plot()
plt.show()
