import rotaryio
import board

encoder = rotaryio.IncrementalEncoder(board.GP18, board.GP19)
last_position = encoder.position
while True:
    position = encoder.position
    if last_position is None or position != last_position:
        print(position)
    last_position = position