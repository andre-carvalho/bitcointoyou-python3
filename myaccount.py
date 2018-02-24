import bitcointoyou
import postgresdb
import time


def app():
    api_key = ''
    api_pass = ''

    btc = bitcointoyou.API(api_key, api_pass)
    def getTicker():
        tick = btc.Ticker() 
        if tick is not None:
            db = postgresdb.bitcoinDAO()
            db.connect()
            db.insertData(tick)
            db.close()
        time.sleep(60)
    
    while True:
        getTicker()

if __name__ == "__main__":
    app()