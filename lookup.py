##12/06/2021
##Luis Severino
##Python Version 3.6
## Created on Ubuntu 20.04 using Sublime Text


import matplotlib.pyplot as plt
from tkinter import * 
import tkinter as tk
### I had error messages because the tkinter module was not found 
### error message was because I have three python versions installed  python2.7 python 3.6 and python 3.9
#### the default  was python 3.9 the tkinter module was intalled under the 3.6 version 
#### I used **sudo update-alternatives --config python** to manually select the python 3.6 in the terminal
from PIL import Image
from PIL import ImageTk
import requests
import json
import os

#This clears the terminal in Ubuntu when when running the python file
os.system('clear')
#################################################################

#This function defines a coloe based on the value of the int.
def red_green(amount):
  if amount >= 0:
    return "green"
  else:
    return "red"

root  = Tk()
root.title("Crypto Currency Portfolio")



###***************Create Header**********************


#head= ["Name", "Rank", "Current Price", "Price Paid", "P/L Per", "1-Hour Change", "24-Hour Change", "7-Day Change", "Current Value", "Profit Loss total"]
header_name = Label(root, text="Name", bg="white", font= "Verdona 8 bold")
header_name.grid(row=0, column=0, sticky=N+S+E+W)

header_rank = Label(root, text="Rank", bg="silver", font= "Verdona 8 bold")
header_rank.grid(row=0, column=1, sticky=N+S+E+W)

header_current_price = Label(root, text="Current Price", bg="white", font= "Verdona 8 bold")
header_current_price.grid(row=0, column=2, sticky=N+S+E+W)

header_Price_Paid = Label(root, text="Price Paid", bg="silver", font= "Verdona 8 bold")
header_Price_Paid.grid(row=0, column=3, sticky=N+S+E+W)

header_profit_loss_per = Label(root, text="Profit Loss Per Coin", bg="white", font= "Verdona 8 bold")
header_profit_loss_per.grid(row=0, column=4, sticky=N+S+E+W)

header_1_Hour_Change = Label(root, text="1-Hour Change", bg="silver", font= "Verdona 8 bold")
header_1_Hour_Change.grid(row=0, column=5, sticky=N+S+E+W)

header_24_Hour_Change = Label(root, text="24-Hour Change", bg="white", font= "Verdona 8 bold")
header_24_Hour_Change.grid(row=0, column=6, sticky=N+S+E+W)

header_7_Day_Change = Label(root, text="7-Day Change", bg="silver", font= "Verdona 8 bold")
header_7_Day_Change.grid(row=0, column=7, sticky=N+S+E+W)

header_Current_Value = Label(root, text="Current Value", bg="white", font= "Verdona 8 bold")
header_Current_Value.grid(row=0, column=8, sticky=N+S+E+W)

header_Profit_Loss_total = Label(root, text="Profit Loss total", bg="silver", font= "Verdona 8 bold")
header_Profit_Loss_total.grid(row=0, column=9, sticky=N+S+E+W)


#root.iconbitmap(r'/dev/sda10/home/school/BTC.ico')
##Got this error message.
##root.tk.call('wm', 'iconphoto', root._w, tk.PhotoImage(file='BTC.ico'))
##NameError: name 'tk' is not defined
### I forgot to add import tkinter as tk to the top this fixed the error

##root.tk.call('wm', 'iconphoto', root._w, tk.PhotoImage(file='/home/school/BTC.jpg'))
##***The above code gave me the following error message***
##File "/usr/lib/python3.6/tkinter/__init__.py", line 3545, in __init__
##Image.__init__(self, 'photo', name, cnf, master, **kw)
##File "/usr/lib/python3.6/tkinter/__init__.py", line 3501, in __init__
##self.tk.call(('image', 'create', imgtype, name,) + options)
##tkinter.TclError: couldn't recognize data in image file "/home/school/BTC.jpg"
## I downloaded Pillow and used  ImageTk to fix that problem

root.tk.call('wm', 'iconphoto', root._w, ImageTk.PhotoImage(file='/home/school/BTC.jpg'))
##***got this error message from the abive code
##Error of failed request:  BadLength (poly request too large or internal Xlib length error)
##Major opcode of failed request:  190 ()
##Minor opcode of failed request:  0
##Serial number of failed request:  188
##Current serial number in output stream:  188
## After resizing the image from 6000px to 100ox it worked




