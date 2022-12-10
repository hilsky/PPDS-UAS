import pandas as pd

df = pd.read_csv("AirPassengers.csv")

autoCorrelation_lag1 = df["#Passengers"].autocorr(lag=1)
print("One Month Lag:", autoCorrelation_lag1)

autoCorrelation_lag3 = df["#Passengers"].autocorr(lag=3)
print("Three Month Lag:", autoCorrelation_lag1)

autoCorrelation_lag6 = df["#Passengers"].autocorr(lag=6)
print("Six Month Lag:", autoCorrelation_lag1)

autoCorrelation_lag9 = df["#Passengers"].autocorr(lag=9)
print("Nine Month Lag:", autoCorrelation_lag1)