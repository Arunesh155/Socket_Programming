import socket

# Function to determine the winner of the game
def determine_winner(choice1, choice2):
    if choice1 == choice2:
        return "Draw"
    elif (choice1 == "stone" and choice2 == "scissor") or \
         (choice1 == "paper" and choice2 == "stone") or \
         (choice1 == "scissor" and choice2 == "paper"):
        return "Player 1 wins!"
    else:
        return "Player 2 wins!"

def tcp_server():
    # Create a TCP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('0.0.0.0', 12345))  # Bind to all network interfaces
    server_socket.listen(2)

    print("Server is waiting for connections...")

    try:
        # Accept two clients
        conn1, addr1 = server_socket.accept()
        print(f"Player 1 connected: {addr1}")

        conn2, addr2 = server_socket.accept()
        print(f"Player 2 connected: {addr2}")

        # Receive choices from both players
        choice1 = conn1.recv(1024).decode().strip().lower()
        choice2 = conn2.recv(1024).decode().strip().lower()

        print(f"Player 1 chose: {choice1}")
        print(f"Player 2 chose: {choice2}")

        # Determine the winner
        result = determine_winner(choice1, choice2)

        # Send the result to both players
        conn1.send(result.encode())
        conn2.send(result.encode())

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        # Close connections
        conn1.close()
        conn2.close()
        server_socket.close()

if __name__ == "__main__":
    while True:
        tcp_server()
