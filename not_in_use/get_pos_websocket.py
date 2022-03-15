import hmac
import json
import time
import websocket

ws_url = "wss://stream-testnet.bybit.com/realtime_private"

api_key = "WJYwnYE2Qv6XUrEMwW"
api_secret = "AVR49x1rNyn98xMdqjtXxl5jWtxROnSlpZs2"

#Generate expires.
expires = int((time.time()+1)*1000)

#Generate signature.
signature = str(hmac.new(
    bytes(api_secret, "utf-8"),
    bytes(f"GET/realtime{expires}", "utf-8"), digestmod = "sha256"
).hexdigest())

param = "api_key={api_key}&expires={expires}&signature={signature}".format(
    api_key=api_key,
    expires=expires,
    signature=signature
)

url = ws_url + "?" + param

ws = websocket.WebSocketApp(
    url=url
)

#Authenticate with API.
ws.send(
    json.dumps({
        "op":"auth",
        "args": [api_key, expires, signature]
    })
)

subs = [
    "position"
]

while True:
    data = ws.fetch(subs[0])
    if data:
        print(data)