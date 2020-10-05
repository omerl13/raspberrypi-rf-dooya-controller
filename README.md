# raspberrypi-rf-dooya-controller
Remote control for Dooya RF curtains using RaspberryPi

## Requierments
- A RaspberryPi
- A 433MHz transmitter and receiver modules
- Jumpers wires to connect the transmitter and receiver to the RaspberryPi

## Recording RF Signals
The `receicer.py` module is used to record RF signals from the remote control, in order to reuse it later
- Requires pyplot (`sudo apt-get install python-matplotlib`)

### Translating the Data:
- The receiver code samples the physical receiver for a configured period of time (`RECORDING_DURATION`, in seconds).
- Both the reciever and the transmitter are using GPIO pin 23, this arbitrary choice can be changed and it migth be helpful to use different pin for each module for testing both components together.
- After finished sampling, a plot will be created, in which the signals transmitted are shown.
- Each code starts with a long signal, and after it 40 shorter signals
 - Long `on` and short `off` will be translated to `1`
 - Short `on` and long `off` will be translated to `0`
- Each code will be repeated several times (to ensure the product will success recognizing it)
- The last 8 digits of the code are specifiying the action:
 - `00011110` = Up
 - `00110011` = Down
 - `01010101` = Stop
- In the DC2702 RC, the 4 digits before the action (digits 29-32) denoting the selected channel number on the RC (e.g.: `0001` for 1, `0010` for 2)
- Code example: `11010000110110100000110011000001101010101` - will trigger `Stop` on channel `6` (so it is enough to record one signal from the original RC in order to recreate everything)

## Transmitting RF Signals
Transmitting the RF recorded signals is acheived by the `transmitter.py` module.
- `transmitter.py` can be tested by passing in CLI by passing the required codes as arguments (e.g. `python transmitter.py example`)
- Timings provided were measured by using the `reciever.py` module, and can be changed for different use cases
- Both the reciever and the transmitter are using GPIO pin 23, this arbitrary choice can be changed and it migth be helpful to use different pin for each module for testing both components together.
- Available codes are on the `KNOWN_CODES` dictionary
- Each code will be transmitted multiple time (as much as set in `NUM_ATTEMPTS`)

## Web Server
Notes: 
- Set the server URL in `templates/index.html` and `templates/multi.html` (default to `127.0.0.1`)
- Triggering multiple requests fast will cause some errors, due to the lack of synchronization mechanism

### UI
There are 2 HTML pages available:
1. `templates/index.html` (route: `/`) - this page provides a simple UI, similar to Dooya DC2700 Remote Control
2. `templates/multi.html` (route: `/multi`) - this page provides a similar UI, with an addidion of select component to support multi-channels, similar to Dooya DC2702 Remote Control
- It is possible to use `multi.html` page as a single RC for multiple products

### API
- `/ctrl?name={name}` - used to trigger the transmitter to transmit the requested code using the `name` query parameter