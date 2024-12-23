#%%
from threading import Timer
from datetime import datetime

class RepeatTimer(Timer):
    def run(self):
        # self.function(*self.args, **self.kwargs)
        while not self.finished.wait(self.interval):
            self.function(*self.args, **self.kwargs)

def batch_order():
    print(f"order time {datetime.now()}")

batch_order_timer = RepeatTimer(3, batch_order)


#%%
def batch_trial_calculate(batch_num, order_num):
    b_order_num = None
    b_remain_num = None
    b_order_num = order_num//(batch_num)
    b_remain_num = order_num%(batch_num)

    if b_remain_num==0:
        return b_order_num, batch_num, 0, 0
    else:
        return b_order_num+1, b_remain_num, b_order_num, batch_num-b_remain_num

batch_num = 3
order_num = 10
b_up_num, b_up_times, b_low_num, b_low_times = batch_trial_calculate(batch_num, order_num)

print(f"共{batch_num}批，分{b_up_times}批{b_up_num}張，{b_low_times}批{b_low_num}張")

order_array = [b_up_num]*b_up_times
order_array.extend([b_low_num]*b_low_times)
print(f"order array: {order_array}")
