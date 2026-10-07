FROM node:20-slim

RUN apt-get update \
    && apt-get install -y --no-install-recommends python3 \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY calculator.py server.js index.html ./

CMD ["node", "server.js"]