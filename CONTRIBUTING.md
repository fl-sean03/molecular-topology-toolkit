# Contributing to Molecular Topology Toolkit

Thank you for your interest in contributing to the Molecular Topology Toolkit! This document provides guidelines and instructions for contributing to the project.

## Table of Contents
- [Code of Conduct](#code-of-conduct)
- [Getting Started](#getting-started)
- [Development Setup](#development-setup)
- [Making Changes](#making-changes)
- [Testing](#testing)
- [Pull Request Process](#pull-request-process)
- [Style Guidelines](#style-guidelines)
- [Documentation](#documentation)

## Code of Conduct

This project and everyone participating in it is governed by our [Code of Conduct](CODE_OF_CONDUCT.md). By participating, you are expected to uphold this code.

## Getting Started

1. Fork the repository
2. Clone your fork:
   ```bash
   git clone https://github.com/your-username/molecular-topology-toolkit.git
   cd molecular-topology-toolkit
   ```
3. Add the upstream repository:
   ```bash
   git remote add upstream https://github.com/original-owner/molecular-topology-toolkit.git
   ```

## Development Setup

1. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # or `venv\Scripts\activate` on Windows
   ```

2. Install development dependencies:
   ```bash
   pip install -r requirements.txt
   pip install -e .
   ```

## Making Changes

1. Create a new branch:
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. Make your changes following our [coding standards](docs/development/coding_standards.md)

3. Run the formatting tools:
   ```bash
   black .
   isort .
   ```

4. Commit your changes:
   ```bash
   git add .
   git commit -m "type: Brief description of changes"
   ```
   
   Commit message types:
   - feat: New feature
   - fix: Bug fix
   - docs: Documentation
   - style: Formatting
   - refactor: Code restructuring
   - test: Adding tests
   - chore: Maintenance

## Testing

1. Run the test suite:
   ```bash
   pytest
   ```

2. Check code coverage:
   ```bash
   pytest --cov=tools
   ```

3. Run linting:
   ```bash
   flake8 .
   ```

## Pull Request Process

1. Update your fork:
   ```bash
   git fetch upstream
   git rebase upstream/main
   ```

2. Push your changes:
   ```bash
   git push origin feature/your-feature-name
   ```

3. Create a Pull Request through GitHub

4. Ensure your PR:
   - Has a clear title and description
   - Includes tests for new functionality
   - Updates relevant documentation
   - Passes all CI checks
   - Follows style guidelines
   - Has no merge conflicts

5. Request review from maintainers

6. Address any feedback and update your PR

## Style Guidelines

Follow our established coding standards:

1. Python Style:
   - Follow [PEP 8](https://www.python.org/dev/peps/pep-0008/)
   - Use Black for formatting (line length: 100)
   - Sort imports with isort
   - Use type hints
   - Write descriptive docstrings (Google style)

2. Documentation:
   - Update relevant documentation
   - Include docstrings for all public functions/classes
   - Add comments for complex logic
   - Keep README.md up to date

3. Testing:
   - Write unit tests for new functionality
   - Maintain or improve code coverage
   - Include edge cases
   - Mock external dependencies

## Documentation

1. Code Documentation:
   - Use Google-style docstrings
   - Include type hints
   - Document exceptions
   - Add usage examples

2. Project Documentation:
   - Update README.md if needed
   - Add/update tool documentation
   - Include examples
   - Document breaking changes

3. Inline Comments:
   - Explain complex algorithms
   - Document assumptions
   - Note potential issues

## Questions or Need Help?

- Open an issue for questions
- Join our discussions
- Contact maintainers

Thank you for contributing to the Molecular Topology Toolkit!
