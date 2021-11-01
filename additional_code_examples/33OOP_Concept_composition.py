# What is difference between inheritance and composition?
# Inheritance and composition are two programming techniques developers use to establish relationships between 
# classes and objects. Whereas inheritance derives one class from another, composition defines a class as the 
# sum of its parts.

#Note:Always initialize mutable attributes in the constructor

class Rpository:
    def __init__(self):
        self.package={}

    def add_package(self,package):
        self.packages[package.name]=package

    def total_size(self):
        result=0
        for package in self.package.values():
            result += package.size
        return result

#Objects can be contained inside each other using composition 