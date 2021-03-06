import os
import time

import board
import asyncio
import adafruit_dht

path = "/home/cameron/pipe/tempPipe"
mode = 0o600  # FIFO


class DHTWriter():
    def __init__(self):
        self.path = "/home/cameron/pipe/tempPipe"
        self.DHTSensor = adafruit_dht.DHT11(board.D2)

    def writeToPipe(self):
        file = open(self.path, "w")
        file.write(str(self.getTemp()))
        file.close()

    def getTemp(self):
        try:
            print(self.DHTSensor.temperature)
            return (self.DHTSensor.temperature) # convert to Fahrenheit
        except RuntimeError as error:
            # Errors happen fairly often, DHT's are hard to read, just keep going
            print(error.args[0])
        except Exception as error:
            self.DHTSensor.exit()
            raise error


writer = DHTWriter()
while 1:
    print("in the loop")
    writer.writeToPipe()
    time.sleep(1)



if __name__ == '__main__':
    main()

