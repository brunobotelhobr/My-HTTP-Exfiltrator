#!/usr/bin/python
############################################################
# Requirements:
# pip install termcolor
############################################################

from http.server import BaseHTTPRequestHandler, HTTPServer
from termcolor import colored
import requests
import datetime
import argparse
import os
import time
import logging
import base64
import urllib.parse

# Disable scapy warning output
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)

NAME = "HTTP GET Server"
VERSION = "1.0"
DATE = "02/06/2024"


def parse_arguments():
    """Parse and return arguments from the command line."""
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-w",
        "--write-file",
        action="store",
        dest="write_file",
        required=True,
        help="File to write the HTTP Get.",
    )
    parser.add_argument(
        "-l",
        "--listener_address",
        action="store",
        dest="listener_address",
        required=True,
        help="Listener Address.",
    )
    parser.add_argument(
        "-p",
        "--port",
        action="store",
        dest="port",
        required=True,
        help="Listener Port.",
    )
    return parser.parse_args()


def print_banner():
    """Print the banner."""
    print("")
    print(f"### {NAME}")
    print(f"### Version {VERSION}")
    print(f"### Date {DATE}")
    print("### by Bruno Botelho - bruno.botelho.br@gmail.com")
    print("")


def write(j):
    """Write the HTTP Get to a file."""
    file = open(parse_arguments().write_file, "a", encoding="utf-8")
    file.write(j)
    file.close()


def log_timestamp():
    """Return the current timestamp."""
    return datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")


class StoreHandler(BaseHTTPRequestHandler):
    """Store Handler Class."""

    def log_message(self, format, *args):
        """This method will prevent any request from being logged."""
        pass

    def do_GET(self):
        """Handle the GET request."""
        try:
            parameters = self.path.split("?")
            binary_string = str(parameters[1])
            binary_string = binary_string[2:]
            byte_array = [
                binary_string[i : i + 8] for i in range(0, len(binary_string), 8)
            ]
            text = "".join([chr(int(byte, 2)) for byte in byte_array])
            payload_vetor = text.split("&&")
            index_c = payload_vetor[0]
            print(
                log_timestamp()
                + " Received: "
                + " Get "
                + "http://"
                + self.client_address[0]
                + "/sys?p="
                + colored(binary_string, "red")
                + " > "
                + colored(str(text).rstrip("\n"), "yellow")
                + " > "
                + colored(index_c, "green")
            )
            write(payload_vetor[0])
            self.send_response(code=200, message="OK")
            self.flush_headers()
        except Exception as e:
            print(log_timestamp() + " Error: " + str(e))
            self.send_response(500)
            self.flush_headers()


def main():
    """Main function."""
    args = parse_arguments()
    print_banner()

    print("### Starting HTTP Server Monitoring")
    print("### Listener Address: " + args.listener_address)
    print("### Listener Port: " + args.port)
    print("### File to Write: " + args.write_file)
    print("")

    server = HTTPServer((args.listener_address, int(args.port)), StoreHandler)
    server.serve_forever()


if __name__ == "__main__":
    main()
