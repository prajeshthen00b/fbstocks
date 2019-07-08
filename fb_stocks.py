import pandas as pd
import numpy as np
from scipy.stats import norm 
import matplotlib.pyplot as plt

fb = pd.read_csv(r"C:\Users\user\Desktop\Projects\FB_data.csv") #or any damn path on your system

def LogRet(h): #Sets up the logarithmic column in the DF
    cur = np.log(h['close'])
    future = np.log(h['close']).shift(-1)  #shifts the column one step UPWARD  
    h['Logarithmic Return'] = future - cur
    h1 = h.dropna(how = 'any')    #returns a new data frame with dropped NAN
    global mu, sd, muy, sdy
    mu = h1['Logarithmic Return'].mean() #mean and standard deviation calcualted
    sd = h1['Logarithmic Return'].std(ddof = 1) #divides by n-1 instead of n
    muy = 220*mu
    sdy = (220**0.5)*sd            #for yearly parameters
    
def dist(h):
    graph = pd.DataFrame()
    graph['x'] = np.arange(h['Logarithmic Return'].min() - 0.2, h['Logarithmic Return'].max(), 0.001)
    graph['y'] = norm.pdf(graph['x'], mu, sd) 
    plt.plot(graph['x'], graph['y'], color = 'red')
    plt.show()
    h['Logarithmic Return'].hist()
    
def predict(h, typ, chg):
    if typ == '1':
        r =  chg*0.01
        prob = 1 - norm.cdf(r, muy, sdy) #calculates prob up to point r
        print("Hey",n,"! The probability of the stock price rising by",chg,"% this year is",prob*100,"%!")
    elif typ == '2':
        r = chg*0.01
        prob = norm.cdf(-r, muy, sdy)
        print("Hey",n,"! The probability of the stock price falling by",chg,"% this year is",prob*100,"%!")
        
## MAIN PROGRAM ##
        
def main(name):
    LogRet(fb)
    print("Hello ", name,"!",end =' ')
    print("Welcome to the yearly FB stock price rise/fall predictor!")
    typ = input("What are you looking at?\nPress 1 for Rise\nPress 2 for Fall")
    chg = int(input("How much of a rise/fall are you looking for? For e.g.: 5%/10%/15%... and so on.\nEnter ONLY THE NUMBER WITHOUT PERCENTAGE SYMBOL:"))
    predict(fb, typ, chg)
    g = input("Would you like to graphically visualize the stock prices?\n1. Yes\n2. No")
    if g=='1':
        dist(fb)
    else:
        print("Thank you for using this predictor! Goodbye!")
        
n = input("Enter your name:")
main(n)
    

    
    

    
    
    
    
        
        

    
        
        






