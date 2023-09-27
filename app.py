#!/usr/bin/python3
# coding: utf-8
from utilites import(
    get_args
)

def main():
    args = get_args()
    
    if args.fail:
        dictionary = {
            "test":"test"
        }
        print("This container will now error!")

        failure = dictionary["not_test"]["this_doesnt_exist"]

        print(f"This will not print: {failure}")
    
    print(args.input)
    
    if args.double:
        print(args.input)

if __name__ == "__main__":
    main()
