import time
import sys

colors = {
    'RED': '\033[91m',
    'YELLOW': '\033[93m',
    'ORANGE': '\033[33m', # Often looks more like dark yellow/brown in terminals
    'MAGENTA': '\033[95m',
    'CYAN': '\033[96m',
    'ENDC': '\033[0m'  # Resets the color
}
color_cycle = list(colors.values())[:-1] 
text = "✨🪔 शुभ दीपावली 🪔✨"

def animate_text():
    try:
        while True:
            for color in color_cycle:
                print(f"{color}{text}{colors['ENDC']}", end='\r', flush=True)
                time.sleep(0.5)
                
    except KeyboardInterrupt:
        print("\nAnimation stopped. Happy Diwali!")

if sys.stdout.isatty():
        print("Starting Deepavali animation... Press Ctrl+C to stop.")
        time.sleep(1)
        animate_text()
else:
        print("This animation requires a terminal that supports ANSI color codes.")
        print(text) # Just print the text normally
