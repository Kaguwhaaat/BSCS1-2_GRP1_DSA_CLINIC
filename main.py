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
        print(f"   Patient: {patient['name']}")
        print(f"   Age   : {patient['age']}")
        print(f"   Reason: {patient['reason']}")
        return patient
    def peek(self):
        
        if self.is_empty():
            return None
        else:
            print(f"\n=== Next Patient: {self.patients[0]['name']} ===")
        
        return self.patients[0]
    def is_empty(self):
        return len(self.patients) == 0
    def size(self):
        return len(self.patients)
    def to_list(self):
        return self.patients.copy()
    

q = Queue()

print("=" * 30 + "\nCLINIC ADMINISTRATOR SYSTEM\n" + "=" * 30)

while True:
    #Clinic Administrator System Menu
    print("\n[1] Patient Registration")
    print("[2] Serve Patients")
    print("[3] Exit")
    choice = input("Enter Function: ").strip()

    if choice == '1':
        #Patient Registration
        print("\n=== Patient Registration ===")
        name = input("Enter Patient Name: ").strip()
        age = input("Enter Patient Age: ").strip()
        reason = input("Enter Reason for Visit: ").strip()

        #Error handling for empty name and non-numeric age
        if not name:
            print("Name cannot be empty. Please try again.")
            continue

        if not age.isdigit():
            print("Invalid age. Please enter a number.")
            continue

        #Enqueue the patient to the queue
        q.enqueue({'name': name, 'age': int(age), 'reason': reason})

        #Display the current queue of patients
        print("\nCurrent Queue:")
        for number, patient in enumerate(q.to_list(), start=1):
            print(f"   [{number}] {patient['name']}")
        
    elif choice == '2':
         #Error handling for empty queue
         if q.is_empty():
            print("\n=== No Patients to Serve ===")
            continue
         else:
            #Serve Patients
            patient_number = 1
            while not q.is_empty():
                q.peek()
                print(f"   Patient number: {patient_number}")
                q.dequeue()
                print(f"\n   Remaining Patients: {q.size()}")
                patient_number += 1

         print("\nThere are no more patients\n")
        
        
    elif choice == '3':
        #Exit the system
        while True:
            #Ensure that the user wants to exit
            confirm_exit = input("Are you sure you want to exit? (Y/N): ").strip().upper()
            if confirm_exit == 'Y':
                 break
            elif confirm_exit == 'N':
                break
            else:
                #Invalid input handling for exit confirmation
                print("Invalid input. Please enter 'Y' or 'N'.")
        if confirm_exit == 'Y':
            print("\nThank you for using the Clinic Administrator System!")
        break
    else:
        #Invalid choice handling
        print("\nInvalid choice. Please try again.")
    

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