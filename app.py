#!/usr/bin/env python
# coding: utf-8

dictionary = {
    "test":"test"
}
print("This container will error!")

fail = dictionary["not_test"]["this_doesnt_exist"]

print("This will not print :(")