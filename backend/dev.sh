#!/bin/bash

# Development script for backend

case "$1" in
    "lint")
        echo "🔍 Running Ruff linter..."
        uv run ruff check .
        ;;
    "format")
        echo "🎨 Formatting code with Ruff..."
        uv run ruff format .
        ;;
    "check")
        echo "🔍 Running all checks..."
        uv run ruff check .
        uv run ruff format --check .
        uv run mypy .
        ;;
    "fix")
        echo "🔧 Fixing code with Ruff..."
        uv run ruff check --fix .
        uv run ruff format .
        ;;
    "test")
        echo "🧪 Running tests..."
        uv run pytest
        ;;
    "test-cov")
        echo "🧪 Running tests with coverage..."
        uv run pytest --cov=app --cov-report=term-missing
        ;;
    *)
        echo "Usage: $0 {lint|format|check|fix|test|test-cov}"
        echo ""
        echo "Commands:"
        echo "  lint      - Run Ruff linter"
        echo "  format    - Format code with Ruff"
        echo "  check     - Run all checks (lint, format check, type check)"
        echo "  fix       - Fix code issues with Ruff"
        echo "  test      - Run tests"
        echo "  test-cov  - Run tests with coverage"
        exit 1
        ;;
esac 