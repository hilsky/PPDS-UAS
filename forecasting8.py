from sklearn.metrics import mean_squared_error
from math import sqrt
from pmdarima.arima import auto_arima
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("AirPassengers.csv")
df["Month"] = pd.to_datetime(df["Month"], format="%Y-%m")
df = df.set_index(["Month"])

df["Date"] = df.index
train = df[df['Date'] < pd.to_datetime("1960-08", format="%Y-%m")]
train['train'] = train['#Passengers']
del train["Date"]
del train["#Passengers"]
test = df[df['Date'] >= pd.to_datetime("1960-08", format="%Y-%m")]
del test['Date']
test['test'] = test["#Passengers"]
del test["#Passengers"]
# plt.plot(train, color="black")
# plt.plot(test, color="red")
# plt.title("Train/Test split for Passenger Data")
# plt.ylabel("Passenger Number")
# plt.xlabel("Year-Month")
# sns.set()
# plt.show()


model = auto_arima(train, trace=True, error_action='ignore',
                   suppress_warnings=True)
model.fit(train)

forecast = model.predict(n_periods=len(test))
# forecast = pd.DataFrame(forecast, index=test, columns=['Predictions'])


rms = sqrt(mean_squared_error(test, forecast))
print("RMSE: ", rms)
