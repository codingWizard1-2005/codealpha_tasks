import csv
import os #(it will be used to check if the file is empty, as i will implement condition to define headers in csv columns)
#Define our stock price database
#This dictionary maps the stock Ticker(key) to it's price(value)

stock_prices = {
    "AAPL": 180, #APPLE 
    "TSLA": 250, #TESLA
    "GOOGL": 140, #GOOGLE
    "MSFT": 370   #MICROSOFT ID
}

print("Price list loaded successfully!")

try:
#Ask user for their holdings
  Ticker = input("Enter the stock ticker of any company (AAPL,TSLA,GOOGL or MSFT): ").upper()
  

  if Ticker in stock_prices:
    shares = int(input("Enter the number of shares you own: "))
    price = stock_prices[Ticker]
    total_investment = price * shares
    print(f"The current price of {Ticker} is {price} $" )
    print(f"Your total investment value is: {total_investment} $.\n")
  else:
    print(f"Error: we don't have price data for '{Ticker}'.")
    print("please try: AAPL, TSLA, GOOGL, or MSFT.\n")
except ValueError:
   print("Error!, please enter the whole number for the quantity of shares")

#  except Exception as e:
#    print(f'An unexpected error occured: {e}')

#save the result to a csv file
try:
 file_name = 'portifolio.csv'
 file_is_empty = not os.path.exists(file_name) or os.stat(file_name).st_size == 0 

 with open(file_name , mode="a", newline='') as file:
    writer = csv.writer(file)
    
#if it's a new file, write the headers first!
    if file_is_empty:
      writer.writerow(["Stock Ticker", "Quantity", "Total Investment($)"])
 #then write the actual user data
    writer.writerow([Ticker, shares, total_investment])
    print("Well, your portifolio has been saved in", file_name)
except:
   print("Error failed to save your portifolio in ", file_name)
  
    





