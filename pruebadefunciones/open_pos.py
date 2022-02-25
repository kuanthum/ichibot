import get_data as gd
import pandas as pd

print("----Open position----")
print("")

quest = input("Do you want to open a position?")
longorshort = input("Select Long or Short position:")
sl = input("Do you want to set stop loss?")
tp = input("Do you want to set take profit?")
sl_input = input("Input stop loss %: ")
tp_input = input("Input take profit %: ")


def open_pos():
    if quest == "y":
        if longorshort == "l":
            return "Buy"
        elif longorshort == "s":
            return "Sell"
        else:
            return "Error"
    elif longorshort == "n":
        return "n"
    else:
        return "Error"

def set_sl_tp():
    if sl == "y":
        return sl_input
    elif tp == "y":
        return tp_input
    else:
        return "coninue"

if open_pos() == "Buy":
    print("Buy order open")
elif open_pos() == "Sell":
    print("Sell order open")


# market_order = (gd.session.place_active_order(
#     symbol="BTCUSDT",
#     side=open_pos(),
#     order_type="Market",
#     qty=0.002,
#     time_in_force="GoodTillCancel",
#     reduce_only = False,
#     close_on_trigger = False
# ))

# md_dataframe = pd.DataFrame(market_order)['result']
# print(md_dataframe)

