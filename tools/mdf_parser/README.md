# MDF Parser Tool

A specialized parser for Molecular Data Format (MDF) files that extracts molecular topology information.

## Features

- Parse MDF file format and extract:
  - Atom information and charge groups
  - Molecular connectivity
  - Bond, angle, and dihedral relationships
- Generate structured topology data
- Flexible output options:
  - CSV or JSON format
  - Combined or separate component files
  - Detailed logging capabilities

## Usage

### Command Line

```bash
topology-parser mdf input.mdf -o topology.csv [options]
```

Options:
- `-o, --output`: Output file name (default: topology.csv)
- `--json`: Output in JSON format instead of CSV
- `--separate`: Save separate files for each component
- `--verbose`: Enable detailed output
- `--log`: Save logs to specified file

### Python API

```python
from tools.mdf_parser import parse_mdf_file, extract_topology, save_output

# Parse MDF file
atoms_data = parse_mdf_file("input.mdf")

# Extract topology information
bonds, angles, dihedrals = extract_topology(atoms_data)

# Save results
save_output("output.csv", atoms_data, json_format=False, separate_files=True)
```

## Output Format

### CSV Format
The tool generates CSV files with the following structure:

```csv
record_type,atom_identifiers,data1,data2,data3,data4
atom,[MOL:1:C1],CG1,,,
bond,[MOL:1:C1-MOL:1:C2],CG1,CG1,,
angle,[MOL:1:C1-MOL:1:C2-MOL:1:C3],CG1,CG1,CG2,
dihedral,[MOL:1:C1-MOL:1:C2-MOL:1:C3-MOL:1:C4],CG1,CG1,CG2,CG2
```

### JSON Format
When using --json, the output is structured as:

```json
[
  {
    "record_type": "atom",
    "atom_identifiers": ["MOL:1:C1"],
    "data1": "CG1",
    "data2": "",
    "data3": "",
    "data4": ""
  },
  ...
]
```

## Error Handling

The parser includes comprehensive error handling for:
- Missing or invalid input files
- Malformed MDF content
- Invalid molecular connectivity
- Output file writing errors

All errors are logged with appropriate context for debugging.
