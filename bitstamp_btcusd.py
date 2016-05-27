"""
Task:
Descripion of script here.
"""
# Import Built-Ins
import sys
import time

# Import Third-Party
import pusherclient

# Import Homebrew



# Add a logging handler so we can see the raw communication data
import logging
root = logging.getLogger()
root.setLevel(logging.INFO)
ch = logging.StreamHandler(sys.stdout)
root.addHandler(ch)

global pusher

# We can't subscribe until we've connected, so we use a callback handler
# to subscribe when able
def connect_handler_BTCUSD(data):
    channel = pusher.subscribe('order_book')
    channel.bind('trade', callback)


pusher = pusherclient.Pusher('de504dc5763aeef9ff52')
pusher.connection.bind('pusher:connection_established', connect_handler_BTCUSD)
pusher.connect()

while True:
    # Do other things in the meantime here...
    time.sleep(1)

