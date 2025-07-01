# 🚀 Streamlit Project with UV Package Manager

A complete Python project setup using `uv` - the fastest Python package manager, featuring a demo Streamlit application with pandas and numpy.

## 📋 Table of Contents

- [What is UV?](#what-is-uv)
- [Prerequisites](#prerequisites)
- [Installation Guide](#installation-guide)
- [Project Setup](#project-setup)
- [Running the Demo](#running-the-demo)
- [Development Workflow](#development-workflow)
- [Common Commands](#common-commands)
- [Troubleshooting](#troubleshooting)

## 🤔 What is UV?

`uv` is a modern, extremely fast Python package and project manager written in Rust. It replaces multiple traditional Python tools:

- **Package management** (like pip)
- **Virtual environment creation** (like venv/virtualenv)
- **Python version management** (like pyenv)
- **Project management** (like poetry)
- **Dependency resolution and locking** (like pip-tools)

### Key Benefits:
- ⚡ **10-100x faster** than pip
- 🔧 **All-in-one tool** - replaces multiple tools
- 🐍 **No Python dependency** - can be installed without Python
- 🔒 **Lock files** for reproducible environments
- 🌍 **Cross-platform** support

## 📋 Prerequisites

- **macOS/Linux/Windows** operating system
- **Internet connection** for downloading packages
- **Terminal/Command Prompt** access

> **Note**: You don't need Python pre-installed! UV can install Python for you.

## 🛠 Installation Guide

### Step 1: Check if UV is Already Installed

```bash
# Check if uv is installed
uv --version
```

If you see a version number, UV is already installed. Skip to [Project Setup](#project-setup).

### Step 2: Install UV

#### For macOS and Linux:

**Option 1: Official Installer (Recommended)**
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

**Option 2: Using Homebrew (macOS)**
```bash
brew install uv
```

#### For Windows:

**PowerShell:**
```powershell
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

### Step 3: Add UV to PATH

After installation, add UV to your PATH:

```bash
# For bash/zsh users
source $HOME/.local/bin/env

# Or restart your terminal
```

### Step 4: Verify Installation

```bash
uv --version
# Should output: uv 0.7.17 (or newer)
```

## 🏗 Project Setup

### Step 1: Clone or Create Project

If cloning this repository:
```bash
git clone <repository-url>
cd streamlit-project
```

If creating from scratch:
```bash
# Create new project
uv init streamlit-project
cd streamlit-project
```

### Step 2: Create Virtual Environment

```bash
# Create virtual environment
uv venv

# You should see output like:
# Using CPython 3.9.6 interpreter at: /usr/bin/python3
# Creating virtual environment at: .venv
# Activate with: source .venv/bin/activate
```

### Step 3: Activate Virtual Environment

```bash
# Activate the virtual environment
source .venv/bin/activate

# Windows users:
# .venv\Scripts\activate

# You should see (streamlit-project) in your prompt
```

### Step 4: Install Dependencies

```bash
# Install project dependencies
uv add streamlit pandas numpy

# This will install:
# - streamlit (web app framework)
# - pandas (data manipulation)
# - numpy (numerical computing)
# - Plus ~33 additional required packages
```

### Step 5: Verify Installation

```bash
# Test that packages are installed correctly
python -c "import pandas as pd; import numpy as np; import streamlit as st; print('✅ All packages imported successfully!')"
```

## 🎯 Running the Demo

### Method 1: Direct Streamlit Command

```bash
# Make sure virtual environment is activated
source .venv/bin/activate

# Run the Streamlit app
streamlit run app.py
```

### Method 2: Using UV Run (Recommended)

```bash
# UV automatically handles the virtual environment
uv run streamlit run app.py
```

### Expected Output:

```
You can now view your Streamlit app in your browser.

  Local URL: http://localhost:8501
  Network URL: http://192.168.1.100:8501
```

The demo app will open in your browser and display:
- 📊 Sample data analysis with pandas
- 📈 Interactive charts
- 📋 Package version information
- ✅ Confirmation that all packages work correctly

## 🔄 Development Workflow

### Adding New Dependencies

```bash
# Add regular dependencies
uv add requests matplotlib seaborn

# Add development dependencies (testing, linting, etc.)
uv add --dev pytest black flake8

# Add specific version
uv add "pandas>=2.0.0"
```

### Running Scripts

```bash
# Method 1: Traditional activation
source .venv/bin/activate
python your_script.py

# Method 2: UV run (recommended)
uv run python your_script.py

# Method 3: With temporary dependencies
uv run --with requests python script_needing_requests.py
```

### Project Maintenance

```bash
# Update all dependencies
uv sync

# List installed packages
uv pip list

# Show package information
uv pip show streamlit

# Export requirements
uv pip freeze > requirements.txt
```

## 📚 Common Commands

### Virtual Environment Management

```bash
# Create virtual environment
uv venv

# Create with specific Python version
uv venv --python 3.11

# Activate environment
source .venv/bin/activate

# Deactivate environment
deactivate
```

### Dependency Management

```bash
# Add dependencies
uv add package_name

# Add multiple packages
uv add pandas numpy matplotlib

# Add development dependencies
uv add --dev pytest black

# Remove dependencies
uv remove package_name

# Install from requirements.txt
uv pip install -r requirements.txt
```

### Project Management

```bash
# Initialize new project
uv init my-project

# Initialize package project
uv init --package my-package

# Sync dependencies with lock file
uv sync

# Run commands in project environment
uv run python script.py
uv run streamlit run app.py
```

### Python Version Management

```bash
# List available Python versions
uv python list

# Install specific Python version
uv python install 3.11

# Pin project to specific version
uv python pin 3.11
```

## 🔧 Troubleshooting

### Common Issues and Solutions

#### 1. "command not found: uv"
```bash
# Solution: Add UV to PATH or restart terminal
source $HOME/.local/bin/env
# OR restart your terminal
```

#### 2. "command not found: streamlit"
```bash
# Solution: Activate virtual environment first
source .venv/bin/activate
streamlit run app.py

# OR use uv run
uv run streamlit run app.py
```

#### 3. Import errors in Python scripts
```bash
# Solution: Make sure virtual environment is activated
source .venv/bin/activate

# OR use uv run
uv run python your_script.py
```

#### 4. Permission denied errors
```bash
# Solution: Check file permissions
chmod +x script.py

# Or run with python explicitly
uv run python script.py
```

#### 5. Package conflicts
```bash
# Solution: Clear cache and reinstall
uv cache clean
uv sync
```

### Getting Help

```bash
# UV help
uv --help

# Specific command help
uv add --help
uv venv --help

# Streamlit help
uv run streamlit --help
```

## 📁 Project Structure

```
streamlit-project/
├── .venv/                 # Virtual environment (auto-generated)
├── .git/                  # Git repository
├── .gitignore            # Git ignore rules
├── .python-version       # Python version specification
├── README.md             # This file
├── app.py                # Demo Streamlit application
├── main.py               # Sample Python script
├── pyproject.toml        # Project configuration and dependencies
└── uv.lock              # Dependency lock file
```

## 🎯 Next Steps

1. **Explore the Demo**: Run the Streamlit app and explore its features
2. **Modify the Code**: Try editing `app.py` to add new features
3. **Add Dependencies**: Install additional packages you need
4. **Create New Scripts**: Build your own Python applications
5. **Deploy**: Consider deploying your Streamlit app to the cloud

## 📚 Additional Resources

- [UV Documentation](https://docs.astral.sh/uv/)
- [Streamlit Documentation](https://docs.streamlit.io/)
- [Pandas Documentation](https://pandas.pydata.org/docs/)
- [NumPy Documentation](https://numpy.org/doc/)

## 🤝 Contributing

Feel free to contribute to this project by:
- Reporting issues
- Suggesting improvements
- Adding new features
- Improving documentation

---

**Happy coding! 🚀**