from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
## This calls the information from the API ans sets the parameters
url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
parameters = {
  'start':'1',
  'limit':'5000',
  'convert':'USD'
}
headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': '3ccdf1ca-11fb-4061-8d4e-0821b7ddada8',
}

session = Session()
session.headers.update(headers)




def lookup():

  try:
    #This lists the Crypto coins that will be alled from the API
    currencies = ["BTC", "XRP", "EOS", "STEEM"]
    response = session.get(url, params=parameters)
    api = json.loads(response.content)
    # We list [] the Crypto we are calling the amount paid and the amount owned. 
    # We do this define dic between the curly brackets {}.
    My_portfolio= [
        {
  	     "sym"           : "STEEM",
  	     "amount_owned"  : 800,
  	     "price_paid_per": .80
        },
        {
          "sym"           : "XRP",
          "amount_owned"  : 5000,
          "price_paid_per": .20
        },
        {
          "sym"           : "XML",
          "amount_owned"  : 3000,
          "price_paid_per": .80
        },
        {
          "sym"           : "EOS",
          "amount_owned"  : 800,
          "price_paid_per": .80
        },
        {
          "sym"           : "BTC",
          "amount_owned"  : 800,
          "price_paid_per": .80
        },
        ]
   
   ## The following variables are assinged(=) to a starting value in this case is '0' defining them as integers. 
    portfolio_profit_loss = 0
    total_current_value = 0
    total_profit_loss_per_coin = 0
    total_onehr_chng = 0
    total_tfhr_chng = 0
    total_7d_chng = 0
    row_count = 1

    # We define pie and pie_size as an empty list using the [].
    pie = []
    pie_size = []
    for x in api['data']:
      for coin in My_portfolio:
        if coin["sym"] == x["symbol"]:
          
          total_paid = float(coin["price_paid_per"]) * float(coin["amount_owned"])
          Current_Value = float(coin["amount_owned"]) * float(x["quote"]["USD"]["price"])
          profit_loss = total_paid - Current_Value
          profit_loss_per_coin = float(x["quote"]["USD"]["price"]) * float(coin["price_paid_per"])
          portfolio_profit_loss += profit_loss
          total_current_value += Current_Value
          total_profit_loss_per_coin += profit_loss_per_coin
          onehr_chng = float(x["quote"]["USD"]["percent_change_1h"])
          tfhr_chng = float(x["quote"]["USD"]["percent_change_24h"])
          sevend_chng = float(x["quote"]["USD"]["percent_change_7d"])
          total_7d_chng += sevend_chng
          total_tfhr_chng += tfhr_chng
          total_onehr_chng += onehr_chng
          pie.append(x["name"])
          pie_size.append(coin["amount_owned"])


          #print(x["name"])
          #print(x["quote"]["USD"]["price"])
          #print("Current Price ${0:.2f}".format(float(x["quote"]["USD"]["price"])))
          #print("Profit Loss Per Coin: ${0:.0f}".format(profit_loss_per_coin))
          #print("Rank: {0:.0f}".format(float(x["cmc_rank"])))
          #print("Total Paid: ${0:.0f}".format(total_paid))
          #print("Current Value: ${0:.0f}".format(Current_Value))
          #print("Profit Loss: ${0:.0f}".format(profit_loss))

          #h = Label(root, text= header, bg="white", font= "Verdona 8 bold")
          #h.grid(row=0, column=row_count, sticky=N+S+E+W)
          
          name = Label(root, text=x["name"], bg="white", font= "Verdona 8 bold")
          name.grid(row=row_count, column=0, sticky=N+S+E+W)
          
          rank = Label(root, text=x["cmc_rank"], bg="silver", font= "Verdona 8 bold")
          rank.grid(row=row_count, column=1, sticky=N+S+E+W)

          current_price = Label(root, text="${0:.2f}".format(float(x["quote"]["USD"]["price"])), bg="white")
          current_price.grid(row=row_count, column=2, sticky=N+S+E+W)

          price_paid = Label(root, text="${0:.0f}".format(total_paid), bg="silver", font= "Verdona 8 bold")
          price_paid.grid(row=row_count, column=3, sticky=N+S+E+W)

          Profit_Loss_Per = Label(root, text="${0:.0f}".format(float(profit_loss_per_coin)), bg="white", fg= red_green(float(profit_loss_per_coin)))
          Profit_Loss_Per.grid(row=row_count, column=4, sticky=N+S+E+W)

          one_hr_change = Label(root, text="${0:.2f}".format(float(x["quote"]["USD"]["percent_change_1h"])), bg="silver", fg= red_green(float(x["quote"]["USD"]["percent_change_1h"])))
          one_hr_change.grid(row=row_count, column=5, sticky=N+S+E+W)

          two_four_hr_change = Label(root, text="${0:.2f}".format(float(x["quote"]["USD"]["percent_change_24h"])), bg="white", fg= red_green(float(x["quote"]["USD"]["percent_change_24h"])))
          two_four_hr_change.grid(row=row_count, column=6, sticky=N+S+E+W)

          seven_day_change = Label(root, text="${0:.2f}".format(float(x["quote"]["USD"]["percent_change_7d"])), bg="silver", fg= red_green(float(x["quote"]["USD"]["percent_change_7d"])))
          seven_day_change.grid(row=row_count, column=7, sticky=N+S+E+W)

          current_value = Label(root, text="${0:.0f}".format(Current_Value), bg="white", fg= red_green(float(Current_Value)))
          current_value.grid(row=row_count, column=8, sticky=N+S+E+W)

          profit_loss_total = Label(root, text="${0:.0f}".format(profit_loss), bg="silver", fg= red_green(float(profit_loss)))
          profit_loss_total.grid(row=row_count, column=9, sticky=N+S+E+W)

          row_count += 1

    total_header = Label(root, text="Total:", bg="white", font= "Verdona 8 bold")
    total_header.grid(row=10, column=0, sticky=N+S+E+W)

    total_one_hr_chng = Label(root, text="${0:.0f}".format(total_onehr_chng), bg="white", fg= red_green(float(total_onehr_chng)))
    total_one_hr_chng.grid(row=10, column=5, sticky=N+S+E+W, padx=5)      

    total_tf_hr_chng = Label(root, text="${0:.0f}".format(total_tfhr_chng), bg="white", fg= red_green(float(total_tfhr_chng)))
    total_tf_hr_chng.grid(row=10, column=6, sticky=N+S+E+W, padx=5)

    Total_seven_day_change = Label(root, text="${0:.2f}".format(total_7d_chng), bg="white", fg= red_green(float(total_7d_chng)))
    Total_seven_day_change.grid(row=10, column=7, sticky=N+S+E+W, padx=5)      

    total_profitloss_per_coin = Label(root, text="${0:.0f}".format(total_profit_loss_per_coin), bg="white", fg= red_green(float(total_profit_loss_per_coin)))
    total_profitloss_per_coin.grid(row=10, column=4, sticky=N+S+E+W, padx=5)

    portfolio_profit = Label(root, text="${0:.0f}".format(portfolio_profit_loss), bg="white", fg= red_green(float(portfolio_profit_loss)))
    portfolio_profit.grid(row=10, column=9, sticky=N+S+E+W, padx=5)

    total_current = Label(root, text="${0:.0f}".format(total_current_value), bg="white", fg= red_green(float(total_current_value)))
    total_current.grid(row=10, column=8, sticky=N+S+E+W, padx=5)

    api= ""
    update_button = Button(root, text ="Update Prices", bg="lightskyblue", command = lookup, font= "Verdona 8 bold")
    update_button.grid(row=row_count, column=10, sticky=N+E+W)

# This creates the graph function and call into it the labels and size 
 
    def graph(labels, size):
      labels = pie
      sizes = pie_size
      colors = ["yellowgreen", "gold", "lightskyblue", "lightcoral", "red"]
      patches, texts = plt.pie(sizes, colors= colors, shadow = True, startangle= 90)
      plt.legend(patches, labels, loc = "best")
      plt.axis("equal")
      plt.tight_layout()
      plt.show()
#This will create the button that calls the graph function.
## The row_count is added to tggle through the different data in the rows when filling the graph
    graph_button = Button(root, text = "Pie Chart",bg="lightskyblue", command = lambda: graph(pie, pie_size), font= "Verdona 8 bold")
    graph_button.grid(row=row_count, column=11, sticky=S+E+W)

##These Exceptions are raised to limit the maxtime of running a command or calling a function.
  except (ConnectionError, Timeout, TooManyRedirects) as e:
    print(e)


lookup()


root.mainloop()

#The following code was for an outdated link from 2018 and no longer works
#api_request = request.get(" https://pro-api.coinmarketcap.com/v1/key/info ")
#api = json.loads(api_request.content) 