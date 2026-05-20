from collections import deque
from datetime import datetime, timezone
from zoneinfo import ZoneInfo
import os
import sys
import time

# =========================
# UX HELPERS  (ported from To-Do app)
# =========================

def clear():
    os.system("cls" if os.name == "nt" else "clear")


def thick_divider(width=50):
    print("═" * width)


def thin_divider(width=50):
    print("─" * width)


def get_char():
    """Read a single keypress without requiring Enter ."""
    if os.name == "nt":
        import msvcrt
        return msvcrt.getwch()
    else:
        import tty
        import termios
        fd = sys.stdin.fileno()
        old = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old)
        return ch


def input_password(prompt="  Password : "):
    """Read password character by character, echoing '*' for each character.
    Supports backspace."""
    print(prompt, end="", flush=True)
    password = ""
    while True:
        ch = get_char()
        # Enter pressed — done
        if ch in ("\r", "\n"):
            print()
            break
        # Backspace (Windows: \x08, Unix: \x7f)
        elif ch in ("\x08", "\x7f"):
            if password:
                password = password[:-1]
                # Move cursor back, erase character, move back again
                print("\b \b", end="", flush=True)
        # Ctrl+C
        elif ch == "\x03":
            print()
            raise KeyboardInterrupt
        else:
            password += ch
            print("*", end="", flush=True)
    return password


def pause(msg="  Press [Enter] or [Space] to continue."):
    print(f"\n{msg}")
    while True:
        ch = get_char()
        if ch in ("\r", "\n", " ", ""):
            break


def print_header(title=None):
    clear()
    thick_divider()
    print("  CLINIC ADMINISTRATOR SYSTEM".center(50))
    thick_divider()
    if title:
        print(f"  {title.upper()}")
        thin_divider()


def loading():
    print("\n  Loading", end="", flush=True)
    for _ in range(3):
        time.sleep(0.3)
        print(".", end="", flush=True)
    print()


def current_time():
    gen_time = datetime.now(timezone.utc)
    phil_time = gen_time.astimezone(ZoneInfo("Asia/Manila"))
    return phil_time.strftime("%B %d, %Y | %I:%M %p")


# =========================
# PATIENT CLASS
# =========================
class Patient:
    def __init__(self, name, age, reason):
        self.name = name.title()
        self.age = age
        self.reason = reason

    def display(self):
        thin_divider(35)
        print(f"  Name   : {self.name}")
        print(f"  Age    : {self.age}")
        print(f"  Reason : {self.reason}")
        thin_divider(35)


# =========================
# QUEUE CLASS
# =========================
class Queue:
    def __init__(self):
        self.patients = deque()

    def enqueue(self, patient):
        self.patients.append(patient)
        print(f"\n  ✔ {patient.name} added to queue.")

    def dequeue(self):
        if self.is_empty():
            print("\n  No patients in queue.")
            return None
        return self.patients.popleft()

    def is_empty(self):
        return len(self.patients) == 0

    def size(self):
        return len(self.patients)

    def display_queue(self):
        thick_divider()
        print("  CURRENT QUEUE")
        thin_divider()
        if self.is_empty():
            print("  (empty)")
        else:
            for i, patient in enumerate(self.patients, start=1):
                print(f"  [{i}] {patient.name}")
        thick_divider()


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
        thick_divider()
        print("  CONSULTED PATIENTS  (Chronological)")
        thin_divider()
        if not self.head:
            print("  No consultation records.")
            thick_divider()
            return
        current = self.head
        count = 1
        while current:
            print(f"\n  Patient #{count}")
            current.patient.display()
            current = current.next
            count += 1
        thick_divider()

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
            if target in current_name:
                return current.patient
            elif target < current_name:
                current = current.left
            else:
                current = current.right
        return None

    def _inorder(self, node):
        if node:
            self._inorder(node.left)
            node.patient.display()
            self._inorder(node.right)

    def display_all(self):
        thick_divider()
        print("  ALL CONSULTED PATIENTS  (Alphabetical)")
        thin_divider()
        if not self.root:
            print("  No records found.")
            thick_divider()
            return
        self._inorder(self.root)
        thick_divider()


# =========================
# HELP MENU
# =========================
def help_menu():
    print_header("Help Menu")
    items = [
        ("1", "Register Patient",  "Adds patient to the waiting queue."),
        ("2", "Serve Patient",     "Serves the first patient in line."),
        ("3", "View History",      "Displays all recently consulted patients (chronological)."),
        ("4", "Search Patient",    "Searches patient by name."),
        ("5", "Delete Record",     "Deletes a consultation record."),
        ("6", "Display Record",    "Displays all consulted patients alphabetically."),
        ("7", "Exit",              "Closes the system safely."),
        ("8", "Help",              "Displays this help menu."),
    ]
    for num, name, desc in items:
        print(f"  [{num}] {name}")
        print(f"       {desc}")
        print()
    pause("  Press [Enter] or [Space] to go back.")


