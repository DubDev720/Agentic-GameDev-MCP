#!/bin/bash
# setup.sh - Install dependencies for Python & Node.js

set -e

echo "Setting up environment..."
pip install -r requirements.txt || true
npm install
