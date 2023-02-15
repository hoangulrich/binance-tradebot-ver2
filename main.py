#! /usr/bin/python3
from input import *
from binanceAPI.wsocket import *
from module.newMarketOrder import *

def main():
    ask_input()
    run_stream()
    
if __name__ == "__main__":
    main()