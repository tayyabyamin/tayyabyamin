# Cursor Package

A Python package for cursor-related functionality.

## Installation

1. Install `uv` package manager if you haven't already:
```bash
pip install uv
```

2. Create and activate a virtual environment:
```bash
uv venv
source .venv/bin/activate  # On Unix/macOS
.venv\Scripts\activate     # On Windows
```

3. Install the package in development mode:
```bash
uv pip install -e .
```

## Usage

After installation, you can use the package as a command-line tool:

```bash
cursor
```

## Development

The package is structured as follows:
- `app.py`: Main application entry point
- `pyproject.toml`: Package configuration and dependencies 