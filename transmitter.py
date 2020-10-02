import time
import sys
import RPi.GPIO as GPIO

NUM_ATTEMPTS = 12
TRANSMIT_PIN = 23

KNOWN_CODES = {
    "example": "11010000110110100000110011000001101010101",
}

TIMINGS = {
    'attempts_gap': 0.008,   # time to wait between attempts
    'first_on': 0.00491,     # initial extended signal time
    'first_gap': 0.001636,   # gap between initial signal to next digit
    'long_on': 0.000545,     # long signal time (i.e. digit 1)
    'long_gap': 0.000454,    # time between long signal to the next digit
    'short_on': 0.000272,    # short signal time (i.e. digit 0)
    'short_gap': 0.0008636,  # time between short signal to the next digit
}


def transmit(codes):
    '''
    Transmits all codes received, assuming: 
    - each code starts with an extended init signal (`first_on` and `first_gap`)
    - long on  + short gap = 1
    - short on + long gap  = 0
    '''
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(TRANSMIT_PIN, GPIO.OUT)
    for code_name in codes:
        code = KNOWN_CODES[code_name]
        for t in range(NUM_ATTEMPTS):
            print('#' + str(t) + ' attempt for "' + code '"')
            GPIO.output(TRANSMIT_PIN, 1)
            time.sleep(TIMINGS['first_on'])
            GPIO.output(TRANSMIT_PIN, 0)
            time.sleep(TIMINGS['first_gap'])
            for i in code:
                if i == '0':
                    GPIO.output(TRANSMIT_PIN, 1)
                    time.sleep(TIMINGS['short_on'])
                    GPIO.output(TRANSMIT_PIN, 0)
                    time.sleep(TIMINGS['short_gap'])
                elif i == '1':
                    GPIO.output(TRANSMIT_PIN, 1)
                    time.sleep(TIMINGS['long_on'])
                    GPIO.output(TRANSMIT_PIN, 0)
                    time.sleep(TIMINGS['long_gap'])
                else:
                    continue
            GPIO.output(TRANSMIT_PIN, 0)
            time.sleep(TIMINGS['attempts_gap'])
    GPIO.cleanup()


if __name__ == '__main__':
    # Receive codes to run as cmd args: `python transmitter.py example`
    codes_to_send = sys.argv[1:]
    if codes_to_send:
        transmit(codes_to_send)
