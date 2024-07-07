import tkinter as tk

def create_user():
    # Implement the logic for creating a user
    print("Creating user...")

def send_message():
    # Implement the logic for sending a message
    print("Sending message...")

def receive_message():
    # Implement the logic for receiving a message
    print("Receiving message...")

def menu():
    root = tk.Tk()

    def handle_choice():
        choice = choice_var.get()
        if choice == 1:
            create_user()
        elif choice == 2:
            send_message()
        elif choice == 3:
            receive_message()

    choice_var = tk.IntVar()
    
    label = tk.Label(root, text="Select your option:")
    label.pack()

    create_user_button = tk.Radiobutton(root, text="Create User", variable=choice_var, value=1)
    create_user_button.pack()

    send_message_button = tk.Radiobutton(root, text="Send Message", variable=choice_var, value=2)
    send_message_button.pack()

    receive_message_button = tk.Radiobutton(root, text="Receive Message", variable=choice_var, value=3)
    receive_message_button.pack()

    submit_button = tk.Button(root, text="Submit", command=handle_choice)
    submit_button.pack()

    root.mainloop()

menu()
