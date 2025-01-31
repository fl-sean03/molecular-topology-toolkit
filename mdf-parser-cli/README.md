# MDF Parser CLI Tool

A command-line application for parsing `.mdf` files and extracting molecular topology information. The tool provides structured outputs in CSV or JSON format with comprehensive logging capabilities.

## Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Unit Tests](#unit-tests)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)
- [Future Improvements](#future-improvements)
- [Authors](#authors)
- [Acknowledgments](#acknowledgments)

## Features

- Parse MDF files to extract molecular topology
- Output in CSV or JSON formats
- Extract bonds, angles, and dihedrals from molecular data
- Improved error handling with detailed messages
- Configurable logging with verbosity levels
- Verbose mode for detailed information
- Option to separate output into multiple files

## Installation

### Prerequisites

- Python **3.10** or higher
- pip package manager

### Virtual Environment (Optional)

It's recommended to use a virtual environment to manage dependencies:

```bash
python3 -m venv venv
source venv/bin/activate
```

### Setup

1. Clone the repository:
```bash
git clone https://github.com/fl-sean03/mdf-parser-cli.git
cd mdf-parser-cli
```

2. Install required dependencies:
```bash
pip install -r requirements.txt
```

## Usage

Basic usage:
```bash
python mdf_parser.py input.mdf -o output.csv
```

### Command Line Options

- `input_file`: Path to the .mdf file (required)
- `-o, --output`: Output file name (default: topology.csv)
- `--json`: Output as JSON instead of CSV
- `--separate`: Save separate CSVs for atoms, bonds, angles, dihedrals
- `--verbose`: Enable detailed output
- `--log`: Save logs to a specified file

### Examples

Output as JSON with verbose logging:
```bash
python mdf_parser.py molecule.mdf -o topology.json --json --verbose --log parser.log
```

Save separate files with logging:
```bash
python mdf_parser.py molecule.mdf --separate --log parser.log
```

### Logging

Use the `--log` option to save log outputs to a file. Logs include detailed information useful for debugging.

Example:
```bash
python mdf_parser.py input.mdf --log logs/parser.log
```

Logs will be saved in the `logs/` directory.

## Building Executable

To create a standalone executable:

1. Install PyInstaller:
```bash
pip install pyinstaller
```

2. Build the executable:
```bash
python build_exe.py
```

The executable will be available in the `dist` directory.

## Project Structure

```
mdf-parser-cli/
│── mdf_parser.py           # Main CLI script
│── parser/                 # Module for parsing logic
│   ├── __init__.py         # Package marker
│   ├── mdf_parser.py       # Core parsing logic
│   ├── topology.py         # Bonds, angles, dihedral extraction
│   └── output_handler.py   # Handles CSV/JSON output
│── logs/                   # Stores logs if user enables logging
│── tests/                  # Unit tests
│── requirements.txt        # Dependencies
│── README.md              # Project documentation
│── setup.py               # Packaging configuration
│── build_exe.py           # Script to convert to .exe
│── LICENSE                # MIT License file
```

## Contributing

Contributions are welcome! Please follow these steps:

1. **Fork** the repository on GitHub.
2. **Clone** your fork locally.
3. **Create a new branch** for your feature or bugfix:
   ```bash
   git checkout -b feature/your-feature-name
   ```
4. **Commit** your changes with descriptive messages.
5. **Push** your branch to your fork:
   ```bash
   git push origin feature/your-feature-name
   ```
6. **Create a Pull Request** on the main repository.

Please ensure that your code adheres to the project's coding standards and passes all unit tests.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Future Improvements

- Implement parallel processing for parsing large MDF files
- Add support for dihedral angle calculations
- Integration with other molecular dynamics tools and formats
- CHARMM parameter integration
- GUI or web interface
- Support for additional file formats (GROMACS .top, .itp)

## Authors

- Sean Florez - [@fl-sean03](https://github.com/fl-sean03)

## Acknowledgments

- Thanks to contributors and users of the tool
- Inspired by molecular dynamics simulation needs
