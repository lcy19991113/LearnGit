import pandas as pd
import numpy as np
import plotly.express as px
train = pd.read_csv('data/train.csv')
print(train.head())

book_example = pd.read_parquet('data/book_train.parquet/stock_id=0')
trade_example = pd.read_parquet('data/trade_train.parquet/stock_id=0')
stock_id = '0'
book_example = book_example[book_example['time_id']==5]
book_example.loc[:,'stock_id'] = stock_id
trade_example = trade_example[trade_example['time_id']==5]
trade_example.loc[:,'stock_id'] = stock_id




print('hh')