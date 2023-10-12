#!/usr/bin/env python3
# coding: utf-8
from utilites import(
    get_args,
    print_ls
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

    if args.list_dir:
        print_ls(args.input)


if __name__ == "__main__":
    main()
