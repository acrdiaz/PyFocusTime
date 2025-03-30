import argparse
import os
import time
from datetime import datetime, timedelta

def notify(message):
    """Display a notification message based on the operating system."""
    print(f"\n[Notification] {message}")
    
    if os.name == 'nt':  # Windows
        try:
            from plyer import notification
            notification.notify(
                title="Pomodoro Timer",
                message=message,
                timeout=5
            )
        except Exception as e:
            # If notification fails, we already have the print fallback above
            pass
    else:  # Unix/Linux/MacOS
        try:
            os.system(f'notify-send "Pomodoro Timer" "{message}"')
        except Exception as e:
            # If system notification fails, we already have the print fallback above
            pass

def format_time(seconds):
    """Format seconds into MM:SS string."""
    return str(timedelta(seconds=seconds))[2:7]

def pomodoro_timer(focus_time=25, break_time=5):
    """Run a Pomodoro timer with specified focus and break durations."""
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
            
            # Ask if user wants to continue
            response = input("\n\nPress Enter to start next session or 'q' to quit: ")
            if response.lower() == 'q':
                break
    except KeyboardInterrupt:
        print("\n\nGoodbye! Pomodoro Timer stopped.")
        return

if __name__ == "__main__":
    try:
        parser = argparse.ArgumentParser(description='PyFocusTime - Your Pomodoro Timer')
        parser.add_argument('-f', '--focus', type=float, default=25,
                          help='Focus time duration in minutes (default: 25)')
        parser.add_argument('-b', '--break-time', type=float, default=5,
                          help='Break time duration in minutes (default: 5)')
        
        args = parser.parse_args()
        
        print("Welcome to PyFocusTime - Your Pomodoro Timer!")
        print(f"Settings: {args.focus} minutes focus + {args.break_time} minutes break")
        pomodoro_timer(focus_time=args.focus, break_time=args.break_time)
    except KeyboardInterrupt:
        print("\n\nGoodbye! Pomodoro Timer stopped.")