import os
import time

import board
import adafruit_dht

path = "/home/cameron/pipe/tempPipe"
mode = 0o600  # FIFO

os.mkfifo(path, mode)


class DHTWriter():
    def __init__(self):
        path = "/home/cameron/pipe/tempPipe"
        mode = 0o600  # FIFO

        os.mkfifo(path, mode)
        self.DHTSensor = adafruit_dht.DHT11(board.D0)

    def writeToPipe(self):
        file = open(path, "w")
        file.write(self.getTemp)

    def getTemp(self):
        try:
            return self.DHTSensor.temperature * (9 / 5) + 32  # convert to Fahrenheit
        except RuntimeError as error:
            # Errors happen fairly often, DHT's are hard to read, just keep going
            print(error.args[0])
        except Exception as error:
            self.DHTSensor.exit()
            raise error


writer = DHTWriter()
while True:
    time.sleep(30)

    writer.writeToPipe()
