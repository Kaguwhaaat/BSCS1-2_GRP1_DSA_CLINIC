class Queue:
    def __init__(self):
        self.patients =[]

"""Pertains to each link in LinkedList"""
class Node:
    def __init__(self, patient):
        self.patient = patient
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

"""To define a single node in BST"""
class BSTNode:
    def __init__(self, patient):
        self.patient = patient
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

"""Kindly continue for the next members in  BRANCH: CODE-TEST"""