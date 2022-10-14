import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

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

sns.set()
plt.title("::Amazon Dataset::")
plt.xlabel("Value of Amazon stocks")
plt.ylabel('Value of closing stocks')
plt.hist(data,bins=20,rwidth=0.95,label='Stocks',orientation='vertical')

plt.show()
