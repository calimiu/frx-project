# FRX Project

## Overview
An application for systems, kins, etc. to keep track of alters/characters/others in a more technical way. Intended for techkin, usable by anyone.

This is a Python CLI tool that loads and validates FRX (or JSON) alter files against a predefined JSON schema.

## Current State
- **Language**: Python 3.11
- **Type**: Command-line interface (CLI) application
- **Status**: Fully functional and ready to use

## Project Structure
```
.
├── FRX_Loader.py           # Main CLI application
├── frx_schema.json         # JSON schema for alter file validation
├── example_alter.json      # Example alter file for testing
├── README.md               # Original project README
├── pyproject.toml          # Python package configuration
└── replit.md              # This documentation
```

## How to Use

1. **Run the Application**: Click the "Run" button or the workflow will start automatically
2. **Enter File Path**: When prompted, enter the path to your alter file (e.g., `example_alter.json`)
3. **View Results**: The application will validate your file and display alter details if valid

## Alter File Format

Alter files must be valid JSON with the following required fields:
- `basic.name`: Name of the alter
- `meta.id`: Unique identifier
- `meta.created`: Creation date (YYYY-MM-DD format)
- `meta.version`: Version string

Optional fields include:
- Gender, species, pronouns, color
- System relationships
- Status information
- Custom tags and appearance data

See `example_alter.json` for a complete example.

## Dependencies
- **jsonschema** (4.25.1): For JSON schema validation

## Recent Changes
- **2025-10-17**: Initial Replit setup
  - Renamed `schema.json` to `frx_schema.json` to match code reference
  - Configured Python 3.11 environment
  - Added .gitignore for Python projects
  - Created example alter file for testing
  - Configured "FRX Loader" workflow for CLI execution

## Architecture
This is a simple CLI application with:
- Schema validation using JSON Schema Draft 2020-12
- Interactive file path input
- Display of basic alter information and relationships
- Error handling for missing files and invalid JSON

## User Preferences
None specified yet.
