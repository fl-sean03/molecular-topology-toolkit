# Modularity Guidelines

This document outlines the principles and practices for maintaining modularity in the molecular topology parser project.

## Module Organization

### Directory Structure
```
tools/
├── __init__.py
├── cli.py
└── your_tool/
    ├── __init__.py
    ├── parser.py
    ├── processors.py
    └── utils.py
```

### Module Responsibilities

1. `__init__.py`
- Export public interface
- Version information
- Import commonly used classes/functions

2. `parser.py`
- Main entry point
- High-level processing logic
- Command-line interface integration

3. `processors.py`
- Core data processing classes
- File parsing logic
- Data transformation

4. `utils.py`
- Helper functions
- Shared utilities
- Common constants

## Interface Design

### Public Interface
```python
# __init__.py
from .parser import main
from .processors import YourToolProcessor

__all__ = ['main', 'YourToolProcessor']
```

### Class Interface
```python
class YourToolProcessor:
    """Process tool-specific files."""
    
    def __init__(self):
        self._initialize()
    
    def process_file(self, filepath: str) -> Dict:
        """Public method for file processing."""
        pass
        
    def _initialize(self):
        """Private initialization method."""
        pass
```

## Dependency Management

### Internal Dependencies
```python
# Relative imports for internal modules
from ..utils import common
from .processors import DataProcessor
```

### External Dependencies
```python
# setup.py
setup(
    name='your_tool',
    install_requires=[
        'pandas>=1.3.0',
        'rich>=10.0.0',
    ],
    extras_require={
        'dev': [
            'pytest>=6.0.0',
            'black>=22.0.0',
        ],
    }
)
```

## Integration Points

### CLI Integration
```python
# cli.py
def main():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers()
    
    # Add your tool's subparser
    your_tool = subparsers.add_parser('your-tool')
    your_tool.add_argument('input_file')
```

### Data Exchange
```python
# Define clear data structures for inter-module communication
from dataclasses import dataclass
from typing import Dict, List

@dataclass
class ProcessingResult:
    """Standard result format for tool output."""
    data: Dict
    metadata: Dict
    errors: List[str]
```

## Testing Strategy

### Unit Tests
```python
# test_processors.py
def test_processor_initialization():
    processor = YourToolProcessor()
    assert processor.is_initialized()

def test_file_processing():
    processor = YourToolProcessor()
    result = processor.process_file('test.txt')
    assert isinstance(result, ProcessingResult)
```

### Integration Tests
```python
# test_integration.py
def test_end_to_end():
    """Test complete processing pipeline."""
    input_file = 'test.txt'
    output_file = 'output.csv'
    
    result = process_complete_pipeline(
        input_file,
        output_file
    )
    
    assert result.success
```

## Error Handling

### Error Types
```python
class ToolError(Exception):
    """Base error for your tool."""
    pass

class ProcessingError(ToolError):
    """Error during file processing."""
    pass

class ValidationError(ToolError):
    """Error during data validation."""
    pass
```

### Error Propagation
```python
def process_file(filepath: str) -> Dict:
    try:
        data = read_file(filepath)
        result = process_data(data)
        return result
    except FileNotFoundError:
        raise ProcessingError(f"File not found: {filepath}")
    except ValueError as e:
        raise ValidationError(f"Invalid data: {str(e)}")
```

## Configuration Management

### Settings
```python
# config.py
from dataclasses import dataclass

@dataclass
class ToolConfig:
    """Tool configuration settings."""
    output_dir: str = 'output'
    max_retries: int = 3
    verbose: bool = False
```

### Environment Variables
```python
import os

class Config:
    """Environment-based configuration."""
    OUTPUT_DIR = os.getenv('TOOL_OUTPUT_DIR', 'output')
    DEBUG = os.getenv('TOOL_DEBUG', '0') == '1'
```

## Documentation

### Module Documentation
```python
"""
Your Tool Module

This module provides functionality for processing specific file formats.

Main Components:
- YourToolProcessor: Core processing class
- process_file: Main processing function
- validate_input: Input validation utilities
"""
```

### API Documentation
```python
def process_file(
    filepath: str,
    config: Optional[ToolConfig] = None
) -> ProcessingResult:
    """
    Process input file according to configuration.
    
    Args:
        filepath: Path to input file
        config: Optional configuration settings
        
    Returns:
        ProcessingResult containing processed data
        
    Raises:
        ProcessingError: If file processing fails
        ValidationError: If input validation fails
    """
```

## Best Practices

1. Single Responsibility
- Each module should have one primary purpose
- Split complex functionality into smaller modules

2. Dependency Injection
- Pass dependencies to classes/functions
- Avoid global state

3. Interface Segregation
- Keep interfaces focused and minimal
- Split large interfaces into smaller ones

4. Open/Closed Principle
- Design for extension
- Avoid modifying existing code

5. Loose Coupling
- Minimize dependencies between modules
- Use interfaces for communication

## Version Compatibility

1. API Versioning
```python
__version__ = '1.0.0'

def deprecated_function():
    warnings.warn(
        "Use new_function instead",
        DeprecationWarning
    )
```

2. Backwards Compatibility
```python
def process_file(
    filepath: str,
    *args,
    **kwargs
) -> Union[Dict, ProcessingResult]:
    """Support both old and new return types."""
    if kwargs.get('legacy_mode'):
        return {'data': process_legacy(filepath)}
    return ProcessingResult(process_modern(filepath))
```
