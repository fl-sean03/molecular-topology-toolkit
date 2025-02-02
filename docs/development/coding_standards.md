# Coding Standards

This document outlines the coding standards for contributing to the molecular topology parser project.

## Python Version

- Target Python 3.6+ compatibility
- Use type hints (PEP 484)
- Use f-strings for string formatting

## Code Style

### General

- Follow PEP 8 with modifications:
  - Line length: 100 characters
  - Use Black for formatting
  - Use isort for import sorting

### Imports

```python
# Standard library imports first
import os
import sys
from typing import Dict, List, Optional

# Third-party imports
import pandas as pd
from rich.console import Console

# Local imports
from ..utils import common_functions
```

### Documentation

- Docstrings: Google style
```python
def process_file(filepath: str) -> Dict[str, pd.DataFrame]:
    """
    Process input file and return structured data.
    
    Args:
        filepath: Path to the input file
        
    Returns:
        Dictionary mapping section names to DataFrames
        
    Raises:
        FileNotFoundError: If file doesn't exist
        ValueError: If file is malformed
    """
```

### Type Hints

- Use type hints consistently
```python
from typing import Dict, List, Optional, Union

def parse_section(
    lines: List[str],
    start_line: int = 0
) -> Optional[pd.DataFrame]:
```

### Error Handling

```python
try:
    result = process_data()
except FileNotFoundError as e:
    logging.error(f"File not found: {str(e)}")
    raise
except ValueError as e:
    logging.error(f"Invalid data format: {str(e)}")
    raise
except Exception as e:
    logging.error(f"Unexpected error: {str(e)}")
    raise
```

### Classes

```python
class DataProcessor:
    """
    Process and analyze data files.
    
    Attributes:
        current_data: Currently loaded data
        filepath: Path to current file
    """
    
    def __init__(self) -> None:
        self.current_data: Dict[str, pd.DataFrame] = {}
        self.filepath: Optional[str] = None
        
    def process_file(self, filepath: str) -> None:
        """Process input file."""
        pass
```

### Constants

```python
# Top of file, after imports
DEFAULT_OUTPUT = 'output.csv'
MAX_RETRIES = 3
SECTION_PATTERNS = {
    'ATOMS': r'^ATOMS',
    'BONDS': r'^BONDS',
}
```

## Testing

### Test Structure

```python
class TestYourTool(unittest.TestCase):
    def setUp(self) -> None:
        """Set up test fixtures."""
        self.processor = YourToolProcessor()
        
    def tearDown(self) -> None:
        """Clean up test fixtures."""
        pass
        
    def test_successful_case(self) -> None:
        """Test normal operation."""
        result = self.processor.process_file('test.txt')
        self.assertIsInstance(result, dict)
        
    def test_error_case(self) -> None:
        """Test error handling."""
        with self.assertRaises(ValueError):
            self.processor.process_file('invalid.txt')
```

### Test Coverage

- Aim for 80%+ coverage
- Test edge cases and error conditions
- Use meaningful test data

## Logging

```python
import logging

def setup_logging(verbose: bool = False) -> None:
    """Configure logging based on verbosity."""
    level = logging.DEBUG if verbose else logging.INFO
    logging.basicConfig(
        level=level,
        format='%(levelname)s: %(message)s'
    )
```

## Performance Considerations

- Use generators for large datasets
- Avoid unnecessary copies of large data structures
- Profile code when performance is critical

## Security

- Validate all file paths
- Sanitize user input
- Use secure defaults

## Version Control

### Commit Messages

```
type: Brief description

Detailed description of changes and reasoning.

- Bullet points for specific changes
- Another change

Fixes #123
```

Types:
- feat: New feature
- fix: Bug fix
- docs: Documentation
- style: Formatting
- refactor: Code restructuring
- test: Adding tests
- chore: Maintenance

### Branches

- main: Stable releases
- develop: Development
- feature/name: New features
- fix/issue-num: Bug fixes

## Code Review Checklist

- [ ] Follows coding standards
- [ ] Includes tests
- [ ] Documentation updated
- [ ] Error handling implemented
- [ ] Logging added
- [ ] Type hints used
- [ ] Performance considered
- [ ] Security reviewed
