# -*- coding: utf-8 -*-
"""stock_investment_assistance.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1CYIFPs0UYc8GgcN_SSXOALthaIk_eUEI

# 1. Environment&Import
"""

start='2022-01-01'
end='2023-04-13'

import financial
# 1. Create portfolio from csv
portfoilo=financial.portfolio('PRIVATE',start,end)
portfoilo.implement()

# 2. Search Tickers
tickers=financial.tickerSearch('NYSE','우라늄').download(start,end,filterPercent=0.5)
print(tickers)

# 3. Compare Financials
tickerDict={
    'SEARCH':tickers.index,
    'WATCH':['CLFD','STEM','GOOG','GFL','CLH','DE','CWEN','OPCH'],
    'SAMPLE':['AAPL','F','DIS','AMZN','KO','GOOG','XOM'],
    'EX':['GOOG','CLFD','STEM']
}
financial.financialCompare(tickerDict,'EX').implement()


