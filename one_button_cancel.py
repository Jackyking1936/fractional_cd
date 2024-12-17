#%%
import pickle
from pathlib import Path

from fubon_neo.sdk import FubonSDK, Mode, Order
from fubon_neo.constant import TimeInForce, OrderType, PriceType, MarketType, BSAction

my_file = Path("./info.pkl")
if my_file.is_file():
    with open('info.pkl', 'rb') as f:
        user_info_dict = pickle.load(f)
    
sdk = FubonSDK()
accounts = sdk.login(user_info_dict['id'], user_info_dict['pwd'], user_info_dict['cert_path'])
active_acc = None
for acc in accounts.data:
    if acc.account == '9809789':
        active_acc = acc

if active_acc:
    print(active_acc)
else:
    raise("account not found")
# %%
order_results = sdk.stock.get_order_results(active_acc)
if order_results.is_success:
    print(f"{order_results.data}")
else:
    print(f"{order_results.message}")
# %%
for order_res in order_results.data:
    if order_res.status == 10 or order_res.status == 0:
        cancel_order = order_res
        cancel_res = sdk.stock.cancel_order(active_acc, cancel_order)
        if cancel_res.is_success:
            cancel_detail = cancel_res.data
            print(f"{cancel_detail.stock_no}, successfully canceled, market_type: {cancel_detail.market_type}, b4_qty: {cancel_detail.before_qty}, after_qty: {cancel_detail.after_qty}")
        else:
            print(f"cancel failed: {cancel_res.message}")
# %%
