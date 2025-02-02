# Molecular Topology Parser Tools

A comprehensive Python toolkit for analyzing and comparing molecular topology files, supporting CHARMM parameter files and Molecular Data Format (MDF) files.

## Overview

This toolkit provides three main tools:

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

## Quick Start

### Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/molecular-topology-parser.git
cd molecular-topology-parser

# Install dependencies
pip install -r requirements.txt

# Install package
pip install -e .
```

### Basic Usage

The toolkit provides a unified command-line interface:

```bash
# MDF Parser
topology-parser mdf input.mdf -o topology.csv

# CHARMM Parser
topology-parser charmm params.prm -o output_dir

# Parameter Checker
topology-parser check input.mdf params.prm -d output --save-all
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

### Running Tests

```bash
# Run all tests
python -m pytest

# Run with coverage
python -m pytest --cov=tools

# Run specific test file
python -m pytest tests/test_mdf_parser.py
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
molecular-topology-parser/
├── tools/
│   ├── mdf_parser/      # MDF file parsing
│   ├── charmm_parser/   # CHARMM parameter parsing
│   └── parameter_checker/# Parameter comparison
├── tests/
│   ├── data/           # Test data files
│   └── test_*.py       # Test modules
├── docs/               # Documentation
├── requirements.txt    # Project dependencies
└── setup.py           # Package configuration
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
