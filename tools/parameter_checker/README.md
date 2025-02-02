# Parameter Checker Tool

A tool for comparing molecular parameters between MDF files and CHARMM parameter files to identify missing or mismatched parameters.

## Features

- Compare parameters between MDF and CHARMM files:
  - Atom types and charge groups
  - Bonds
  - Angles
  - Dihedrals
- Support for CHARMM wildcards ('X')
- Save intermediate parsing results
- Flexible output formats (CSV/JSON)
- Detailed logging and reporting

## Usage

### Command Line

```bash
topology-parser check mdf_file.mdf charmm_file.prm [options]
```

Options:
- `-o, --output`: Output file name (default: missing_parameters.csv)
- `-d, --output-dir`: Output directory for all files
- `--save-all`: Save intermediate files from MDF and CHARMM parsing
- `--json`: Output as JSON instead of CSV
- `--verbose`: Enable detailed output
- `--log`: Save logs to specified file

### Python API

```python
from tools.parameter_checker import main as checker_main

result = checker_main(
    mdf_file="input.mdf",
    charmm_file="params.prm",
    output_file="results.csv",
    output_dir="output",
    save_all=True,
    json_format=False,
    verbose=True
)
```

## Output Format

### CSV Format
The tool generates a CSV file with parameter comparison results:

```csv
parameter_type,parameters,found,line_number
atom,CG1,true,15
bond,CG1-CG2,false,
angle,CG1-CG2-CG3,true,45
dihedral,CG1-CG2-CG3-CG4,true,78
```

### JSON Format
When using --json, the output is structured as:

```json
[
  {
    "parameter_type": "atom",
    "parameters": "CG1",
    "found": true,
    "line_number": 15
  },
  {
    "parameter_type": "bond",
    "parameters": "CG1-CG2",
    "found": false,
    "line_number": null
  }
]
```

## Parameter Matching

The tool performs intelligent parameter matching:

1. Atoms
   - Direct matching of atom types/charge groups
   - Support for CHARMM wildcards

2. Bonds
   - Bidirectional matching (A-B = B-A)
   - Wildcard support in CHARMM parameters

3. Angles
   - Symmetric matching (A-B-C = C-B-A)
   - Central atom preservation
   - Wildcard support

4. Dihedrals
   - Forward/reverse matching
   - Wildcard support
   - Proper handling of multiplicity

## Intermediate Files

When using --save-all:

1. MDF parsing results:
   - output_dir/mdf_topology.csv

2. CHARMM parsing results:
   - output_dir/charmm/ATOMS.csv
   - output_dir/charmm/BONDS.csv
   - output_dir/charmm/ANGLES.csv
   - output_dir/charmm/DIHEDRALS.csv
   - output_dir/charmm/IMPROPER.csv

## Error Handling

The tool includes comprehensive error handling for:
- Missing or invalid input files
- Parameter parsing errors
- Output directory/file issues
- Invalid parameter comparisons

All errors are logged with detailed context for debugging.
