import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("AirPassengers.csv")
df['Month'] = pd.to_datetime(df['Month'],format='%Y-%m')

sns.lineplot(df)
plt.ylabel("Number of Passengers")
plt.show()