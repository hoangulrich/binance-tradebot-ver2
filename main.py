#! /usr/bin/python3
import argparse
from input import *
from binanceAPI.wsocket import *
from module.newMarketOrder import *
from binanceAPI.teleBot import application

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--symbol", help = "Specify Symbol", required=False)
    args = vars(parser.parse_args())

    ask_input(args["symbol"])
    run_stream()
    

if __name__ == "__main__":
    main()