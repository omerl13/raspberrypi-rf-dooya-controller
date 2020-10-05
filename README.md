# raspberrypi-rf-dooya-controller
Remote control for Dooya RF curtains using RaspberryPi

## Web Server
Notes: 
- Set the server URL in `templates/index.html` and `templates/multi.html` (default to `127.0.0.1`)

### UI
There are 2 HTML pages available:
1. `templates/index.html` (route: `/`) - this page provides a simple UI, similar to Dooya DC2700 Remote Control
2. `templates/multi.html` (route: `/multi`) - this page provides a similar UI, with an addidion of select component to support multi-channels, similar to Dooya DC2702 Remote Control
- It is possible to use `multi.html` page as a single RC for multiple products

