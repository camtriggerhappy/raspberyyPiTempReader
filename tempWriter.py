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
        self.mode = 0o600  # FIFO
        self.DHTSensor = adafruit_dht.DHT11(board.D14)

    try:
        os.mkfifo(path, mode)


    except FileExistsError:
        print("file is already there")

    def writeToPipe(self):
        file = open(path, "w+")
        file.write(self.getTemp)
        file.close()

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

def main():
    while 1:
        print("in the loop")
        writer.writeToPipe()
        time.sleep(5)

if __name__ == '__main__':
    main()

