import pandas as pd
import time
import datetime
import csv

ticker = 'BTC-EUR' #Name of ticker
period1 = int(time.mktime(datetime.datetime(2022, 1, 22,23,59).timetuple())) #The day that start your search
period2 = int(time.mktime(datetime.datetime(2022, 1, 31,23,59).timetuple())) #The day that ends your search
interval = '1d' #The range within the search

query_string = f'https://query1.finance.yahoo.com/v7/finance/download/{ticker}?period1={period1}&period2={period2}&interval={interval}&events=history&includeAdjustedClose=true' #URL finance

df = pd.read_csv(query_string)
df.to_csv('eur_btc_rates_complete.csv') #Create the csv with all the data

# Gonna create a new archive csv the end file
f = open('eur_btc_rates.csv', 'w', newline='') # Put into 'newfile.csv' the name of end file gonna be created
w = csv.writer(f, quoting=csv.QUOTE_NONNUMERIC, delimiter=',')

# Open the main csv file which you will use to look up the txt information
with open('eur_btc_rates_complete.csv') as arquivo_pricebtc: #Put into 'Teste.csv' the main csv
    table = csv.reader(arquivo_pricebtc, delimiter=',')

    for l in table:
        date = l[1]
        price = l[5]

        w.writerow([date, price])

f.close()

print(pd.read_csv("eur_btc_rates.csv"))
