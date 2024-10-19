import sys

def cli_parser(command):
    switcher = {
        'start': "Starting the program...",
        'stop': "Stopping the program...",
        'restart': "Restarting the program..."
    }
    return switcher.get(command, "Unknown command")

# Example usage:
if len(sys.argv) > 1:
    print(cli_parser(sys.argv[1]))
else:
    print("No command provided")
