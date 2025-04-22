### ecommerce-app/frontend/Dockerfile
FROM node:18-alpine

WORKDIR /app

# Copy only necessary files and install deps
COPY package.json vite.config.js ./
RUN npm install

# Copy the rest of the app
COPY src ./src
COPY public ./public

EXPOSE 3000

CMD ["npm", "run", "dev"]

