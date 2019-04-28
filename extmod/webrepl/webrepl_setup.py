import sys

# import uos as os
import os
import machine
import webrepl
from config import config


def input_choice(prompt, choices):
    while 1:
        resp = input(prompt)
        if resp in choices:
            return resp


def getpass(prompt):
    return input(prompt)


def input_pass():
    while 1:
        passwd1 = getpass("New password (4-127 chars): ")
        if len(passwd1) < 4 or len(passwd1) > 127:
            print("Invalid password length")
            continue
        passwd2 = getpass("Confirm password: ")
        if passwd1 == passwd2:
            return passwd1
        print("Passwords do not match")

def get_daemon_status():
    cfg = config('webrepl')
    return cfg['enabled']

def change_daemon(boot):
    cfg = config('webrepl')
    cfg['enabled'] = boot
    config('webrepl', cfg)

def main():
    status = get_daemon_status()

    print("WebREPL daemon auto-start status:", "enabled" if status else "disabled")
    print("\nWould you like to (E)nable or (D)isable it running on boot?")
    print("(Empty line to quit)")
    resp = input("> ").upper()

    cfg = config('webrepl')
    if resp == "E":
        if cfg.get('password'):
            resp2 = input_choice("Would you like to change WebREPL password? (y/n) ", ("y", "n", ""))
        else:
            print("To enable WebREPL, you must set password for it")
            resp2 = "y"

        if resp2 == "y":
            passwd = input_pass()
            cfg['password'] = passwd
            config('webrepl', cfg)

    change_daemon(resp == "E")

    if resp == "E":
        webrepl.start()


main()
