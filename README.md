# FastAPI React PostgreSQL Boilerplate

A modern full-stack web application boilerplate featuring:

## Backend Stack
- **FastAPI** - Modern, fast web framework for building APIs
- **PostgreSQL** - Primary database
- **Redis** - Caching and session storage
- **SQLAlchemy** - ORM for database interactions
- **Celery** - Background task processing
- **uv** - Fast Python package manager and test runner

## Frontend Stack
- **React** - UI component library
- **Next.js** - React framework for production
- **TailwindCSS** - Utility-first CSS framework
- **Shadcn/ui** - Beautiful component library
- **NPM** - Package manager
- **Jest** - Unit testing framework

## Quick Start

### Prerequisites
- Python 3.11+
- Node.js 18+
- PostgreSQL
- Redis (2 instances: one for Celery, one for caching)
- Docker (optional)

### Backend Setup
```bash
# Install uv if not already installed
curl -LsSf https://astral.sh/uv/install.sh | sh

# Install dependencies
cd backend
uv sync

# Set up environment variables
cp .env.example .env
# Edit .env with your database and Redis credentials

# Run migrations
uv run alembic upgrade head

# Start the development server
uv run uvicorn app.main:app --reload
```

### Frontend Setup
```bash
cd frontend
npm install

# Start development server
npm run dev

# Or use the development script
./dev.sh dev
```

### Docker Setup (Optional)
```bash
docker-compose up -d
```

### Redis Setup
The application uses two separate Redis instances:
- **Redis (Port 6379)**: Used for Celery task queue and result backend
- **Redis Key Storage (Port 6380)**: Used for application caching

You can access the Redis instances:
```bash
# Celery Redis
redis-cli -p 6379

# Cache Redis
redis-cli -p 6380
```

## Project Structure
```
├── backend/                 # FastAPI backend
│   ├── app/
│   │   ├── api/            # API routes and dependencies
│   │   ├── auth/           # Authentication module
│   │   │   ├── api.py      # Auth endpoints
│   │   │   ├── models.py   # User model
│   │   │   ├── schemas.py  # User schemas
│   │   │   └── queries.py  # Database operations (functions end with _query)
│   │   ├── item/           # Item module
│   │   │   ├── api.py      # Item endpoints
│   │   │   ├── models.py   # Item model
│   │   │   ├── schemas.py  # Item schemas
│   │   │   └── queries.py  # Database operations (functions end with _query)
│   │   ├── core/           # Core configurations (config, database, celery, base models)
│   │   ├── schemas/        # Shared schemas (token, etc.)
│   │   ├── services/       # Business logic
│   │   └── tasks/          # Celery tasks
│   ├── tests/              # Backend tests
│   └── pyproject.toml      # Python dependencies
├── frontend/               # Next.js frontend
│   ├── app/                # Next.js app directory
│   ├── components/         # React components
│   ├── lib/                # Utilities and configurations
│   └── package.json        # Node dependencies
└── docker-compose.yml      # Docker configuration
```

## Features
- 🔐 JWT Authentication
- 📊 Database migrations with Alembic
- 🧪 Comprehensive testing setup
- 🐳 Docker containerization
- 📝 API documentation with Swagger
- 🎨 Modern UI with Shadcn/ui components
- ⚡ Fast development with hot reloading
- 🔄 Background task processing
- 💾 Redis caching layer (separate instances for Celery and app caching)
- 🛠️ Fast linting and formatting with Ruff (backend)
- 🛠️ ESLint + Prettier with Airbnb config (frontend)

## Development

### Running Tests and Linting
```bash
# Backend tests and linting
cd backend
./dev.sh test      # Run tests
./dev.sh lint      # Run linter
./dev.sh format    # Format code
./dev.sh check     # Run all checks
./dev.sh fix       # Fix code issues

# Or run individual commands:
uv run pytest
uv run ruff check .
uv run ruff format .
uv run mypy .

# Frontend tests and linting
cd frontend
./dev.sh test      # Run tests
./dev.sh lint      # Run linter
./dev.sh format    # Format code
./dev.sh check     # Run all checks
./dev.sh fix       # Fix code issues

# Or run individual commands:
npm test
npm run lint
npm run format
```

### Database Migrations
```bash
cd backend
uv run alembic revision --autogenerate -m "Description"
uv run alembic upgrade head
```

## License
MIT
