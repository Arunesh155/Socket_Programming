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

def udp_server():
    # Create a UDP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind(('0.0.0.0', 12345))  # Bind to all network interfaces

    print("UDP server is waiting for connections...")

    try:
        # Receive choices from two players
        data1, addr1 = server_socket.recvfrom(1024)
        choice1 = data1.decode().strip().lower()
        print(f"Player 1 ({addr1}) chose: {choice1}")

        data2, addr2 = server_socket.recvfrom(1024)
        choice2 = data2.decode().strip().lower()
        print(f"Player 2 ({addr2}) chose: {choice2}")

        # Determine the winner
        result = determine_winner(choice1, choice2)

        # Print the result in the terminal
        print(f"Game result: {result}")

        # Send the result back to both players
        server_socket.sendto(result.encode(), addr1)
        server_socket.sendto(result.encode(), addr2)

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        # Close the server socket
        server_socket.close()

if __name__ == "__main__":
    while True:
        udp_server()
