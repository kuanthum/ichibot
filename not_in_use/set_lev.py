
from api_pybit import session

sym = "CROUSDT"

def set_margin(sym):
    session.cross_isolated_margin_switch(
    symbol=sym,
    is_isolated=False,
    buy_leverage=5,
    sell_leverage=5
)

set_margin(sym)

def set_lev(sym):
    session.set_leverage(
        symbol=sym,
        buy_leverage=5,
        sell_leverage=5
)

set_lev(sym)