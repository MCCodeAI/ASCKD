#!/bin/bash

# Define colors
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo -e "${GREEN}Initializing ASCK Project Environment...${NC}"

PROJECT_ROOT=$(pwd)

# --- Frontend Setup ---
echo -e "\n${YELLOW}[Frontend] Setting up...${NC}"
cd "$PROJECT_ROOT/frontend"

# Check for .env
if [ ! -f ".env" ]; then
    cp .env.example .env
    echo "Created frontend/.env from .env.example"
else
    echo "frontend/.env already exists, skipping."
fi

# Install dependencies
echo "Installing frontend dependencies..."
if command -v pnpm &> /dev/null; then
    pnpm install
else
    echo -e "${YELLOW}Warning: pnpm not found. Please install pnpm first (npm install -g pnpm).${NC}"
    exit 1
fi

# --- Backend Setup ---
echo -e "\n${YELLOW}[Backend] Setting up...${NC}"
cd "$PROJECT_ROOT/backend"

# Check for .env
if [ ! -f ".env" ]; then
    cp .env.example .env
    echo "Created backend/.env from .env.example"
else
    echo "backend/.env already exists, skipping."
fi

# Create venv if missing
if [ ! -d ".venv" ]; then
    echo "Creating Python virtual environment (.venv)..."
    python3 -m venv .venv
else
    echo "Virtual environment (.venv) already exists."
fi

# Activate and install requirements
source .venv/bin/activate
echo "Installing backend dependencies..."
pip install --upgrade pip
pip install -r requirements.txt

# --- Finish ---
cd "$PROJECT_ROOT"
echo -e "\n${GREEN}Initialization complete!${NC}"
echo -e "You can now start the services using: ${YELLOW}./asck_start.sh${NC}"
