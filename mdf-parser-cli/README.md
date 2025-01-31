# MDF Parser CLI Tool

A command-line application for parsing `.mdf` files and extracting molecular topology information. The tool provides structured outputs in CSV or JSON format and supports logging and verbosity options.

## Features

- Parse MDF files to extract molecular topology
- Output in CSV or JSON formats
- Extract bonds, angles, and dihedrals
- Colorized output support using Rich
- Configurable logging
- Verbose mode for detailed information
- Option to separate output into multiple files

## Installation

### Prerequisites

- Python 3.10 or higher
- pip package manager

### Setup

1. Clone the repository:
```bash
git clone https://github.com/yourusername/mdf-parser-cli.git
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
- `--rich`: Enable colorized output
- `--log`: Save logs to a specified file

### Examples

Output as JSON with verbose logging:
```bash
python mdf_parser.py molecule.mdf -o topology.json --json --verbose
```

Save separate files with logging:
```bash
python mdf_parser.py molecule.mdf --separate --log parser.log
```

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
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Future Improvements

- Parallel processing for large .mdf files
- CHARMM parameter integration
- GUI or web interface
- Support for additional file formats (GROMACS .top, .itp)

## Authors

- Your Name (@yourusername)

## Acknowledgments

- Thanks to contributors and users of the tool
- Inspired by molecular dynamics simulation needs
