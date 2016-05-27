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


ws = create_connection("wss://ws-feed.gdax.com")

ws.send(json.dumps({
    "type": "subscribe",
    "product_id": "BTC-USD"
}))

ws.send(json.dumps({
    "type": "heartbeat",
    "on": True
}))


while True:
    result = ws.recv()
    result = json.loads(result)
    print ("Received '%s'" % result)

ws.close()