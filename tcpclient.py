import socket
import tkinter as tk
from tkinter import messagebox
import random

# Function to determine the winner of the game
def determine_winner(choice1, choice2):
    if choice1 == choice2:
        return "Draw"
    elif (choice1 == "stone" and choice2 == "scissor") or \
         (choice1 == "paper" and choice2 == "stone") or \
         (choice1 == "scissor" and choice2 == "paper"):
        return "You win!"
    else:
        return "Computer wins!"

# Function to handle 2-player game using the server
def send_choice(choice):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('192.168.137.1', 12345))
    
    # Send the selected choice to the server
    client_socket.send(choice.encode())
    
    # Receive the game result
    result = client_socket.recv(1024).decode()
    
    # Show the result in a message box
    messagebox.showinfo("Result", result)
    
    client_socket.close()

# Function for playing against the computer (1-player mode)
def play_against_computer(choice):
    computer_choice = random.choice(['stone', 'paper', 'scissor'])
    result = determine_winner(choice, computer_choice)
    messagebox.showinfo("Result", f"Computer chose: {computer_choice}\n{result}")

# Function to handle button clicks for Stone, Paper, Scissors in 1-player mode
def on_button_click_1_player(choice):
    play_against_computer(choice)

# Function to handle button clicks for Stone, Paper, Scissors in 2-player mode
def on_button_click_2_player(choice):
    send_choice(choice)

# UI for the actual game (Stone, Paper, Scissors buttons) with "Back" button
def game_ui(num_players):
    window = tk.Tk()
    window.title("Stone Paper Scissors Game")
    window.geometry("500x400")
    window.configure(bg="#87CEEB")  # Sky blue background

    tk.Label(window, text="Choose your option:", font=("Arial", 14), fg="white", bg="#87CEEB").pack(pady=10)

    if num_players == 1:
        tk.Label(window, text="You are playing against the computer", font=("Arial", 14), fg="white", bg="#87CEEB").pack(pady=10)
    else:
        tk.Label(window, text="You are Player 1", font=("Arial", 14), fg="white", bg="#87CEEB").pack(pady=10)

    # Styling for buttons
    button_style = {"font": ("Arial", 12), "width": 10, "bg": "#4682B4", "fg": "white", "activebackground": "#1E90FF", "activeforeground": "#fff"}

    # Create buttons for Stone, Paper, Scissors
    stone_button = tk.Button(window, text="Stone", **button_style,
                             command=lambda: on_button_click_1_player("stone") if num_players == 1 else on_button_click_2_player("stone"))
    stone_button.pack(pady=5)
    
    paper_button = tk.Button(window, text="Paper", **button_style,
                             command=lambda: on_button_click_1_player("paper") if num_players == 1 else on_button_click_2_player("paper"))
    paper_button.pack(pady=5)
    
    scissor_button = tk.Button(window, text="Scissors", **button_style,
                               command=lambda: on_button_click_1_player("scissor") if num_players == 1 else on_button_click_2_player("scissor"))
    scissor_button.pack(pady=5)

    # Create "Back" button to return to the main menu
    back_button = tk.Button(window, text="Back", font=("Arial", 12), width=10, bg="#DC143C", fg="white",
                            command=lambda: [window.destroy(), main_menu()])
    back_button.pack(pady=10)

    window.mainloop()

# Initial page to select the number of players
def main_menu():
    window = tk.Tk()
    window.title("KONGU ENGINEERING COLLEGE")
    window.geometry("500x400")
    window.configure(bg="#87CEEB")  # Sky blue background

    # Header and Title
    tk.Label(window, text="KONGU ENGINEERING COLLEGE", font=("Arial", 16, "bold"), fg="white", bg="#87CEEB").pack(pady=10)
    tk.Label(window, text="ONLINE GAME", font=("Arial", 14, "italic"), fg="white", bg="#87CEEB").pack(pady=5)

    tk.Label(window, text="Select the number of players:", font=("Arial", 14), fg="white", bg="#87CEEB").pack(pady=20)

    # Button for 1 Player (play against computer)
    one_player_button = tk.Button(window, text="1 Player", font=("Arial", 12), width=15, bg="#4682B4", fg="white",
                                  activebackground="#1E90FF", activeforeground="#fff", command=lambda: [window.destroy(), game_ui(1)])
    one_player_button.pack(pady=10)

    # Button for 2 Players (play against another player via server)
    two_player_button = tk.Button(window, text="2 Players", font=("Arial", 12), width=15, bg="#4682B4", fg="white",
                                  activebackground="#1E90FF", activeforeground="#fff", command=lambda: [window.destroy(), game_ui(2)])
    two_player_button.pack(pady=10)

    # Footer with member names, one by one
    member_names = ["3: Akashine Y", "2: Arunesh S", "1: Bavyadharshini R"]
    for member in member_names:
        tk.Label(window, text=f"Member {member}", font=("Arial", 10), fg="white", bg="#87CEEB").pack(side="bottom", pady=5, anchor="e")

    window.mainloop()

if __name__ == "__main__":
    main_menu()