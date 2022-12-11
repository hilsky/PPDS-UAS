import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("AirPassengers.csv")
df['Month'] = pd.to_datetime(df['Month'], format='%Y-%m')
df = df.set_index(["Month"])

sns.lineplot(df)
plt.xlabel("Date")
plt.ylabel("Number of Passengers")
plt.plot(df)
plt.show()
