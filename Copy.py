import csv

GOOG = "GOOG.csv"
GOOG_2 = "GOOG_2.csv"

IBM = "IBM.csv"
IBM_2 = "IBM_2.csv"

MSFT = "MSFT.csv"
MSFT_2 = "MSFT_2.csv"


with open(GOOG, 'r', newline='') as f, open(GOOG_2, 'w', newline='') as data:
     writer = csv.writer(data, delimiter=',', quoting=csv.QUOTE_NONE, escapechar=',')
     writer.writerows(line.split() for line in f)

try:
     import pandas as pd
     new_val = pd.read_csv('GOOG_2.csv', sep=',', usecols=['Date', 'Open', 'High', 'Low', 'Close', 'AdjClose', 'Volume'])
     new_val['Change'] = (new_val['Close'] - new_val['Open']) / new_val['Open']
     new_val.to_csv('Polaczone_2.csv', index=False)
except:
     print("Something went wrong when writing to the file")
finally:
    f.close()

    with open(IBM, 'r', newline='') as f, open(IBM_2, 'w', newline='') as data:
        writer = csv.writer(data, delimiter=',', quoting=csv.QUOTE_NONE, escapechar=',')
        writer.writerows(line.split() for line in f)

try:
    import pandas as pd

    new_val = pd.read_csv('IBM_2.csv', sep=',', usecols=['Date', 'Open', 'High', 'Low', 'Close', 'AdjClose', 'Volume'])
    new_val['Change'] = (new_val['Close'] - new_val['Open']) / new_val['Open']
    new_val.to_csv('Polaczone_2_IBM.csv', index=False)
except:
    print("Something went wrong when writing to the file")
finally:
    f.close()

    with open(MSFT, 'r', newline='') as f, open(MSFT_2, 'w', newline='') as data:
        writer = csv.writer(data, delimiter=',', quoting=csv.QUOTE_NONE, escapechar=',')
        writer.writerows(line.split() for line in f)

try:
    import pandas as pd

    new_val = pd.read_csv('MSFT_2.csv', sep=',', usecols=['Date', 'Open', 'High', 'Low', 'Close', 'AdjClose', 'Volume'])
    new_val['Change'] = (new_val['Close'] - new_val['Open']) / new_val['Open']
    new_val.to_csv('Polaczone_2_MSFT.csv', index=False)
except:
    print("Something went wrong when writing to the file")
finally:
    f.close()