import pandas as pd
from statsmodels.tsa.stattools import adfuller

df = pd.read_csv("AirPassengers.csv")
df = df["#Passengers"]
adft = adfuller(df, autolag="AIC")

output_df = pd.DataFrame({"Values": [adft[0], adft[1], adft[2], adft[3], adft[4]['1%'], adft[4]["5%"], adft[4]["10%"], ], "Metric": [
                         "Test Statistics", "p-value", "No. of lags used", "Number of observations", "critical value (1%)", "critical value (5%)", "critical value (10%)"]})

print(output_df)

df["Month"] = pd.to_datetime(df["Month"], format='%Y-%m')
df = df.set_index(["Month"])

df["Month"] = df.index
train = df[df["Month"]] < pd.to_datetime("1960-08", format='%Y-%m')
test = df[df["Month"]] >= pd.to_datetime("1960-08", format='%Y-%m')

# test = df["#Passengers"]
# rms = sqrt(mean_squared_error(test, forecast))
