from rotary import Rotary
import time


# parameter order is Pin0, Pin1, Pin2 ---> dt, clk, sw 
from board import GP0, GP1, GP2
rotary = Rotary(GP0, GP1, GP2)
print("Starting")

val = 0

def rotary_changed(change):
    global val
    if change == Rotary.ROT_CW:
        val += 1
        print(val)
    elif change == Rotary.ROT_CCW:
        val -= 1
        print(val)
    elif change == Rotary.SW_PRESS:
        print('PRESSED')
    elif change == Rotary.SW_RELEASE:
        print('RELEASED')

try:
    rotary.add_handler(rotary_changed)
except RuntimeError:
    pass

while True:
    time.sleep(0.1)
    
