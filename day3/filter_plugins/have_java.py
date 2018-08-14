#!/bin/python

class FilterModule(object):
    def filters(self):
        return {
            'have_java': self.have_java
        }

    def have_java(self, version):
        return version in have_java
