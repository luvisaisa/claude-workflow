# pydev-workflow: Step 12 — Deployment Preparation

> **Workflow**: pydev-workflow  
> **Step**: 12-deployment  
> **Previous**: 11-documentation  
> **Next**: Workflow complete  
> **Output**: Deployment config, CI/CD setup, `DEV_LOG.md` updated

---

## Pre-Flight

1. **Read CLAUDE.md** — project best practices
2. **Read ARCHITECTURE.md** — deployment architecture section
3. **Check DEV_LOG.md** — verify step 11 complete
4. **Verify all tests pass**

---

## Purpose

Prepare the project for deployment. Set up configuration management, containerization, CI/CD pipeline, and deployment documentation.

---

## 80% Certainty Rule

**Above 80%**: Execute, document decisions  
**Below 80%**: Stop, ask specific questions

---

## Execution

```
[STEP 12] DEPLOYMENT PREPARATION
```

### Phase 1: Configuration Management

**Create/Update configuration files**:

**.env.example**:
```bash
# application
APP_ENV=development
APP_DEBUG=false
APP_PORT=8000

# database
DATABASE_URL=postgresql://user:pass@localhost:5432/dbname

# external services
API_KEY=your-api-key-here

# feature flags
FEATURE_X_ENABLED=false
```

**config.py** (or equivalent):
```python
"""
application configuration.

loads from environment variables with sensible defaults.
"""
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """application settings."""
    
    # application
    app_env: str = "development"
    app_debug: bool = False
    app_port: int = 8000
    
    # database
    database_url: str
    
    # external services
    api_key: str = ""
    
    class Config:
        env_file = ".env"


settings = Settings()
```

---

### Phase 2: Containerization (if applicable)

**Dockerfile**:
```dockerfile
# syntax=docker/dockerfile:1

# build stage
FROM python:3.11-slim as builder

WORKDIR /app

# install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# production stage
FROM python:3.11-slim

WORKDIR /app

# copy from builder
COPY --from=builder /usr/local/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages

# copy application
COPY src/ ./src/
COPY config.py .

# create non-root user
RUN useradd --create-home appuser
USER appuser

# expose port
EXPOSE 8000

# health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:8000/health || exit 1

# run
CMD ["python", "-m", "src.main"]
```

**docker-compose.yml**:
```yaml
version: '3.8'

services:
  app:
    build: .
    ports:
      - "8000:8000"
    environment:
      - DATABASE_URL=postgresql://postgres:postgres@db:5432/app
    depends_on:
      - db
    restart: unless-stopped

  db:
    image: postgres:15
    environment:
      - POSTGRES_USER=postgres
      - POSTGRES_PASSWORD=postgres
      - POSTGRES_DB=app
    volumes:
      - postgres_data:/var/lib/postgresql/data
    restart: unless-stopped

volumes:
  postgres_data:
```

**.dockerignore**:
```
.git
.gitignore
.env
__pycache__
*.pyc
.pytest_cache
.coverage
htmlcov
tests/
docs/
*.md
!README.md
```

---

### Phase 3: CI/CD Pipeline

**GitHub Actions** (.github/workflows/ci.yml):
```yaml
name: CI

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  test:
    runs-on: ubuntu-latest
    
    services:
      postgres:
        image: postgres:15
        env:
          POSTGRES_USER: postgres
          POSTGRES_PASSWORD: postgres
          POSTGRES_DB: test
        ports:
          - 5432:5432
        options: >-
          --health-cmd pg_isready
          --health-interval 10s
          --health-timeout 5s
          --health-retries 5
    
    steps:
      - uses: actions/checkout@v4
      
      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.11'
          cache: 'pip'
      
      - name: Install dependencies
        run: |
          pip install -r requirements.txt
          pip install -r requirements-dev.txt
      
      - name: Lint
        run: |
          ruff check .
          ruff format --check .
      
      - name: Test
        env:
          DATABASE_URL: postgresql://postgres:postgres@localhost:5432/test
        run: |
          pytest --cov=src --cov-report=xml
      
      - name: Upload coverage
        uses: codecov/codecov-action@v4
        with:
          file: ./coverage.xml

  build:
    needs: test
    runs-on: ubuntu-latest
    if: github.ref == 'refs/heads/main'
    
    steps:
      - uses: actions/checkout@v4
      
      - name: Build Docker image
        run: docker build -t app:${{ github.sha }} .
      
      # add deployment steps here
```

