class Queue:
    def __init__(self):
        self.patients =[]
    def enqueue(self, patient):
        self.patients.append(patient)
        print(f"{patient['name']} is now currently waiting...")
    def dequeue(self):
        if self.is_empty():
            print("=== No Patients in Line ===")
            return None
        patient = self.patients.pop(0)
        print(f"=== Currently Serving Patient: {patient['name']} ===")
        return patient
    def peek(self):
        if self.is_empty():
            print("=== No Patients in Line ===")
            return None
        return self.patients[0]
    def is_empty(self):
        return len(self.patients) == 0
    def size (self):
        return len(self.patients)
    def display(self):
        if self.is_empty():
            print("===Queue is Empty ===")
            return
        print("=== Current Queue ===")
        for i, patient in enumerate(self.patients, 1):
            print(f" [{i}] {patient['name']} | Age: {patient['age']} | Concern: {patient['concern']}")

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

"""Kindly continue for the next members in  BRANCH: VERSION-ONE"""
