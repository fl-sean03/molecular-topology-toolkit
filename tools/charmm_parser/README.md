# CHARMM Parameter File Parser

A specialized parser for CHARMM force field parameter files that extracts and organizes molecular force field parameters.

## Features

- Parse CHARMM parameter (.prm) files:
  - ATOMS section (mass and type)
  - BONDS section
  - ANGLES section
  - DIHEDRALS section
  - IMPROPERS section
- Preserve comments and metadata
- Support for wildcards ('X') in parameters
- Structured output in CSV or JSON format
- Detailed logging capabilities

## Usage

### Command Line

```bash
topology-parser charmm input.prm -o output_dir [options]
```

Options:
- `-o, --output_dir`: Output directory (default: current directory)
- `--json`: Output in JSON format instead of CSV
- `--verbose`: Enable detailed output
- `--log`: Save logs to specified file

### Python API

```python
from tools.charmm_parser import CharmmProcessor

# Initialize processor
processor = CharmmProcessor()

# Process file
data = processor.process_file("input.prm", "output_dir", json_format=False)
```

## Output Format

### CSV Format
The tool generates separate CSV files for each parameter type:

ATOMS.csv:
```csv
Force Field Type,Mass,Comments,Line Number
H,1.008,Hydrogen,1
C,12.011,Carbon,2
```

BONDS.csv:
```csv
Atom 1,Atom 2,Force Constant (Kb),Equilibrium Bond Length (b0),Comments,Line Number
H,C,340.0,1.090,Aliphatic CH,5
```

### JSON Format
When using --json, each section is saved as a JSON file:

ATOMS.json:
```json
[
  {
    "Force Field Type": "H",
    "Mass": 1.008,
    "Comments": ["Hydrogen"],
    "Line Number": 1
  }
]
```

## Parameter Sections

The parser handles these CHARMM parameter sections:

1. ATOMS
   - Force field type
   - Atomic mass
   - Comments

2. BONDS
   - Atom types (2)
   - Force constant (Kb)
   - Equilibrium length (b0)
   - Comments

3. ANGLES
   - Atom types (3)
   - Force constant (Ktheta)
   - Equilibrium angle (Theta0)
   - Urey-Bradley term (optional)
   - Comments

4. DIHEDRALS
   - Atom types (4)
   - Force constant (Kchi)
   - Multiplicity (n)
   - Phase shift (delta)
   - Comments

5. IMPROPERS
   - Atom types (4)
   - Force constant (Kpsi)
   - Equilibrium improper angle (Psi0)
   - Comments

## Error Handling

The parser includes robust error handling for:
- Missing or invalid input files
- Malformed parameter sections
- Invalid parameter values
- Output directory/file writing issues

All errors are logged with appropriate context for debugging.
