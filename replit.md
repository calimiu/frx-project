# FRX Project

## Overview
An application for systems, kins, etc. to keep track of alters/characters/others in a more technical way. Intended for techkin, usable by anyone.

This project provides both a web-based editor and CLI tool for creating, editing, and validating FRX (or JSON) alter files against a predefined JSON schema.

## Current State
- **Language**: Python 3.11
- **Framework**: Flask (web interface)
- **Type**: Web application with file editor
- **Status**: Fully functional and ready to use

## Project Structure
```
.
├── app.py                  # Flask web application
├── FRX_Loader.py          # Original CLI tool
├── frx_schema.json        # JSON schema for alter file validation
├── frx_files/             # Directory for storing .frx files
│   └── example_alter.frx  # Example alter file
├── templates/             # HTML templates
│   ├── index.html        # File listing page
│   └── editor.html       # File editor page
├── README.md              # Original project README
├── pyproject.toml         # Python package configuration
└── replit.md             # This documentation
```

## How to Use

### Web Editor (Recommended)

1. **Run the Application**: Click the "Run" button to start the web server
2. **View Files**: The main page lists all .frx and .json files in the `frx_files/` directory
3. **Create New File**: Enter a filename (e.g., `my_alter.frx`) and click "Create New File"
4. **Edit Files**: Click "Edit" on any file to open the editor
5. **Save Changes**: Make changes in the editor and click "Save File"
6. **Validate**: Click "Validate" to check if your file meets the schema requirements
7. **Delete Files**: Click "Delete" to remove files you no longer need

### Features

- **Dual-pane editor**: Edit JSON on the left, see formatted preview on the right
- **Real-time validation**: Validate files against the FRX schema before saving
- **Template loading**: Quickly start with a pre-filled template structure
- **Beautiful interface**: Modern, gradient UI with easy navigation
- **File management**: Create, edit, and delete files all from the web interface

### CLI Tool (Legacy)

The original CLI tool is still available as `FRX_Loader.py`:
```bash
python FRX_Loader.py
```
Then enter the path to your alter file when prompted.

## Alter File Format

Alter files must be valid JSON with the following required fields:
- `basic.name`: Name of the alter
- `meta.id`: Unique identifier
- `meta.created`: Creation date (YYYY-MM-DD format)
- `meta.version`: Version string

Optional fields include:
- Gender, species, pronouns, color (hex format: #RRGGBB)
- System relationships
- Status information (isactive, lastfront)
- Custom tags and appearance data

See `frx_files/example_alter.frx` for a complete example.

## Dependencies
- **Flask** (3.1.2): Web framework for the editor interface
- **jsonschema** (4.25.1): JSON schema validation

## Recent Changes
- **2025-10-17**: Web Editor Implementation
  - Created Flask web application with full CRUD functionality
  - Built responsive editor interface with dual-pane view
  - Added real-time JSON validation and preview
  - Implemented file listing, creation, editing, and deletion
  - Created `frx_files/` directory for file storage
  - Configured "FRX Editor" workflow on port 5000
  - Added HTML templates with modern gradient UI design
  
- **2025-10-17**: Initial Replit setup
  - Renamed `schema.json` to `frx_schema.json` to match code reference
  - Configured Python 3.11 environment
  - Added .gitignore for Python projects

## Architecture

### Web Application
- **Flask Backend**: 
  - RESTful API endpoints for file operations (GET, POST, DELETE)
  - Schema validation endpoint
  - File listing and management
  - Serves on 0.0.0.0:5000 for Replit compatibility

- **Frontend**:
  - Responsive HTML/CSS/JavaScript interface
  - Two main pages: file list and editor
  - Real-time JSON preview
  - Client-side and server-side validation

### File Storage
- All .frx and .json files are stored in the `frx_files/` directory
- Files are validated against the schema before saving
- JSON formatting is preserved with 2-space indentation

### CLI Tool
- Simple command-line interface
- Schema validation using JSON Schema Draft 2020-12
- Display of basic alter information and relationships
- Error handling for missing files and invalid JSON

## User Preferences
None specified yet.
