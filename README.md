# Traffic Light Simulation

A Python-based interactive traffic light simulation using the Turtle graphics library. This program creates a visual representation of traffic lights for both vehicles and pedestrians, complete with realistic timing sequences.

## Description

This simulation creates two traffic light boxes:
- A main traffic light for vehicles with red, yellow, and green signals
- A pedestrian traffic light with red and green signals

The lights change automatically in a continuous cycle, mimicking real-world traffic light behavior.

## Features

- Real-time light transitions
- Timed sequences matching typical traffic patterns
- Visual representation using Turtle graphics
- Black background for better visibility
- Two synchronized traffic light systems
- Infinite loop simulation

## Prerequisites

To run this simulation, you need:
- Python 3.x
- Python Turtle graphics library (included in standard Python installation)
- `time` module (included in standard Python installation)

## Installation

1. Clone or download the code to your local machine
2. Save it as `traffic_light.py` (or any preferred name with `.py` extension)
3. Make sure you have Python installed on your system

## Usage

1. Open your terminal/command prompt
2. Navigate to the directory containing the script
3. Run the script using Python:
   ```bash
   python traffic_light.py
   ```

## Light Sequence Timing

The simulation follows this timing sequence:
1. Initial state: Vehicle red light (2 seconds)
2. Vehicle green light (10 seconds)
3. Vehicle yellow light (3.5 seconds)
4. Vehicle red light with pedestrian green light (10 seconds)
5. Sequence repeats

## Technical Details

### Components
- Main traffic light dimensions: 60x120 pixels
- Pedestrian light dimensions: 60x90 pixels
- Circle shapes for light indicators
- Color states: red, yellow, green, and grey (off state)

### Light States
- Grey: Light is off
- Colored: Light is active
- Vehicle traffic light: Red → Green → Yellow → Red
- Pedestrian traffic light: Red → Green → Red

## Controls

The simulation runs automatically once started. To exit:
1. Close the Turtle graphics window
2. Use Ctrl+C in the terminal (if needed)

## Customization

You can modify these parameters in the code:
- Timing sequences (by changing the `seconds` variables)
- Light colors (by modifying the `color()` values)
- Box dimensions (by adjusting the `fd()` and `rt()` values)
- Circle sizes (using `shapesize()`)

## Known Limitations

- The simulation runs indefinitely until manually stopped
- Window size is fixed
- No interactive controls during runtime

## Contributing

Feel free to fork this project and submit improvements via pull requests. Some areas for potential enhancement:
- Adding interactive controls
- Implementing keyboard shortcuts
- Adding sound effects
- Creating multiple intersection support

## License

This project is available for educational and personal use.

## Author's Note

This simulation is designed for educational purposes to demonstrate the use of:
- Turtle graphics in Python
- Time-based programming
- State management
- Infinite loops with conditions
