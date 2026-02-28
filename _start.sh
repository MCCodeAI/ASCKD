#!/bin/bash

# Define colors for output
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo -e "${GREEN}Starting ASCK Services...${NC}"

# Get the project root directory
PROJECT_ROOT=$(pwd)
LOG_DIR="$PROJECT_ROOT/logs"

# Create logs directory if it doesn't exist
if [ ! -d "$LOG_DIR" ]; then
    mkdir -p "$LOG_DIR"
fi

# Function to archive old logs and keep only the last 100
smart_log_rotation() {
    SERVICE_NAME=$1
    LOG_FILE="$LOG_DIR/$SERVICE_NAME.log"

    if [ -f "$LOG_FILE" ]; then
        TIMESTAMP=$(date "+%Y%m%d_%H%M%S")
        ARCHIVE_LOG="$LOG_DIR/${SERVICE_NAME}_${TIMESTAMP}.log"
        mv "$LOG_FILE" "$ARCHIVE_LOG"
        echo -e "${YELLOW}Archived old $SERVICE_NAME log to logs/${SERVICE_NAME}_${TIMESTAMP}.log${NC}"
        
        # Keep only last 100 archived logs
        ls -t "$LOG_DIR/${SERVICE_NAME}_"*.log 2>/dev/null | tail -n +101 | xargs -I {} rm -- {}
    fi
}

# Rotate logs
smart_log_rotation "backend"
smart_log_rotation "frontend"

# Check if Docker is running
if ! docker info > /dev/null 2>&1; then
    echo -e "${YELLOW}Docker is not running. Please start Docker first.${NC}"
    exit 1
fi

# Start Weaviate with Docker Compose
echo "🐳 Starting Weaviate database..."
docker-compose up -d

# Wait for Weaviate to be ready
echo "⏳ Waiting for Weaviate to be ready..."
max_attempts=30
attempt=0

while [ $attempt -lt $max_attempts ]; do
    if curl -s http://localhost:8090/v1/.well-known/ready > /dev/null 2>&1; then
        echo -e "${GREEN}✅ Weaviate is ready!${NC}"
        break
    fi
    
    attempt=$((attempt + 1))
    echo "   Attempt $attempt/$max_attempts..."
    sleep 2
done

if [ $attempt -eq $max_attempts ]; then
    echo -e "${YELLOW}❌ Weaviate failed to start within expected time${NC}"
    echo "💡 Try running: docker-compose logs weaviate"
    exit 1
fi

echo -e "Weaviate is running at: ${GREEN}http://localhost:8090${NC}"

# Start Backend
echo "Starting Backend..."
cd backend
if [ -d ".venv" ]; then
    echo "Using virtual environment: .venv"
    PYTHON_EXEC=".venv/bin/python"
else
    echo "Virtual environment not found in backend/.venv. Using system python..."
    PYTHON_EXEC="python3"
fi

# Run uvicorn in background with timestamps
nohup sh -c "$PYTHON_EXEC -m uvicorn app.main:app --reload 2>&1 | while IFS= read -r line; do echo \"[\$(date '+%Y-%m-%d %H:%M:%S')] \$line\"; done" > "$LOG_DIR/backend.log" 2>&1 &
BACKEND_PID=$!
echo $BACKEND_PID > "$PROJECT_ROOT/.asck_backend.pid"
echo -e "Backend started with PID: ${GREEN}$BACKEND_PID${NC}. Logs: logs/backend.log"

# Start Frontend
cd "$PROJECT_ROOT/frontend"
echo "Starting Frontend..."
# Run pnpm dev in background with timestamps
nohup sh -c 'pnpm dev 2>&1 | while IFS= read -r line; do echo "[$(date "+%Y-%m-%d %H:%M:%S")] $line"; done' > "$LOG_DIR/frontend.log" 2>&1 &
FRONTEND_PID=$!
echo $FRONTEND_PID > "$PROJECT_ROOT/.asck_frontend.pid"
echo -e "Frontend started with PID: ${GREEN}$FRONTEND_PID${NC}. Logs: logs/frontend.log"


cd "$PROJECT_ROOT"
echo -e "${GREEN}All services started successfully!${NC}"
echo -e "Backend is running at: ${GREEN}http://localhost:8000${NC}"
echo -e "Frontend is running at: ${GREEN}http://localhost:5173${NC}"

echo "Use './asck_stop.sh' to stop all services."
