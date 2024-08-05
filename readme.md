# Moon Phases Script
## Table of Contents

- [Introduction](#introduction)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Example](#example)

## Introduction

This script generates and processes images showing the moon phase for a given date. It integrates with the Busy Tag device to save the images to a specified drive. 

## Project Purpose

The main goal of this project is to:
	
- Fetch moon phase data from an online API.

- Convert the SVG to a PNG image.

- Crop, overlay, and add text to the image.

- Save the final image to a Busy Tag device.


## Prerequisites

To run this script, ensure you have the following installed:

- Python 3.6 or higher
- `Pillow` (PIL Fork) - Python Imaging Library
- `html2image` for converting HTML to PNG
- `requests` for API calls
- A Busy Tag device connected to your computer.

## Installation
 
  To get started with this Python script, follow these steps:

1. **Clone the repository:**
   First, clone the repository from GitHub to your local machine.
   ```
   git clone https://github.com/busy-tag/Moon_Phases_Script.git
2. Navigate to the cloned repository:

	```
	cd cd Moon_Phases_Script
	```
3. Install the required dependencies:
	Use `pip` to install the necessary packages.
	
	```
	pip install pillow html2image requests
	```

4. Ensure the default font file `MontserratBlack-3zOvZ.ttf` is in the project directory.

## Configuration

The script provides several customizable parameters:
 
• **Drive Letter:** Prompted input for the drive letter where the Busy Tag device is located (e.g., `D`).

• **Date:** Prompted input for the date or use the current system date.

• **SVG Generation:** Customize the SVG parameters such as size and colors in moon_config.py.

• **Image Processing:** Parameters for cropping, overlaying, and adding text are set in image_operations.py.


## Usage
1. **Execute the script:**
You can run the script from the command line:
```
python main.py
```
2. **Provide Drive Letter:**
   
    The script will prompt you to enter the drive letter assigned to the Busy Tag device. Enter the letter (e.g., `D`) and press Enter.
         
3. **Provide date:**

	Enter a date in DD/MM/YYYY format or press Enter to use the current date.
	
4. **Script Operation::**
	
	The script will generate an image of the moon phase for the given date and save it to the Busy Tag device. The image will include the moon phase, date, and additional text annotations.

5. **Output:**
	
	The generated image will be saved in the specified directory (e.g., D:) and will include the moon phase along with the date and waning value.

	
### Example

After running the script, you should see output similar to this in your terminal:
```
Is the Busy Tag device connected to your computer? (yes/no): y
Please enter the drive letter assigned to Busy Tag device (e.g., D): D
Enter a date (DD/MM/YYYY) or press Enter to use the current system date: 24/08/2024
28532 bytes written to file D:\moon_phase.png
Process completed successfully.
```

An image (e.g., moon_phase.png) will be saved in the specified directory (e.g., D:), displaying the moon phase for the specified date.
Sample:

<img src="/moon_phases_sample.png" alt="Sample Moon Phase Image" width="480" height="560"/>

### Troubleshooting ###

If you encounter any issues, ensure:

All Python packages are installed correctly.

The font file (`MontserratBlack-3zOvZ.ttf`) is present in the project directory.

You have an active internet connection.

The drive letter is correct and the Busy Tag device is connected.

The date format is correct if manually entered.

For any additional help, please open an issue in the repository or contact the maintainer.