# =========================
# LOGIN
# =========================
USERNAME = "Admin"
PASSWORD = "123Clinic"


def login():
    attempts = 3
    while attempts > 0:
        clear()
        thick_divider()
        print("  CLINIC ADMINISTRATOR SYSTEM".center(50))
        thick_divider()
        print("  LOGIN")
        thin_divider()
        username = input("  Username : ").strip()
        password = input_password("  Password : ").strip()

        if username == USERNAME and password == PASSWORD:
            thick_divider()
            print("  ✔ Login Successful!")
            loading()
            return True

        attempts -= 1
        thick_divider()
        if attempts > 0:
            print(f"  ✘ Invalid credentials. Attempts left: {attempts}")
        else:
            print("  ✘ Too many failed attempts. System locked.")
        pause("  Press [Enter] or [Space] to try again." if attempts > 0 else "  Press [Enter] or [Space] to exit.")

    return False


# =========================
# MAIN MENU DISPLAY
# =========================
def print_main_menu(queue):
    print_header()
    thick_divider()
    print(f"  Date & Time      : {current_time()}")
    print(f"  Patients Waiting : {queue.size()}")
    thick_divider()
    thin_divider()
    print("  [1] Register Patient")
    print("  [2] Serve Patient")
    print("  [3] View History")
    print("  [4] Search Patient")
    print("  [5] Delete Record")
    print("  [6] Display Record")
    print("  [7] Exit")
    print("  [8] Help")
    thin_divider()


def is_valid_name(name):
    """Allow only letters, spaces, and periods (for names like 'Jr.' or 'St.')"""
    return all(c.isalpha() or c in (" ", ".") for c in name)


# =========================
# MENU HANDLERS
# =========================
def handle_register(queue):
    print_header("Patient Registration")
    name = input("  Patient Name    : ").strip()
    if not name:
        print("  Name cannot be empty.")
        pause()
        return
    if not is_valid_name(name):
        print("  Invalid name. Only letters, spaces, and '.' are allowed.")
        pause()
        return

    age_input = input("  Patient Age     : ").strip()
    if not age_input.isdigit():
        print("  Invalid age.")
        pause()
        return
    age = int(age_input)
    if age < 1 or age > 120:
        print("  Age must be between 1 and 120.")
        pause()
        return

    reason = input("  Reason for Visit: ").strip()
    if not reason:
        print("  Reason cannot be empty.")
        pause()
        return

    patient = Patient(name, age, reason)
    queue.enqueue(patient)
    queue.display_queue()
    pause()


def handle_serve(queue, records, search_tree):
    patient = queue.dequeue()
    if patient:
        loading()
        print_header("Serving Patient")
        patient.display()
        records.add_record(patient)
        search_tree.insert(patient)
        print("\n  ✔ Patient served successfully.")
        pause()


def handle_view_history(records):
    print_header("View History")
    records.display_records()
    pause()


def handle_search(search_tree):
    print_header("Search Patient")
    name = input("  Enter patient name: ").strip()
    found = search_tree.search(name)
    thin_divider()
    if found:
        print("  PATIENT FOUND")
        found.display()
    else:
        print("  Patient not found.")
    pause()


def handle_delete(records):
    print_header("Delete Record")
    name = input("  Enter patient name to delete: ").strip()
    thin_divider()
    print(f"  This will permanently delete the record for \"{name.title()}\".")
    confirm = input('  Type "YES" to confirm: ').strip()
    if confirm == "YES":
        deleted = records.delete_record(name)
        if deleted:
            print("\n  ✔ Record deleted successfully.")
            deleted.display()
        else:
            print("  Record not found.")
    else:
        print("  Deletion cancelled. Nothing was changed.")
    pause()


def handle_display_all(search_tree):
    print_header("Display All Records")
    search_tree.display_all()
    pause()


def handle_exit():
    print_header()
    thick_divider()
    confirm = input("  Exit system? (Y/N): ").strip().upper()
    if confirm == "Y":
        thick_divider()
        print("\n  Thank you for using the Clinic System!")
        print("  Stay safe and healthy. 🏥\n")
        thick_divider()
        return True
    return False


# =========================
# MAIN PROGRAM
# =========================
def main():
    if not login():
        exit()

    queue       = Queue()
    records     = LinkedList()
    search_tree = BST()

    while True:
        print_main_menu(queue)
        choice = input("  Enter choice: ").strip()

        if choice == "1":
            handle_register(queue)
        elif choice == "2":
            handle_serve(queue, records, search_tree)
        elif choice == "3":
            handle_view_history(records)
        elif choice == "4":
            handle_search(search_tree)
        elif choice == "5":
            handle_delete(records)
        elif choice == "6":
            handle_display_all(search_tree)
        elif choice == "7":
            if handle_exit():
                break
        elif choice == "8":
            help_menu()
        else:
            thick_divider()
            print("  Invalid choice. Please try again.")
            pause()

if __name__ == "__main__":
    main()

"""Love You Sir :D - Group 1 | BSCS 1 - 2"""
