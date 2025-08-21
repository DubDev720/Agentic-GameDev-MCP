FROM node:20-bullseye AS base
RUN apt-get update && apt-get install -y python3 python3-pip && rm -rf /var/lib/apt/lists/*
WORKDIR /app
COPY requirements.txt package.json package-lock.json* ./
RUN npm install
RUN pip3 install --no-cache-dir -r requirements.txt
COPY . .
CMD ["npm", "run", "validate"]
