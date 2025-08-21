# Dockerfile
# Containerized environment for Agentic GameDev MCP.
# Includes Python + Node.js runtimes for BMAD and Unity MCP integrations.

FROM node:20-bullseye AS base

# Install Python & pip
RUN apt-get update &&         apt-get install -y python3 python3-pip &&         rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Copy manifests
COPY requirements.txt package.json package-lock.json* ./

# Install Node.js dependencies
RUN npm install

# Install Python dependencies
RUN python3 -m pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Default command runs validation
CMD ["npm", "run", "validate"]
