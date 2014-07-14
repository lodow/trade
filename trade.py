#!/usr/bin/python2.7 -u

import pprint
import sys

capital = 0
nbDays = 0
capitalization = []
stock = 0
slice = []
state = {"min" : False, "max" : False}

def buy(n, day):
    global capitalization, capital, stock

    if capital - (0.15 / 100 * capital) >= n * capitalization[day] and n > 0:
        print("buy " + str(n))
        stock += n
        capital -= n * capitalization[day]
        capital = capital - (0.15 / 100 * (n * capitalization[day]))
    else:
        print("wait")

def sell(n, day):
    global capitalization, capital, stock

    if stock >= n and n > 0:
        print("sell " + str(n))
        stock -= n
        capital += n * capitalization[day]
        capital = capital - (0.15 / 100 * (n * capitalization[day]))
    else:
        print("wait")

def algo(curDay):
    global capitalization, stock, slice, state
    i = 0

    if len(slice) <= curDay / 5:
        slice.append([])
    slice[curDay / 5].append(capitalization[curDay])
    if curDay < 25:
        print("wait")
    else:
        i = curDay / 5
        tmpmax = []
        tmpmin = []
        while i >= 0 and len(tmpmax) < 5:
            tmpmax.append(max(slice[i]))
            tmpmin.append(min(slice[i]))
            i -= 1
        moy_min = sum(tmpmin) / len(tmpmin)
        moy_max = sum(tmpmax) / len(tmpmax)

        if capitalization[curDay] > moy_min and state["min"] == True:
            sell(1, curDay)
        elif capitalization[curDay] < moy_max and state["max"] == True:
            buy(1, curDay)
        else:
            print("wait")

        if capitalization[curDay] < moy_min:
            state["min"] = True
        else:
            state["min"] = False

        if capitalization[curDay] > moy_max:
            state["max"] = True
        else:
            state["max"] = False

def startTrade():
    global nbDays, capitalization, stock
    i = 0
    while i < nbDays:
        line = sys.stdin.readline()
        capitalization.append(int(line))
        if i >= nbDays - 1:
            sell(stock, i)
        else:
            algo(i)
        i += 1

def setCapital():
    global capital, f
    line = sys.stdin.readline()
    capital = int(line)

def setNbDays():
    global nbDays, f
    line = sys.stdin.readline()
    nbDays = int(line)

def main():
    setCapital()
    setNbDays()
    startTrade()

if __name__ == "__main__":
    main()
