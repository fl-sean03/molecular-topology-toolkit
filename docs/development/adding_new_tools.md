# Adding New Tools to the Project

This guide explains how to add new tools to the computational chemistry and materials science toolkit while maintaining consistency and quality.

## Directory Structure

New tools should follow this structure:

```
tools/
└── your_tool_name/
    ├── __init__.py
    ├── README.md
    ├── main.py         # Main functionality
    ├── core.py         # Core algorithms/computations
    ├── io.py          # Input/output handling
    └── utils.py       # Utility functions
```

## Step-by-Step Guide

1. Create Tool Directory
```bash
mkdir tools/your_tool_name
touch tools/your_tool_name/__init__.py
touch tools/your_tool_name/README.md
```

2. Update Project Files
- Add tool to `tools/__init__.py`
- Update `setup.py` with new dependencies
- Add tool to CLI in `tools/cli.py`
- Create tests in `tests/test_your_tool.py`

3. Implement Core Functionality
- Create main parser/processor class
- Follow existing error handling patterns
- Use typing hints and docstrings
- Add logging support

## Code Standards

### Imports
```python
# Standard library imports
import os
import logging
from typing import Dict, List

# Third-party imports
import pandas as pd
from rich.console import Console

# Local imports
from ..utils import setup_logging
```

### Class Structure
```python
class YourToolProcessor:
    """
    Main class for processing tool-specific files.
    
    Attributes:
        current_data: Dictionary storing processed data
    """
    def __init__(self):
        self.current_data: Dict = {}
        
    def process_file(self, filepath: str) -> Dict:
        """Process input file and return results."""
        pass
```

### Error Handling
```python
try:
    result = process_data()
except FileNotFoundError:
    logging.error("Input file not found")
    raise
except Exception as e:
    logging.error(f"Unexpected error: {str(e)}")
    raise
```

## CLI Integration

1. Add subparser in `tools/cli.py`:
```python
your_tool = subparsers.add_parser('your-tool', help='Your tool description')
your_tool.add_argument('input_file', help='Path to input file')
your_tool.add_argument('-o', '--output', help='Output file')
```

2. Add command handling:
```python
elif args.command == 'your-tool':
    from .your_tool.parser import main as your_tool_main
    return your_tool_main(
        input_file=args.input_file,
        output_file=args.output
    )
```

## Testing

1. Create test file:
```python
import unittest
from tools.your_tool import YourToolProcessor

class TestYourTool(unittest.TestCase):
    def setUp(self):
        self.processor = YourToolProcessor()
        
    def test_basic_functionality(self):
        result = self.processor.process_file('test_file.txt')
        self.assertIsInstance(result, dict)
```

2. Add test data in `tests/data/`

## Documentation

1. Tool README.md should include:
- Feature overview
- Usage examples
- Input/output formats
- Error handling
- API documentation

2. Update main README.md with tool description

## Integration Checklist

- [ ] Tool directory structure created
- [ ] Core functionality implemented
- [ ] Tests written and passing
- [ ] CLI integration complete
- [ ] Documentation updated
- [ ] Dependencies added to setup.py
- [ ] Code formatting (black, isort)
- [ ] Type hints and docstrings
- [ ] Error handling implemented
- [ ] Logging added
