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
            print(f"\n=== Next in Line ===")
        
        return self.patients[0]
    def is_empty(self):
        return len(self.patients) == 0
    def size(self):
        return len(self.patients)
    def to_list(self):
        return self.patients.copy()
    
class Node:
    def __init__(self, patient):
        self.patient = patient
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def new_record(self, patient):
        newNode = Node(patient)
        if not self.head:
            self.head = newNode
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = newNode

    def display(self):
        if not self.head:
            print("==== No patients consulted yet ===")
            return
        current = self.head
        print("=== Consulted Patients ===")
        patient_number = 1
        while current:
            print(f"[{patient_number}]")
            print(f"Patient Name: {current.patient['name']}")
            print(f"Patient Age: {current.patient['age']}")
            print(f"Patient Reason: {current.patient['reason']}")
            print("==========================")
            current = current.next
            patient_number += 1
    

q = Queue()
consulted = LinkedList()

print("=" * 30 + "\nCLINIC ADMINISTRATOR SYSTEM\n" + "=" * 30)

while True:
    #Clinic Administrator System Menu
    print("\n[1] Patient Registration")
    print("[2] Serve Patients")
    print("[3] View Consultation Record")
    print("[4] Exit")
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
            q.peek()
            patient = q.dequeue()
            consulted.new_record(patient)
            print(f"   Status: Served")
            print(f"\n   Remaining Patients: {q.size()}")

        
    elif choice == '3':
        consulted.display()

    elif choice == '4':
        #Exit the system
        while True:
            #Ensure that the user wants to exit
            confirm_exit = input("Are you sure you want to exit? (Y/N): ").strip().upper()
            if confirm_exit == 'Y':
                break
            elif confirm_exit == 'N':
                print("\nReturning to the main menu...")
                break
            else:
                #Invalid input handling for exit confirmation
                print("Invalid input. Please enter 'Y' or 'N'.")
        if confirm_exit == 'Y':
            print("\nThank you for using the Clinic Administrator System!")
            break
        elif confirm_exit == 'N':
            continue
    else:
        #Invalid choice handling
        print("\nInvalid choice. Please try again.")

class BSTNode:
    def __init__(self, patient):
        self.patient = patient
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

def insert(self, patient):
    if self.root is None:
        self.root = BSTNode(patient)
    return

curP = self.root
while True:
    if patient['name'].lower() < curP.patient['name'].lower():
        if curP.left is None:
            curP.left = BSTNode(patient)
            break
            curP = curP.left
        else:
         if curP.right is None:
             curP.right = BSTNode(patient)
             break 
        curP = curP.right

    def patient_search(self, p_name_search):
        target = p_name_search.lower()
        curP = self.root

        while curP is not None:
            if curP.patient['name'].lower() == target:
                return curP.patient

            if target < curP.patient['name'].lower():
                curP = curP.left
            else:
                curP = curP.right

        return None


"""Kindly continue for the next members in  BRANCH: VERSION-ONE"""
