from datetime import datetime
import matplotlib.pyplot as pyplot
import RPi.GPIO as GPIO

RECORDING_DURATION = 4
RECEIVE_PIN = 23

if __name__ == '__main__':
    signals = [[], []]  # [[time of reading], [signal reading]]
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(RECEIVE_PIN, GPIO.IN)
    cumulative_time = 0
    beginning_time = datetime.now()
    print('** Started recording **')
    psec = 0
    while cumulative_time < RECORDING_DURATION:
        if cumulative_time > psec:
            psec = cumulative_time
        time_delta = datetime.now() - beginning_time
        signals[0].append(time_delta)
        signals[1].append(GPIO.input(RECEIVE_PIN))
        cumulative_time = time_delta.seconds
    print('** Ended recording **')
    GPIO.cleanup()

    print('** Processing results **')
    for i in range(len(signals[0])):
        signals[0][i] = signals[0][i].seconds + \
            signals[0][i].microseconds/1000000.0

    print('** Plotting results **')
    pyplot.plot(signals[0], signals[1])
    pyplot.axis([0, RECORDING_DURATION, -1, 2])
    pyplot.show()
