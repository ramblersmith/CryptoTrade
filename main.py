import krakenex
import json
import pprint
import numpy as np

if __name__ == "__main__":
    print("main")


'''
def get_kraken_data(self):

    print("kraken fucntion")

'''
k = krakenex.API()
records = 6

response = k.query_public('Depth', {'pair': 'XXBTZUSD', 'count': records})
# pprint.pprint(response)

data = json.dumps(response)
a = json.loads(data)
kraken_arr = np.array([])
tstamp = "now"
temp_arr = []

i = 0
while i < records:
    np.append(kraken_arr, i)
    temp_arr = (tstamp, "Kraken", a["result"]["XXBTZUSD"]["bids"][i][0], a["result"]["XXBTZUSD"]["bids"][i][1],
                      a["result"]["XXBTZUSD"]["asks"][i][0], a["result"]["XXBTZUSD"]["asks"][i][1])
    np.append(kraken_arr, temp_arr, axis=0)
    i += 1

pprint.pprint(kraken_arr[0])
# print(kraken_arr)

'''for k in a["result"]["XXBTZUSD"]:
    pprint.pprint("testing 123... ")
    print(k)
    pprint.pprint(a["result"]["XXBTZUSD"]["bids"][0])
    # pprint.pprint(k["bids"])
'''


# Get the data into an array and write to DB


# Get the exchange prices every minute
'''
import sched, time
s = sched.scheduler(time.time, time.sleep)
def do_something(sc):
    print "Doing stuff..."
    # do your stuff
    s.enter(60, 1, do_something, (sc,))

s.enter(60, 1, do_something, (s,))
s.run()

'''