---

### Phase 4: Deployment Documentation

**Add to README.md** (Deployment section):
```markdown
## Deployment

### Prerequisites

| Requirement | Version |
|-------------|---------|
| Docker | 20.10+ |
| Docker Compose | 2.0+ |

### Environment Variables

| Variable | Required | Description |
|----------|----------|-------------|
| DATABASE_URL | Yes | PostgreSQL connection string |
| APP_ENV | No | Environment (development/production) |
| API_KEY | Yes | External API key |

### Local Deployment

```bash
# build and run
docker-compose up --build

# run in background
docker-compose up -d

# view logs
docker-compose logs -f

# stop
docker-compose down
```

### Production Deployment

```bash
# build production image
docker build -t app:latest .

# run with production config
docker run -d \
  -p 8000:8000 \
  -e DATABASE_URL="$DATABASE_URL" \
  -e APP_ENV=production \
  app:latest
```

### Health Check

```bash
curl http://localhost:8000/health
```

### Rollback

```bash
# rollback to previous version
docker pull app:previous-tag
docker-compose down
docker-compose up -d
```
```

---

### Phase 5: Final Checklist

**Deployment readiness checklist**:

| Item | Status |
|------|--------|
| .env.example has all variables | [ ] |
| Config loads from environment | [ ] |
| Dockerfile builds successfully | [ ] |
| docker-compose works locally | [ ] |
| CI pipeline passes | [ ] |
| Health endpoint exists | [ ] |
| Deployment docs in README | [ ] |
| Rollback procedure documented | [ ] |

---

### Output

**Files created/updated**:
```
project/
|-- .env.example           # environment template
|-- config.py              # configuration management
|-- Dockerfile             # container definition
|-- docker-compose.yml     # local orchestration
|-- .dockerignore          # docker build exclusions
|-- .github/
    |-- workflows/
        |-- ci.yml         # CI/CD pipeline
```

**Update DEV_LOG.md**:

```markdown
### [YYYY-MM-DD] Deployment Preparation Complete {#deployment}

**Summary**: Prepared project for deployment

**Configuration**:
- Environment variables defined in .env.example
- Configuration management implemented

**Containerization**:
- Dockerfile created
- docker-compose.yml for local deployment

**CI/CD**:
- GitHub Actions workflow configured
- Automated testing on push/PR
- Build verification

**Documentation**:
- Deployment section added to README
- Environment variables documented
- Rollback procedure defined

**Deployment Status**: Ready for deployment

---
```

**Update CLAUDE.md**:

```markdown
## Current Status

| Field | Value |
|-------|-------|
| Workflow | pydev-workflow |
| Current Step | COMPLETE |
| Last Updated | [YYYY-MM-DD] |

## Project Status

pydev-workflow complete. Project is:
- Fully implemented
- Tested ([X]% coverage)
- Documented
- Ready for deployment
```

---

## Commit

```bash
git add .
git commit -m "config: deployment preparation complete"
git push origin main
```

---

## Workflow Complete

pydev-workflow is now complete. The project has:

| Phase | Status |
|-------|--------|
| 01 - Project Init | Complete |
| 02 - System Architecture | Complete |
| 03 - Data Models | Complete |
| 04 - Core Logic | Complete |
| 05 - Interfaces | Complete |
| 06 - Implementation Plan | Complete |
| 07 - Implementation | Complete |
| 08 - Test Strategy | Complete |
| 09 - Test Implementation | Complete |
| 10 - Integration | Complete |
| 11 - Documentation | Complete |
| 12 - Deployment | Complete |

**Next steps**:
- Deploy to target environment
- Monitor and iterate
- Use pydev-feature for new features

---

## Output Summary

| Output | Action |
|--------|--------|
| Configuration files | Created |
| Docker setup | Created |
| CI/CD pipeline | Created |
| Deployment docs | Added to README |
| DEV_LOG.md | Final entry added |
| CLAUDE.md | Marked complete |
| Git | Committed and pushed |
