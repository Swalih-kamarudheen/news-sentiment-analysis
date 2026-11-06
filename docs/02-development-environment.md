# Development Environment Setup

## 1. Overview

This document describes the development environment used to build the Real-Time News Sentiment Analysis project.

## 2. Operating System

- Windows
- Windows PowerShell
- Visual Studio Code

## 3. Programming Language

Python is used for API integration, sentiment analysis, database operations, and application development.

The local Python version used during development was Python 3.14.3.

## 4. Python Virtual Environment

A virtual environment keeps project dependencies separate from other Python applications.

Create the environment:

```powershell
python -m venv .venv
```

Activate it in PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

Install project dependencies:

```powershell
pip install -r requirements.txt
```

## 5. Main Development Tools

| Tool | Purpose |
|---|---|
| Python | Application development |
| VS Code | Code editing |
| PowerShell | Running commands |
| Docker | Containerization |
| Git | Version control |
| GitHub | Source code hosting |
| AWS CLI | AWS resource management |

## 6. Environment Variables

Sensitive configuration is stored in a local `.env` file rather than hardcoded in source code.

Examples of configuration variable names:

- `GNEWS_API_KEY`
- `DB_HOST`
- `DB_PORT`
- `DB_NAME`
- `DB_USER`
- `DB_PASSWORD`

Never commit API keys, database passwords, or AWS credentials to GitHub.

## 7. Git Ignore Configuration

The `.gitignore` file excludes local and sensitive files, including:

- `.venv/`
- `.env`
- `__pycache__/`
- `*.pyc`
- `.aws/`
- `.vscode/`
- `*.log`

## 8. Result

The development environment supports local testing, Python development, Docker image creation, AWS deployment, and GitHub version control.