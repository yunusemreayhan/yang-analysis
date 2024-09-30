#!/usr/bin/env python3

import sys
import traceback
import xml.dom.minidom
from ncclient import manager
from ncclient.xml_ import to_ele

host = sys.argv[1]
port = 830
user = "admin_user"
password = "Ericsson1234"
ROW_LENGTH = 160


def print_formatted(string):
    try:
        print(xml.dom.minidom.parseString(string).toprettyxml())
    except Exception:
        print("Exception while printing xml dom")
        traceback.print_exc()
        print("Trying to print simplified version")
        print_simplified(string)


def print_simplified(string):
    row = ""
    index = 0
    if len(string) < ROW_LENGTH:
        print(string)
    else:
        for ch in string:
            if index < ROW_LENGTH:
                row += (ch)
                index += 1
            else:
                print(row)
                index = 0
                row = ""


def input_multiline():
    user_input = []
    while True:
        line = input()
        if line == "":  # If line is blank
            break
        else:
            user_input.append(line)
    user_input = '\n'.join(user_input)
    return user_input


def main():
    with manager.connect(host=host, port=port, username=user, password=password, hostkey_verify=False) as m:
        print("Successfully connected to host {}:{} as user {}".format(
            host, port, user))
        print("To quit the script type 'exit' to the input and press Enter twice.")
        while True:
            try:
                print("Paste the xml, then press Enter twice!")
                message = input_multiline()
                if message.lower() == "exit":
                    print('Exiting from script.')
                    break
                elif message == '':
                    continue
                response = m.dispatch(to_ele(message))
                print("----------------------------------\n    Response    \n")
                print_formatted(response.xml)
                print("\n    End of response    \n----------------------------------")
            except KeyboardInterrupt:
                print('Keyboard interruption, Exiting from script.')
                break
            except Exception:
                traceback.print_exc()
                continue


if __name__ == "__main__":
    main()
