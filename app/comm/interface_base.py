from abc import ABCMeta, abstractmethod
import json


class InterfaceBase:
    __metaclass__ = ABCMeta

    def __init__(self):
        self.rsp = {}

    def execute(self):
        self.parse_input()
        self.do_execute()
        self.set_output()
        return json.dumps(self.rsp)

    @abstractmethod
    def parse_input(self):
        print("parse_input")

    @abstractmethod
    def do_execute(self):
        print("do_execute")

    @abstractmethod
    def set_output(self):
        print("set_output")
