"""
Task:
Descripion of script here.
"""

# Import Built-Ins
import logging
import json


# Import Third-Party
from websocket import create_connection
# Import Homebrew

# Init Logging Facilities
log = logging.getLogger(__name__)

subscriptions = {'ETHUSD': {"event": "subscribe",
                             "channel": "book",
                             "pair": "ETHUSD",
                             "prec": "P0"}}

ws = create_connection("wss://api2.bitfinex.com:3000/ws")

for subscription in subscriptions:
    ws.send(json.dumps(subscriptions[subscription]))

while True:
    result = ws.recv()
    result = json.loads(result)
    print(result)

ws.close()