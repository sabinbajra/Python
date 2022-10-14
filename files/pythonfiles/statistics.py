import pandas as pd
import matplotlib.pyplot as plt


# df = pd.read_csv('AMZN.csv')
# print(df.to_string())
# print(df.std())
# print(df['Open'].mean())
# print(df['Close'].mean())
# print("Stock: {} - Mean: {} - Standard deviation: {}".format('AMZN', df['Close'].mean(), df['Close'].std()))

def get_dataframe_fromCSV(filename):
    df = pd.read_csv(filename)
    return df


stock = "AMZN"
df = get_dataframe_fromCSV('{}.csv'.format(stock))

data = df['Close']
mean = df['Close'].mean()
median = df['Close'].median()
std = df['Close'].std()

min_value = min(data)
max_value = max(data)

plt.title("::Amazon Dataset::")
plt.ylim(min_value-100, max_value+100)
plt.scatter(x=df.index, y=df['Close'])
plt.hlines(y=mean, xmin=0, xmax=len(data))
plt.hlines(y=median, xmin=0, xmax=len(data),colors='r')
plt.show()
