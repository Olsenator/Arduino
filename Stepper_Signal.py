import pyfirmata
import time
import os


board = pyfirmata.Arduino('/dev/ttyACM0')

it = pyfirmata.util.Iterator(board)

''' Setup-Part'''
LEDPin= board.get_pin('d:4:o')
dirPin= board.get_pin('d:2:o')
stepPin= board.get_pin('d:3:o')
enPin= board.get_pin('d:7:o')
Steps_in_Rev = 200

''' LOOP PART'''
it.start()

while True:
    enPin.write(0)
    dirPin.write(1)

    for i in range(200):

        stepPin.write(1)
        stepPin.write(0)

    LEDPin.write(1)

    time.sleep(0.5)
    stepPin.write(0)
    LEDPin.write(0)
    time.sleep(0.5)

