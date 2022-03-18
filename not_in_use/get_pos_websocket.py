import hmac
import json
import time
import websocket

ws_url = "wss://stream-testnet.bybit.com/realtime_private"

api_key = "WJYwnYE2Qv6XUrEMwW"
api_secret = "AVR49x1rNyn98xMdqjtXxl5jWtxROnSlpZs2"

#Generate expires.
expires = int((time.time()+50*60)*1000)
print(expires)

#Generate signature.
signature = str(hmac.new(
    bytes(api_secret, "utf-8"),
    bytes(f"GET/realtime{expires}", "utf-8"), digestmod = "sha256"
).hexdigest())

subs = [
    "position"
]

param = "api_key={api_key}&expires={expires}&signature={signature}&subscriptions={subs}".format(
    api_key=api_key,
    expires=expires,
    signature=signature,
    subscriptions=subs
)

url = ws_url + "?" + param

ws = websocket.WebSocketApp(
    url=url
)

while True:
    data = ws.fetch(subs[0])
    if data:
        print(data)
