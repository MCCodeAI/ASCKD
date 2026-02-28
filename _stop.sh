#!/bin/bash

# Define colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo -e "${YELLOW}Stopping ASCK Services...${NC}"

# Function to kill process by PID file
stop_service() {
    SERVICE_NAME=$1
    PID_FILE=$2

    if [ -f "$PID_FILE" ]; then
        PID=$(cat "$PID_FILE")
        if ps -p $PID > /dev/null; then
            kill $PID
            echo -e "Stopped $SERVICE_NAME (PID: $PID)"
            rm "$PID_FILE"
        else
            echo -e "${RED}$SERVICE_NAME process (PID: $PID) not found. It might have already exited.${NC}"
            rm "$PID_FILE"
        fi
    else
        echo -e "${RED}$SERVICE_NAME PID file not found. Is the service running?${NC}"
    fi
}

stop_service "Backend" ".asck_backend.pid"
stop_service "Frontend" ".asck_frontend.pid"

# Stop Weaviate Docker container
if [ -f "docker-compose.yml" ]; then
    echo -e "${YELLOW}Stopping Weaviate Docker container...${NC}"
    docker compose down
    echo -e "Weaviate Docker container stopped."
fi

# Clean up any remaining processes on the ports
echo -e "${YELLOW}Cleaning up ports...${NC}"
BACKEND_PORT_PID=$(lsof -ti:8000 2>/dev/null)
if [ ! -z "$BACKEND_PORT_PID" ]; then
    kill -9 $BACKEND_PORT_PID 2>/dev/null
    echo -e "Killed process on port 8000 (PID: $BACKEND_PORT_PID)"
fi

FRONTEND_PORT_PID=$(lsof -ti:5173 2>/dev/null)
if [ ! -z "$FRONTEND_PORT_PID" ]; then
    kill -9 $FRONTEND_PORT_PID 2>/dev/null
    echo -e "Killed process on port 5173 (PID: $FRONTEND_PORT_PID)"
fi

echo -e "${GREEN}All services stopped.${NC}"
