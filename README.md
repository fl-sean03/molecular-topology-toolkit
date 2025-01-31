# Molecular Topology Parser Tools

A Python toolkit for parsing and analyzing molecular topology files in CHARMM parameter and MDF formats.

## Features

- Parse CHARMM parameter files (.prm)
  - Extract bonds, angles, dihedrals, and improper parameters
  - Support for comments and metadata
  - Output to CSV or JSON formats
  
- Parse MDF (Molecular Data Format) files
  - Extract molecular topology information
  - Generate bond, angle, and dihedral connectivity
  - Support for charge groups
  - Output to CSV or JSON formats

## Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/molecular-topology-parser.git
cd molecular-topology-parser

# Install dependencies
pip install pandas rich
```

## Usage

The toolkit provides a unified command-line interface for both parsers:

### CHARMM Parameter File Parser

```bash
./cli.py charmm input.prm -o output_dir --json --verbose
```

Options:
- `input.prm`: Path to CHARMM parameter file
- `-o/--output_dir`: Output directory (default: current directory)
- `--json`: Output in JSON format instead of CSV
- `--verbose`: Enable detailed output
- `--log`: Save logs to specified file

### MDF File Parser

```bash
./cli.py mdf input.mdf -o topology.csv --json --separate --verbose
```

Options:
- `input.mdf`: Path to MDF file
- `-o/--output`: Output file name (default: topology.csv)
- `--json`: Output in JSON format instead of CSV
- `--separate`: Save separate files for each component
- `--verbose`: Enable detailed output
- `--log`: Save logs to specified file

## API Usage

### CHARMM Parser

```python
from tools.charmm_parser import CharmmProcessor

processor = CharmmProcessor()
data = processor.process_file("input.prm", "output_dir")
```

### MDF Parser

```python
from tools.mdf_parser import parse_mdf_file, extract_topology, save_output

# Parse MDF file
atoms_data = parse_mdf_file("input.mdf")

# Extract topology
bonds, angles, dihedrals = extract_topology(atoms_data)

# Save results
save_output("output.csv", atoms_data, json_format=False, separate_files=True)
```

## Testing

Run the test suite:

```bash
python -m unittest discover tests
```

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.
