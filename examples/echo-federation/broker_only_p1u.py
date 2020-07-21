import helics as h
from math import pi
import random
import time
import sys

initstring = "-f 2 --ipv4 --loglevel=7"
#str(len(feeders)+1)
#fedinitstring = "--broker=federate_broker --federates=1"
deltat = 0.01

helicsversion = h.helicsGetVersion()

print("broker: Helics version = {}".format(helicsversion))

# Create broker #
print("Creating Broker")
broker = h.helicsCreateBroker("zmq", "", initstring)
print("Created Broker")

print("Checking if Broker is connected")
isconnected = h.helicsBrokerIsConnected(broker)
print("Checked if Broker is connected: {}".format(isconnected))

time.sleep(10)

# this federate has finished, but don't finalize until all have finished
iters = 0
#max_iters = 60*300 # don't wait more than half an hour for all other federates to finalize and write
while h.helicsBrokerIsConnected(broker)==1:# and iters<max_iters:
    time.sleep(1)
    iters += 1

h.helicsCloseLibrary()
print("library closed")

#Test Change for branch
