#!/bin/python

class FilterModule(object):
    def filters(self):
        return {
            'detect': self.detect
        }

    def detect(self, value, name):
        data = [] 
        for item in value:
            if item['name'] == name:
                data.append(item)  
        return data
