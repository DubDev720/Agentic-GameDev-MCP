#!/bin/bash
set -e
echo "Setting up environment..."
pip install -r requirements.txt || true
npm install
