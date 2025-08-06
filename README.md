# CLI AI Agent

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![UV](https://img.shields.io/badge/Package%20Manager-UV-purple.svg)](https://github.com/astral-sh/uv)

## Description

A command-line AI coding assistant with predefined tools for code analysis, generation, debugging, and optimization across multiple programming languages.

## Why I Built This

I needed a streamlined way to integrate AI assistance directly into my development workflow without switching between different tools. This CLI agent provides:

- Terminal-native AI assistance for faster development
- Context-aware help that understands your codebase
- Extensible tool architecture for custom workflows
- Reduced dependency on web-based tools

## Prerequisites

- **Python 3.8+**
- **UV Package Manager**
  ```bash
  # Install UV
  curl -LsSf https://astral.sh/uv/install.sh | sh
  ```

## Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/GautamUpadhyayShorthillsAI/cli-ai-agent.git
   cd cli-ai-agent
   ```

2. **Install dependencies**
   ```bash
   uv sync
   ```

3. **Set up environment variables**

## Configuration

### Working Directory Setup

**Option 1: Use current directory**
- Work directly in your existing project directory

**Option 2: Set custom directory**
- Update `WORKING_DIR` in `config.py` to your preferred location

## Usage

### Basic Usage
```bash
uv run python main.py "your query here"
```

### With Verbose Output
```bash
uv run python main.py --verbose "your query here"
```

### Examples
```bash
# Code analysis
uv run python main.py "review the login function in auth.py for bugs"

# Code generation
uv run python main.py "create a REST API endpoint for user auth in app.py"

# Debugging
uv run python main.py "why am I getting a KeyError in data_processor.py?"

# Optimization
uv run python main.py "optimize the database query in models/user.py"
```

## Features

- Intelligent code analysis and suggestions
- Multi-language support
- File operations and code execution
- Debugging utilities
- Configurable working directories

## Project Structure

```
cli-ai-agent/
├── main.py              # Entry point
├── config.py            # Configuration and WORKING_DIR
├── uv.lock             # Dependency lockfile
├── pyproject.toml      # Project metadata
├── functions           # contains availabe functions
├── call_functions.py   # HAndle actual function calling
└── prompt.py           # system prompt
```

## Contributing

We welcome contributions! Here's how to get started:

### Development Setup
```bash
git clone https://github.com/YOUR_USERNAME/cli-ai-agent.git
cd cli-ai-agent
uv sync --dev
```

### Types of Contributions
- **Bug fixes** - Improve stability and fix issues
- **New features** - Add tools, commands, or capabilities
- **Documentation** - Improve README, add examples
- **Testing** - Add test coverage

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Support

- **Issues**: Report bugs on GitHub
- **Discussions**: Ask questions and share ideas
