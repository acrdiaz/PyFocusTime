# PyFocusTime

A simple focus timer application written in Python that helps you stay productive using timed focus and break sessions.

## Features
- Customizable focus and break durations
- Audio notifications (Windows) / System notifications (Linux/MacOS)
- Command-line interface
- Cross-platform support (Windows, Linux, MacOS)
- Reminder notifications if you don't respond after a break

## Requirements
- Python 3.6 or higher
- No external packages required!

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/PyFocusTime.git
   cd PyFocusTime
   ```

2. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the timer with default settings (25-minute focus + 5-minute break):
```bash
python main.py
```

The application will:
1. Start a 25-minute focus session
2. Play a beep sound when the focus session ends
3. Begin a 5-minute break
4. Play a beep sound when the break is over
5. Ask if you want to start another session

## How It Works

PyFocusTime follows the Pomodoro Technique:
1. Work focused for 25 minutes
2. Take a short 5-minute break
3. Repeat the cycle

The application shows a real-time countdown and sends desktop notifications to help you stay on track with your work/break cycles.

## Contributing

Contributions are welcome! Feel free to submit issues and pull requests.

## License

This project is open source and available under the MIT License.