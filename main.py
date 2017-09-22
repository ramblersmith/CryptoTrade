import krakenex

import pprint

k = krakenex.API()

response = k.query_public('Depth', {'pair': 'XXBTZUSD', 'count': '10'})
pprint.pprint(response)

# Get the data into an array and write to DB

# Get the exchange prices every minute

import sched, time
s = sched.scheduler(time.time, time.sleep)
def do_something(sc):
    print "Doing stuff..."
    # do your stuff
    s.enter(60, 1, do_something, (sc,))

s.enter(60, 1, do_something, (s,))
s.run()