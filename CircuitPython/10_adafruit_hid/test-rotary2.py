import rotaryio
import board
#import time

encoder = rotaryio.IncrementalEncoder(board.GP18, board.GP19)
last_position = encoder.position

while True:
    position = encoder.position
    position_change = position - last_position

    if position_change > 0:
        print("==>", position_change)
    elif position_change < 0:
        print("<==", position_change)

    last_position = position

    #time.sleep(0.02)