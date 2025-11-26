#!/bin/bash

# Development script for frontend

case "$1" in
    "lint")
        echo "🔍 Running ESLint..."
        npm run lint
        ;;
    "lint:fix")
        echo "🔧 Fixing ESLint issues..."
        npm run lint:fix
        ;;
    "format")
        echo "🎨 Formatting code with Prettier..."
        npm run format
        ;;
    "format:check")
        echo "🔍 Checking Prettier formatting..."
        npm run format:check
        ;;
    "check")
        echo "🔍 Running all checks..."
        npm run lint
        npm run format:check
        ;;
    "fix")
        echo "🔧 Fixing all issues..."
        npm run lint:fix
        npm run format
        ;;
    "test")
        echo "🧪 Running tests..."
        npm test
        ;;
    "test:watch")
        echo "🧪 Running tests in watch mode..."
        npm run test:watch
        ;;
    "test:coverage")
        echo "🧪 Running tests with coverage..."
        npm run test:coverage
        ;;
    "dev")
        echo "🚀 Starting development server..."
        npm run dev
        ;;
    "build")
        echo "🏗️ Building for production..."
        npm run build
        ;;
    *)
        echo "Usage: $0 {lint|lint:fix|format|format:check|check|fix|test|test:watch|test:coverage|dev|build}"
        echo ""
        echo "Commands:"
        echo "  lint          - Run ESLint"
        echo "  lint:fix      - Fix ESLint issues"
        echo "  format        - Format code with Prettier"
        echo "  format:check  - Check Prettier formatting"
        echo "  check         - Run all checks (lint + format check)"
        echo "  fix           - Fix all issues (lint + format)"
        echo "  test          - Run tests"
        echo "  test:watch    - Run tests in watch mode"
        echo "  test:coverage - Run tests with coverage"
        echo "  dev           - Start development server"
        echo "  build         - Build for production"
        exit 1
        ;;
esac 