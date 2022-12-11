import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("AirPassengers.csv")

df = df.set_index(["Month"])

rolling_mean = df.rolling(7).mean()
rolling_std = df.rolling(7).std()

plt.plot(df, color="blue", label="Original Passenger Data")
plt.plot(rolling_mean, color="red", label="Rolling Mean Passenger Number")
plt.plot(rolling_std, color="black",
         label="Rolling Standar Deviation in Passenger Number")
plt.title("Passenger Time Series, Rolling Mean, Standart Deviation")
plt.legend(loc="best")
plt.show()

# sns.lineplot(df)
# plt.ylabel("Number of Passengers")
# plt.show()
