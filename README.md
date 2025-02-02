# Molecular Topology Toolkit

A comprehensive Python toolkit for computational chemistry and materials science, providing tools for molecular topology analysis, force field parameter handling, and more.

## Table of Contents

- [Overview](#overview)
- [Quick Start](#quick-start)
  - [Installation](#installation)
  - [Basic Usage](#basic-usage)
- [Requirements](#requirements)
- [Development](#development)
  - [Setup Development Environment](#setup-development-environment)
  - [Code Style](#code-style)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgments](#acknowledgments)

## Overview

This toolkit provides a growing collection of tools for computational chemistry and materials science:

### Current Tools

1. [MDF Parser](tools/mdf_parser/README.md)
   - Parse Molecular Data Format files
   - Extract topology information
   - Generate structured molecular data

2. [CHARMM Parser](tools/charmm_parser/README.md)
   - Parse CHARMM parameter files
   - Extract force field parameters
   - Organize molecular force field data

3. [Parameter Checker](tools/parameter_checker/README.md)
   - Compare MDF and CHARMM parameters
   - Identify missing parameters
   - Validate molecular force fields

### Future Tools

The toolkit is designed to expand with additional tools for:
- Molecular dynamics analysis
- Structure visualization
- Force field parameterization
- Property prediction
- And more...

## Quick Start

### Installation

```bash
# Clone the repository
git clone https://github.com/fl-sean03/molecular-topology-toolkit.git
cd molecular-topology-toolkit

# Install dependencies
pip install -r requirements.txt

# Install package
pip install -e .
```

### Basic Usage

The toolkit provides a unified command-line interface:

```bash
# MDF Parser
moltopkit mdf input.mdf -o topology.csv

# CHARMM Parser
moltopkit charmm params.prm -o output_dir

# Parameter Checker
moltopkit check input.mdf params.prm -d output --save-all
```

See individual tool READMEs for detailed usage instructions.

## Requirements

- Python 3.6+
- pandas >= 1.3.0
- rich >= 10.0.0

Additional development requirements:
- pytest >= 6.0.0
- coverage >= 6.0.0
- black >= 22.0.0
- flake8 >= 4.0.0
- sphinx >= 4.0.0

## Development

### Setup Development Environment

```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

# Install development dependencies
pip install -r requirements.txt
```


### Code Style

The project follows PEP 8 guidelines with some modifications:
- Line length: 100 characters
- Uses Black for code formatting
- Sorted imports using isort

Format code before committing:
```bash
black .
isort .
```

## Project Structure

```
molecular-topology-toolkit/
├── tools/
│   ├── __init__.py
│   ├── cli.py
│   ├── mdf_parser/      # MDF file parsing
│   │   ├── __init__.py
│   │   ├── README.md
│   │   ├── parser.py
│   │   ├── mdf_parser.py
│   │   ├── topology.py
│   │   ├── output_handler.py
│   │   └── tests/
│   │       └── test_mdf_parser.py
│   ├── charmm_parser/   # CHARMM parameter parsing
│   │   ├── __init__.py
│   │   ├── README.md
│   │   ├── parser.py
│   │   ├── parsers.py
│   │   └── tests/
│   │       └── test_charmm_parser.py
│   └── parameter_checker/# Parameter comparison
│       ├── __init__.py
│       ├── README.md
│       └── parameter_checker.py
├── docs/
│   └── development/    # Development guidelines
│       ├── adding_new_tools.md
│       ├── coding_standards.md
│       └── modularity_guidelines.md
├── CONTRIBUTING.md     # Contribution guidelines
├── LICENSE            # MIT License
├── README.md         # Project documentation
├── requirements.txt  # Project dependencies
├── pyproject.toml   # Build configuration
└── setup.py         # Package configuration
```

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Run tests and ensure they pass
4. Format code using Black and isort
5. Commit your changes (`git commit -m 'Add amazing feature'`)
6. Push to the branch (`git push origin feature/amazing-feature`)
7. Open a Pull Request

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct and the process for submitting pull requests.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Thanks to all contributors who have helped shape this project
- Special thanks to the molecular modeling community for their input and feedback
