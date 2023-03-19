# -*- coding: utf-8 -*-
"""stock_investment_assistance.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1CYIFPs0UYc8GgcN_SSXOALthaIk_eUEI

# 1. Environment&Import
"""

start='2022-01-01'
end='2023-03-19'

import default

# 1. Create portfolio from csv
# default.portfolio('PRIVATE',start,end).implement()

# # 2. Search Tickers
searched=default.tickerSearch('NYSE','전기 유틸리티').download(start,end,filterPercent=0.2)
print(searched)

# 3. Compare Financials

tickerDict={
    'SEARCH':searched.index,
    'SAMPLE':['AAPL','F','DIS','AMZN','KO','GOOG','XOM']
}
default.financialCompare(tickerDict,'SAMPLE').implement()

