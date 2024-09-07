# Package Checker for ARM64 Compatibility

This script checks if the installed packages on a given Ubuntu version have a compatible ARM64 version. It reads from a list of installed packages, makes HTTP requests to the Ubuntu package repository, and checks if the package exists for the selected architecture (ARM64).

## Features

- Checks if packages from Ubuntu repositories have ARM64 versions.
- Allows the user to select the Ubuntu version they want to search in (up to Ubuntu 24.04).
- Provides progress updates and only lists packages that do not have ARM64 versions.
- Detailed instructions on generating the list of installed packages for use in the script.

## Requirements

- Python 3.x
- `requests` library

## Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/sahb/armchecker.git
   cd armchecker
   ```

2. Install the required Python libraries:

   ```bash
   pip install -r requirements.txt
   ```

   Or manually install the `requests` library:

   ```bash
   pip install requests
   ```

## Usage

1. **Generate the list of installed packages**:
   - Open your terminal on an Ubuntu system.
   - Run the following command to generate a list of installed packages:
     ```bash
     dpkg --get-selections | awk '{print $1}' > installed_packages.txt
     ```
   - This will create a file named `installed_packages.txt` with all installed packages.

2. **Run the script**:
   - Run the Python script and provide the path to the file containing the list of packages:
     ```bash
     python arm64Checker.py
     ```
3. **Inform the path to the file with the list of packages**
   - From the instructions above, it will be `installed_packages.txt`

3. **Select the Ubuntu version**:
   - The script will ask you to choose the Ubuntu version by presenting a list of available versions up to 24.04.

4. **View results**:
   - The script will show the number of packages processed and list any packages that do not have an ARM64 version available.



