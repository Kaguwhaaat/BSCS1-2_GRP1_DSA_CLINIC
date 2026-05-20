from getpass import getpass

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

    def delete_record(self, p_name):

        target = p_name.lower()
 
        #Empty list
        if not self.head:
            print("\n=== No Consulted Records to Delete ===")
            return None
 
        #Head node is the match
        if self.head.patient['name'].lower() == target:
            deleted = self.head.patient
            self.head = self.head.next
            return deleted
 
        #Search through the rest of the list
        current = self.head
        while current.next:
            if current.next.patient['name'].lower() == target:
                deleted = current.next.patient
                current.next = current.next.next  
                return deleted
            current = current.next
 
        return None

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

class BSTNode:
    def __init__(self, patient):
        self.patient = patient
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None
    
    def is_empty(self):
        return self.root is None
    
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
    
    def delete_patient(self, p_name):
      
        target = p_name.lower()
        parent = None
        curP = self.root
        is_left_child = False
 
        #locate node and parent
        while curP is not None:
            cur_name = curP.patient['name'].lower()
            if cur_name == target:
                break
            parent = curP
            if target < cur_name:
                curP = curP.left
                is_left_child = True
            else:
                curP = curP.right
                is_left_child = False
 
        if curP is None:
            return None  
 
        deleted_patient = curP.patient
 
        if curP.left is not None and curP.right is not None:
            # finding inorder succesor
            successor_parent = curP
            successor = curP.right
            while successor.left is not None:
                successor_parent = successor
                successor = successor.left
 
            # copy the data into current node
            curP.patient = successor.patient
 
            # delete successor node
            if successor_parent == curP:
                successor_parent.right = successor.right
            else:
                successor_parent.left = successor.right
 
            return deleted_patient
 

        if curP.left is None and curP.right is None:
            replacement = None             
        elif curP.left is None:
            replacement = curP.right     
        else:
            replacement = curP.left         
 
        if parent is None:
            # delete root
            self.root = replacement
        elif is_left_child:
            parent.left = replacement
        else:
            parent.right = replacement
 
        return deleted_patient

    def _inorder(self, node, result):

        if node is None:
            return
        self._inorder(node.left, result)
        result.append(node.patient)
        self._inorder(node.right, result)

    def display_all(self):

        if self.root is None:
            print("\n=== No Records in BST ===")
            return
        #Collects patient record in sorted order via inorder traversal
        records = []
        self._inorder(self.root,records)
        #Prints patients alphabetically arranged
        print("\n=== All Consulted Patients (A-Z) ===")
        for i, patient in enumerate(records, start=1):
            print(f"[{i}]")
            print(f"   Name  : {patient['name']}")
            print(f"   Age   : {patient['age']}")
            print(f"   Reason: {patient['reason']}")
            print("   " + "-" * 26)

# LOGIN SYSTEM TO AUTHENTICATE

SYSTEM_USERNAME = "Admin"
SYSTEM_PASSWORD = "123Clinic"

print("=" * 30)
print("CLINIC LOGIN SYSTEM")
print("=" * 30)

attempts = 3

while attempts > 0:
    username = input("Enter Username: ").strip()
    password = getpass("Enter Password: ").strip() 
    #ADDED GETPASS FOR PASSWORD INVISIBILITY

    if username == SYSTEM_USERNAME and password == SYSTEM_PASSWORD:
        print("\nLogin Successful!")
        break
    else:
        attempts -= 1
        print("\nInvalid Username or Password.")
        print("=" * 30)
        print(f"Attempts Remaining: {attempts}")

if attempts == 0:
    print("\nToo many failed attempts.")
    print("System Locked.")
    exit()

# START OF THE MAIN SYSTEM

q = Queue()
consulted = LinkedList()
search = BST()

print("=" * 30 + "\nCLINIC ADMINISTRATOR SYSTEM\n" + "=" * 30)


def format_name(name):
         return name.title()

while True:
    #Clinic Administrator System Menu
    print("\n[1] Patient Registration")
    print("[2] Serve Patients")
    print("[3] View Consultation Record")
    print("[4] Search Patient")
    print("[5] Delete Patient")
    print("[6] Display All Records")
    print("[7] Exit")
    choice = input("Enter Function: ").strip()

    if choice == '1':
        #Patient Registration
        print("\n=== Patient Registration ===")
        name = input("Enter Patient Name: ").strip()
        name = format_name(name)

        wrongInput = True

        while wrongInput:
            age = input("Enter Patient Age: ").strip()
        
        #Error handling for empty name and non-numeric age
            if  not name:
                print("\n === Name cannot be empty. Please try again. === \n")
                continue

        #Error handling for unrealistic age negative and over 120

            if not age.isdigit():
                print("\n === Invalid age. Please enter a number. === \n")
                continue

            age = int(age)

            if age < 1 or age > 120:
                print("\n === Invalid Age. Try Again (1-120). === \n")
                continue
                
            reason = input("Enter Reason for Visit: ").strip()

            #Enqueue the patient to the queue
            q.enqueue({'name': name, 'age': age, 'reason': reason})

            #Display the current queue of patients
            print("\nCurrent Queue:")
            for number, patient in enumerate(q.to_list(), start=1):
                print(f"   [{number}] {patient['name']}")

            wrongInput = False
        
    elif choice == '2':
         #Error handling for empty queue
         if q.is_empty():
            print("\n=== No Patients to Serve ===")
            continue
         else:
            #Serve Patients
            print("\n=== Serving Patients ===")
            patient = q.dequeue()
            consulted.new_record(patient)
            #To save patient into the BST
            search.insert(patient)
            print(f"   Status: Served")
            print(f"\n   Remaining Patients: {q.size()}")

        
    elif choice == '3':
        consulted.display()
    
    elif choice == '4':
        if search.is_empty():
            print("\n=== No Patients to Search ===")
            continue

        print("\n=== Search Patient ===")
        Sname = input("Enter Patient Full Name: ").strip()

        Found = search.patient_search(Sname)

        if Found:
            print("\n=== Patient Found ===")
            print(f"Name : {Found['name']}")
            print(f"Age  : {Found['age']}")
            print(f"Reason : {Found['reason']}")
        
        else:
            print("Patient not found.")

    elif choice == '5':
        if search.is_empty():
            print("\n=== No Records to Delete ===")
            continue
 
        print("\n=== Delete Consultation Record ===")
        delete_name = input("Enter Patient Full Name to Delete: ").strip()
 
        deleted_record = consulted.delete_record(delete_name)
 
        if deleted_record is None:
            print(f"\nNo record found for '{delete_name}'. Nothing was deleted.")
        else:
            # Mirror the deletion in the BST
            search.delete_patient(name)
            print(f"\n=== Record Deleted Successfully ===")
            print(f"   Name  : {deleted_record['name']}")
            print(f"   Age   : {deleted_record['age']}")
            print(f"   Reason: {deleted_record['reason']}")
    
    elif choice == '6':
        search.display_all()
 
    elif choice == '7':
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


"""Kindly continue for the next members in  BRANCH: VERSION-ONE"""
