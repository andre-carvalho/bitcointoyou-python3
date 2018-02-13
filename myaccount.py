#!/usr/local/bin/python3
import sys
#sys.path.append('../libbty/')
import bitcointoyou

api_key = ''
api_pass = ''

btc = bitcointoyou.API(api_key, api_pass)

tick = btc.Ticker()

print(tick)
