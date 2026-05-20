from getpass import getpass
from collections import deque
from datetime import datetime
import time

# =========================
# DISPLAY FUNCTIONS
# =========================
def header(title):
    print("\n" + "=" * 45)
    print(title.center(45))
    print("=" * 45)

def loading():
    print("\nLoading", end="")

    for i in range(3):
        time.sleep(0.3)
        print(".", end="")

    print()

def current_time():
    now = datetime.now()
    return now.strftime("%B %d, %Y | %I:%M %p")

# =========================
# PATIENT CLASS
# =========================
class Patient:
    def __init__(self, name, age, reason):
        self.name = name.title()
        self.age = age
        self.reason = reason

    def display(self):
        print("-" * 35)
        print(f" Name   : {self.name}")
        print(f" Age    : {self.age}")
        print(f" Reason : {self.reason}")
        print("-" * 35)

# =========================
# QUEUE CLASS
# =========================
class Queue:
    def __init__(self):
        self.patients = deque()

    def enqueue(self, patient):
        self.patients.append(patient)
        print(f"\n{patient.name} added to queue.")

    def dequeue(self):
        if self.is_empty():
            print("\nNo patients in queue.")
            return None

        return self.patients.popleft()

    def is_empty(self):
        return len(self.patients) == 0

    def size(self):
        return len(self.patients)

    def display_queue(self):
        if self.is_empty():
            print("\nQueue is empty.")
            return

        header("CURRENT QUEUE")

        for i, patient in enumerate(self.patients, start=1):
            print(f"[{i}] {patient.name}")

# =========================
# LINKED LIST
# =========================
class Node:
    def __init__(self, patient):
        self.patient = patient
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add_record(self, patient):
        new_node = Node(patient)

        if not self.head:
            self.head = new_node
            return

        current = self.head

        while current.next:
            current = current.next

        current.next = new_node

    def display_records(self):
        if not self.head:
            print("\nNo consultation records.")
            return

        header("CONSULTED PATIENTS")

        current = self.head
        count = 1

        while current:
            print(f"\nPatient #{count}")
            current.patient.display()
            current = current.next
            count += 1

    def delete_record(self, name):

        if not self.head:
            return None

        target = name.lower()

        if self.head.patient.name.lower() == target:
            deleted = self.head.patient
            self.head = self.head.next
            return deleted

        current = self.head

        while current.next:

            if current.next.patient.name.lower() == target:
                deleted = current.next.patient
                current.next = current.next.next
                return deleted

            current = current.next

        return None

# =========================
# BST
# =========================
class BSTNode:
    def __init__(self, patient):
        self.patient = patient
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, patient):

        new_node = BSTNode(patient)

        if not self.root:
            self.root = new_node
            return

        current = self.root

        while True:

            if patient.name.lower() < current.patient.name.lower():

                if current.left is None:
                    current.left = new_node
                    return

                current = current.left

            else:

                if current.right is None:
                    current.right = new_node
                    return

                current = current.right

    def search(self, name):

        current = self.root
        target = name.lower()

        while current:

            current_name = current.patient.name.lower()

            # Partial search
            if target in current_name:
                return current.patient

            elif target < current_name:
                current = current.left

            else:
                current = current.right

        return None

    def inorder(self, node):

        if node:
            self.inorder(node.left)
            node.patient.display()
            self.inorder(node.right)

    def display_all(self):

        if not self.root:
            print("\nNo records found.")
            return

        header("ALL CONSULTED PATIENTS")
        self.inorder(self.root)

# =========================
# HELP MENU
# =========================
def help_menu():

    header("HELP MENU")

    print("""
[1] Register Patient
    - Adds patient to waiting queue.

[2] Serve Patient
    - Serves the first patient in line.

[3] View Records
    - Displays all consulted patients.

[4] Search Patient
    - Searches patient by name.

[5] Delete Record
    - Deletes consultation record.

[6] Display All
    - Displays all patients alphabetically.

[7] Exit
    - Closes the system safely.

[8] Help
    - Displays this help menu.
    """)


# =========================
# LOGIN
# =========================
USERNAME = "Admin"
PASSWORD = "123Clinic"

attempts = 3

while attempts > 0:

    header("LOGIN SYSTEM")

    username = input("Username: ").strip()
    password = getpass("Password: ").strip()

    if username == USERNAME and password == PASSWORD:
        print("\nLogin Successful!")
        loading()
        break

    attempts -= 1
    print(f"\nInvalid login. Attempts left: {attempts}")

if attempts == 0:
    print("\nSystem Locked.")
    exit()

# =========================
# SYSTEM OBJECTS
# =========================
queue = Queue()
records = LinkedList()
search_tree = BST()

# =========================
# MAIN PROGRAM
# =========================
while True:

    header("CLINIC ADMINISTRATOR SYSTEM")

    print(f"Date & Time      : {current_time()}")
    print(f"Patients Waiting : {queue.size()}")

    print("\n[1] Register Patient")
    print("[2] Serve Patient")
    print("[3] View Records")
    print("[4] Search Patient")
    print("[5] Delete Record")
    print("[6] Display All")
    print("[7] Exit")
    print("[8] Help")

    choice = input("\nEnter choice: ").strip()

    # =====================
    # REGISTER
    # =====================
    if choice == '1':

        header("PATIENT REGISTRATION")

        name = input("Patient Name: ").strip()

        if not name:
            print("Name cannot be empty.")
            continue

        age_input = input("Patient Age: ").strip()

        if not age_input.isdigit():
            print("Invalid age.")
            continue

        age = int(age_input)

        if age < 1 or age > 120:
            print("Age must be between 1-120.")
            continue

        reason = input("Reason for Visit: ").strip()

        if not reason:
            print("Reason cannot be empty.")
            continue

        patient = Patient(name, age, reason)

        queue.enqueue(patient)
        queue.display_queue()

    # =====================
    # SERVE
    # =====================
    elif choice == '2':

        patient = queue.dequeue()

        if patient:

            loading()

            header("SERVING PATIENT")

            patient.display()

            records.add_record(patient)
            search_tree.insert(patient)

            print("\nPatient served successfully.")

    # =====================
    # VIEW RECORDS
    # =====================
    elif choice == '3':
        records.display_records()

    # =====================
    # SEARCH
    # =====================
    elif choice == '4':

        header("SEARCH PATIENT")

        name = input("Enter patient name: ").strip()

        found = search_tree.search(name)

        if found:
            print("\n=== PATIENT FOUND ===")
            found.display()

        else:
            print("Patient not found.")

    # =====================
    # DELETE
    # =====================
    elif choice == '5':

        header("DELETE RECORD")

        name = input("Enter patient name to delete: ").strip()

        confirm = input("Delete this record? (Y/N): ").upper()

        if confirm == 'Y':

            deleted = records.delete_record(name)

            if deleted:
                print("\nRecord deleted successfully.")
                deleted.display()

            else:
                print("Record not found.")

        else:
            print("Deletion cancelled.")

    # =====================
    # DISPLAY ALL
    # =====================
    elif choice == '6':
        search_tree.display_all()

    # =====================
    # EXIT
    # =====================
    elif choice == '7':

        confirm = input("Exit system? (Y/N): ").upper()

        if confirm == 'Y':
            print("\nThank you for using the system!")
            break

    # =====================
    # HELP MENU
    # =====================
    elif choice == '8':
        help_menu()

    else:
        print("\nInvalid choice.")


"""Kindly continue for the next members in  BRANCH: VERSION-ONE"""
