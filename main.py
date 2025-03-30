import argparse
import os
import time
from datetime import datetime, timedelta

def notify(message):
    """Display a notification message based on the operating system."""
    print(f"\n[Notification] {message}")
    
    if os.name == 'nt':  # Windows
        try:
            import winsound
            # Play a beep sound (frequency=800, duration=1000ms)
            winsound.Beep(800, 1000)
        except Exception as e:
            # If sound notification fails, we already have the print fallback above
            pass
    else:  # Unix/Linux/MacOS
        try:
            os.system(f'notify-send "PyFocusTime Timer" "{message}"')
        except Exception as e:
            # If system notification fails, we already have the print fallback above
            pass

def format_time(seconds):
    """Format seconds into MM:SS string."""
    return str(timedelta(seconds=seconds))[2:7]

def focus_timer(focus_time=25, break_time=5):
    """Run a PyFocusTime timer with specified focus and break durations."""
    focus_seconds = focus_time * 60
    break_seconds = break_time * 60
    
    try:
        while True:
            # Focus Time
            print(f"\nStarting {focus_time} minute focus session...")
            start_time = time.time()
            while time.time() - start_time < focus_seconds:
                remaining = focus_seconds - int(time.time() - start_time)
                print(f"Focus Time Remaining: {format_time(remaining)}", end='\r')
                time.sleep(1)
            
            notify(f"Focus session complete! Take a {break_time} minute break.")

            # Break Time
            print(f"\n\nStarting {break_time} minute break...")
            start_time = time.time()
            while time.time() - start_time < break_seconds:
                remaining = break_seconds - int(time.time() - start_time)
                print(f"Break Time Remaining: {format_time(remaining)}", end='\r')
                time.sleep(1)
            
            notify("Break time is over! Ready for another focus session?")
            
            # Ask if user wants to continue with timeout
            print("\n\nPress Enter to start next session or 'q' to quit: ", end='', flush=True)
            
            # Set up a timeout for user input
            import threading
            import sys
            
            response = [None]
            input_timeout = 10  # 60 seconds timeout
            stop_thread = False
            
            def get_input():
                while not stop_thread:
                    try:
                        response[0] = input()
                        break
                    except EOFError:
                        # Handle Ctrl+C in input thread
                        break
            
            input_thread = threading.Thread(target=get_input)
            input_thread.daemon = True
            input_thread.start()
            
            # Wait for input or timeout
            start_wait_time = time.time()
            while input_thread.is_alive():
                # Check if a minute has passed
                if time.time() - start_wait_time >= input_timeout:
                    # Timeout occurred, notify user
                    print("\nWaiting for your response...", flush=True)
                    notify("Please respond to continue or quit the PyFocusTime session")
                    # Reset the timer for the next notification
                    start_wait_time = time.time()
                # Sleep briefly to avoid high CPU usage
                time.sleep(1)
            
            if response[0] and response[0].lower() == 'q':
                break
    except KeyboardInterrupt:
        stop_thread = True
        print("\n\nGoodbye! PyFocusTime Timer stopped.")
        return

if __name__ == "__main__":
    try:
        parser = argparse.ArgumentParser(description='PyFocusTime - Your Focus Timer')
        parser.add_argument('-f', '--focus', type=float, default=0.20,
                          help='Focus time duration in minutes (default: 25)')
        parser.add_argument('-b', '--break-time', type=float, default=0.05,
                          help='Break time duration in minutes (default: 5)')
        
        args = parser.parse_args()
        
        print("Welcome to PyFocusTime - Your PyFocusTime Timer!")
        print(f"Settings: {args.focus} minutes focus + {args.break_time} minutes break")
        focus_timer(focus_time=args.focus, break_time=args.break_time)
    except KeyboardInterrupt:
        print("\n\nGoodbye! PyFocusTime Timer stopped.")