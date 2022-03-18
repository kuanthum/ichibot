from pybit import WebSocket
subs = [
    "position"
]
ws = WebSocket(
    "wss://stream-testnet.bybit.com/realtime_private",
    subscriptions=subs,
    api_key="WJYwnYE2Qv6XUrEMwW", api_secret="AVR49x1rNyn98xMdqjtXxl5jWtxROnSlpZs2"
)
while True:
    data = ws.fetch(subs[0])
    if data:
        print(data)
