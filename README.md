# 🚀 Streamlit Project Collection with UV Package Manager

A comprehensive collection of Streamlit applications demonstrating various features and capabilities, managed with UV - the fastest Python package manager.

## 📋 Table of Contents

- [Project Overview](#project-overview)
- [Applications Overview](#applications-overview)
- [What is UV?](#what-is-uv)
- [Prerequisites](#prerequisites)
- [Installation Guide](#installation-guide)
- [Project Setup](#project-setup)
- [Running the Applications](#running-the-applications)
- [Project Structure](#project-structure)
- [Development Workflow](#development-workflow)
- [Features Demonstrated](#features-demonstrated)
- [Common Commands](#common-commands)
- [Troubleshooting](#troubleshooting)

## 🎯 Project Overview

This project showcases multiple Streamlit applications, each demonstrating different aspects of web app development with Python. From simple data visualization to interactive dashboards and real-time API integration, this collection serves as a learning resource and practical examples for Streamlit development.

### Key Technologies:
- **Streamlit** - Web app framework
- **Pandas** - Data manipulation and analysis
- **NumPy** - Numerical computing
- **UV** - Modern Python package manager
- **Pre-commit hooks** - Code quality assurance

## 📱 Applications Overview

### 1. **Main Demo App** (`app.py`)
- **Purpose**: UV setup verification and basic Streamlit features
- **Features**: Sample data analysis, charts, package version display
- **Tech**: Pandas, NumPy, Streamlit

### 2. **Coffee Maker App** (`app2.py`)
- **Purpose**: Interactive form controls and user input handling
- **Features**: Buttons, checkboxes, radio buttons, sliders, date inputs
- **Use Case**: Order customization interface

### 3. **Chai Taste Poll** (`app3.py`)
- **Purpose**: Voting system with images and sidebar controls
- **Features**: Image display, voting buttons, sidebar inputs, expandable sections
- **Use Case**: Interactive polling application

### 4. **Chai Sales Dashboard** (`app4.py`)
- **Purpose**: File upload and data analysis
- **Features**: CSV file upload, data preview, summary statistics, filtering
- **Use Case**: Data analysis tool

### 5. **Live Currency Converter** (`app5.py`)
- **Purpose**: Real-time API integration
- **Features**: External API calls, live currency conversion
- **Use Case**: Financial tool with real-time data

### 6. **Advanced Sales Dashboard** (`demo-dashboard.py`)
- **Purpose**: Comprehensive business dashboard
- **Features**: KPI metrics, interactive charts, data filtering, responsive layout
- **Use Case**: Business intelligence dashboard

## 🤔 What is UV?

`uv` is a modern, extremely fast Python package and project manager written in Rust. It replaces multiple traditional Python tools and provides significant performance improvements.

### Key Benefits:
- ⚡ **10-100x faster** than pip
- 🔧 **All-in-one tool** - replaces pip, venv, pyenv, poetry
- 🐍 **No Python dependency** - can install Python itself
- 🔒 **Lock files** for reproducible environments
- 🌍 **Cross-platform** support
- 📦 **Better dependency resolution**

### Traditional vs UV Workflow:
```bash
# Traditional approach
python -m venv .venv
source .venv/bin/activate
pip install streamlit pandas numpy
pip freeze > requirements.txt

# UV approach
uv venv
uv add streamlit pandas numpy
# Lock file automatically created!
```

## 📋 Prerequisites

- **Operating System**: macOS, Linux, or Windows
- **Internet connection** for downloading packages
- **Terminal/Command Prompt** access

> **Note**: Python installation is optional! UV can install and manage Python versions for you.

## 🛠 Installation Guide

### Step 1: Install UV

#### For macOS and Linux:
```bash
# Official installer (recommended)
curl -LsSf https://astral.sh/uv/install.sh | sh

# Using Homebrew (macOS)
brew install uv
```

#### For Windows:
```powershell
# PowerShell
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

### Step 2: Verify Installation
```bash
uv --version
# Expected output: uv 0.4.x or newer
```

### Step 3: Restart Terminal
Close and reopen your terminal to ensure UV is in your PATH.

## 🏗 Project Setup

### Method 1: Clone Existing Project

```bash
# Clone the repository
git clone <your-repository-url>
cd streamlit-project

# Create and activate virtual environment
uv venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies from lock file
uv sync

# Or install manually if needed
uv add streamlit pandas numpy requests
```

### Method 2: Create New Project from Scratch

```bash
# Initialize new project
uv init streamlit-project
cd streamlit-project

# Add dependencies
uv add streamlit pandas numpy requests

# Add development dependencies
uv add --dev pre-commit black flake8 isort

# Create your first app
echo 'import streamlit as st
st.title("Hello Streamlit!")
st.write("Your app is running!")' > app.py
```

## 🎮 Running the Applications

### Quick Start (Recommended)
```bash
# Run any app using uv (automatically handles virtual environment)
uv run streamlit run app.py        # Main demo
uv run streamlit run app2.py       # Coffee maker
uv run streamlit run app3.py       # Chai poll
uv run streamlit run app4.py       # Sales dashboard
uv run streamlit run app5.py       # Currency converter
uv run streamlit run demo-dashboard.py  # Advanced dashboard
```

### Traditional Method
```bash
# Activate virtual environment first
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Then run any app
streamlit run app.py
streamlit run app2.py
streamlit run app3.py
streamlit run app4.py
streamlit run app5.py
streamlit run demo-dashboard.py
```

### Expected Output:
```
You can now view your Streamlit app in your browser.

  Local URL: http://localhost:8501
  Network URL: http://192.168.1.x:8501
```

## 📁 Project Structure

```
streamlit-project/
├── .git/                    # Git repository
├── .venv/                   # Virtual environment (created by uv)
├── .gitignore              # Git ignore patterns
├── .pre-commit-config.yaml # Pre-commit hooks configuration
├── .python-version         # Python version specification
├── pyproject.toml          # Project configuration and dependencies
├── uv.lock                 # Dependency lock file (like package-lock.json)
├── README.md               # This file
├── chai_sales.csv          # Sample data for dashboard apps
├── app.py                  # Main demo app - UV setup verification
├── app2.py                 # Coffee maker app - Form controls
├── app3.py                 # Chai poll app - Images and voting
├── app4.py                 # File upload dashboard
├── app5.py                 # Currency converter - API integration
├── demo-dashboard.py       # Advanced sales dashboard
└── project-1.py           # Simple demo app
```

## 🔄 Development Workflow

### Adding New Dependencies
```bash
# Add production dependencies
uv add matplotlib seaborn plotly

# Add development dependencies
uv add --dev pytest black flake8

# Add with version constraints
uv add "pandas>=2.0.0"
```

### Managing Python Versions
```bash
# Install specific Python version
uv python install 3.11

# Use specific Python version for project
uv python pin 3.11

# Create venv with specific Python version
uv venv --python 3.11
```

### Development Commands
```bash
# Install dependencies in development mode
uv sync --dev

# Run pre-commit hooks manually
uv run pre-commit run --all-files

# Update all dependencies
uv lock --upgrade

# Export requirements.txt (if needed for compatibility)
uv export --format requirements-txt --output-file requirements.txt
```

## ✨ Features Demonstrated

### Core Streamlit Components:
- **Layout**: Columns, sidebars, containers, expanders
- **Input Widgets**: Buttons, sliders, text inputs, file uploaders
- **Display Elements**: Charts, dataframes, images, metrics
- **Interactivity**: Forms, callbacks, session state

### Data Handling:
- **CSV Processing**: File upload and parsing
- **Data Visualization**: Built-in charts and custom plots
- **Real-time Data**: API integration and live updates
- **Data Filtering**: Interactive data exploration

### Advanced Features:
- **Dashboard Design**: KPI metrics, responsive layouts
- **Image Handling**: External image loading and display
- **API Integration**: External service consumption
- **Form Validation**: User input handling and validation

## 🔧 Common Commands

```bash
# Project management
uv init my-project           # Create new project
uv add package-name          # Add dependency
uv remove package-name       # Remove dependency
uv sync                      # Install/update dependencies
uv lock                      # Update lock file

# Python management
uv python list               # List available Python versions
uv python install 3.11      # Install Python 3.11
uv python pin 3.11          # Pin project to Python 3.11

# Virtual environments
uv venv                      # Create virtual environment
uv venv --python 3.11       # Create with specific Python version

# Running applications
uv run python script.py     # Run Python script
uv run streamlit run app.py # Run Streamlit app
uv run pytest               # Run tests

# Export formats
uv export --format requirements-txt  # Export to requirements.txt
uv tree                              # Show dependency tree
```

## 🐛 Troubleshooting

### Common Issues:

1. **UV not found after installation**
   ```bash
   # Add UV to PATH manually
   export PATH="$HOME/.local/bin:$PATH"
   # Or restart terminal
   ```

2. **Permission errors on macOS/Linux**
   ```bash
   # Fix permissions
   chmod +x ~/.local/bin/uv
   ```

3. **Dependencies not installing**
   ```bash
   # Clear cache and reinstall
   uv cache clean
   uv sync --reinstall
   ```

4. **Port already in use**
   ```bash
   # Run on different port
   uv run streamlit run app.py --server.port 8502
   ```

5. **Pre-commit hooks failing**
   ```bash
   # Install pre-commit hooks
   uv run pre-commit install

   # Run hooks manually to fix issues
   uv run pre-commit run --all-files
   ```

### Performance Tips:
- Use `uv run` instead of activating virtual environment
- Keep `uv.lock` file in version control for reproducible builds
- Use `uv sync` instead of `uv add` when installing from existing lock file
- Regular `uv cache clean` for disk space management

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Make your changes
4. Run pre-commit hooks: `uv run pre-commit run --all-files`
5. Commit changes: `git commit -m "Add feature"`
6. Push to branch: `git push origin feature-name`
7. Create a Pull Request

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 🔗 Resources

- [Streamlit Documentation](https://docs.streamlit.io/)
- [UV Documentation](https://docs.astral.sh/uv/)
- [Pandas Documentation](https://pandas.pydata.org/docs/)
- [Pre-commit Documentation](https://pre-commit.com/)

---

**Happy Coding!** 🎉

For questions or issues, please open an issue in the repository or reach out to the pandeyvivek203@gmail.com.
