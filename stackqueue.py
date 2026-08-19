from collections import deque


# ============================================================
#                       QUEUE
# ============================================================

def queue_program():
    queue = deque()

    while True:
        print("\n========== QUEUE ==========")
        print("1. Enqueue (Add)")
        print("2. Dequeue (Remove)")
        print("3. Peek (Front)")
        print("4. Display Queue")
        print("5. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            customer = input("Enter customer name: ").strip()

            if customer:
                queue.append(customer)
                print(f"{customer} added to the queue.")
            else:
                print("Customer name cannot be empty.")

        elif choice == "2":
            if queue:
                served = queue.popleft()
                print(f"Served: {served}")
            else:
                print("Queue is empty!")

        elif choice == "3":
            if queue:
                print(f"Next customer: {queue[0]}")
            else:
                print("Queue is empty!")

        elif choice == "4":
            if queue:
                print("Current Queue:", list(queue))
            else:
                print("Queue is empty!")

        elif choice == "5":
            print("Exiting Queue program...")
            break

        else:
            print("Invalid choice. Please enter 1-5.")


# ============================================================
#                       STACK
# ============================================================

def stack_program():
    stack = []

    while True:
        print("\n========== STACK ==========")
        print("1. Push")
        print("2. Pop")
        print("3. Peek")
        print("4. Display Stack")
        print("5. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            item = input("Enter item to add: ").strip()

            if item:
                stack.append(item)
                print(f"{item} added to the stack.")
            else:
                print("Item cannot be empty.")

        elif choice == "2":
            if stack:
                removed = stack.pop()
                print(f"Removed: {removed}")
            else:
                print("Stack is empty!")

        elif choice == "3":
            if stack:
                print(f"Top item: {stack[-1]}")
            else:
                print("Stack is empty!")

        elif choice == "4":
            if stack:
                print("Current Stack:", stack)
            else:
                print("Stack is empty!")

        elif choice == "5":
            print("Exiting Stack program...")
            break

        else:
            print("Invalid choice. Please enter 1-5.")


# ============================================================
#                    LINKED LIST
# ============================================================

def linked_list_program():
    linked_list = ["USA", "China", "Canada"]

    while True:
        print("\n======= LINKED LIST =======")
        print("Current List:", linked_list)

        print("\n1. Add Element")
        print("2. Remove Element")
        print("3. Replace Element")
        print("4. Search Element")
        print("5. Display List")
        print("6. Exit")

        choice = input("Enter your choice: ").strip()

        # Add
        if choice == "1":
            element = input("Enter element: ").strip()

            try:
                position = int(input("Enter position: "))

                if position < 0 or position > len(linked_list):
                    print("Invalid position!")
                else:
                    linked_list.insert(position, element)
                    print("Element added successfully.")

            except ValueError:
                print("Please enter a valid number.")

        # Remove
        elif choice == "2":
            element = input("Enter element to remove: ").strip()

            if element in linked_list:
                linked_list.remove(element)
                print("Element removed successfully.")
            else:
                print("Element not found.")

        # Replace
        elif choice == "3":
            try:
                position = int(input("Enter position: "))

                if position < 0 or position >= len(linked_list):
                    print("Invalid position!")
                else:
                    new_element = input("Enter new element: ").strip()
                    old_element = linked_list[position]

                    linked_list[position] = new_element

                    print(
                        f"'{old_element}' replaced with "
                        f"'{new_element}'."
                    )

            except ValueError:
                print("Please enter a valid number.")

        # Search
        elif choice == "4":
            element = input("Enter element to search: ").strip()

            if element in linked_list:
                position = linked_list.index(element)
                print(f"Element found at position {position}.")
            else:
                print("Element not found.")

        # Display
        elif choice == "5":
            print("Current List:", linked_list)

        # Exit
        elif choice == "6":
            print("Exiting Linked List program...")
            break

        else:
            print("Invalid choice. Please enter 1-6.")


# ============================================================
#                     MAIN PROGRAM
# ============================================================

def main():
    while True:
        print("\n================================")
        print("       DATA STRUCTURES")
        print("================================")
        print("1. Queue")
        print("2. Stack")
        print("3. Linked List")
        print("4. Exit")

        choice = input("Choose a data structure: ").strip()

        if choice == "1":
            queue_program()

        elif choice == "2":
            stack_program()

        elif choice == "3":
            linked_list_program()

        elif choice == "4":
            print("Program closed. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter 1-4.")


# Run the program
if __name__ == "__main__":
    main()
