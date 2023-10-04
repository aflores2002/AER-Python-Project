import pandas as pd
#skips first 13 rows
df = pd.read_csv("Charlie-DataLog-9-24.csv", skiprows=13,
                 usecols=['Time', 'D1 DC Bus Voltage','D4 DC Bus Current','D4 VBC Vq Voltage',
                          'D2 Output Voltage','D3 HV Input Current','D2 Max Charge Current','Fast DC Bus Voltage'])
print(df)
