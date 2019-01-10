# tunneler
Simple python script for SSH tunneling (linux only)

## Intro

This script is useful for setting up a ssh tunnel to a remote machine, e.g., where you run a jupyter notebook.

## Usage

```
usage: tunnel.py [-h] [--port PORT] [-u U] ip

positional arguments:
  ip                    ip address or a text file with the ip address

optional arguments:
  -h, --help            show this help message and exit
  --port PORT, -p PORT  port number to tunnel
  -u U                  username
```

### IP text file

The IP text file is a simple file with the IP at the first line.
