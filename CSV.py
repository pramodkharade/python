import csv
import datetime


class CSVReader:
    
    def readCsv(self):
        csvfile = open("Google Stock Market_Data_google_stock_data.csv",newline='')
        reader = csv.reader(csvfile)
        header = next(reader) # The first line is the header
        
        data = []
        for row in reader:
            #row = [Date, Open, High,Low, Close, Adj, Close]
            date = datetime.datetime.strptime(row[0],"%m/%d/%Y")
            open_price = float(row[1])
            high = float(row[2])
            low = float(row[3])
            close = float(row[4])
            volume = int(row[5])
            adj_close = float(row[6])
            data.append([date,open_price,high,low,close,volume,adj_close])

    #compute and store daily stock return
            returnpath = "google_return.csv"
            file = open(returnpath,'w')
            writer = csv.writer(file)
            writer.writerow(["Date","Return"])

            for i in range(len(data)-1):
                todays_row = data[i]
                todays_date = todays_row[0]
                todays_price = todays_row[-1]
                yesterdays_row = data[i+1]
                yesterdays_price = yesterdays_row[-1]

                daily_return = (todays_price - yesterdays_price) / yesterdays_price
                formatted_date = todays_date.strftime("%m/%d/%Y")
                writer.writerow([formatted_date,daily_return])
                
                
            
