# Step 1: Build the React application
FROM node:22-alpine AS build

WORKDIR /app

# Copy the package.json and install dependencies
COPY package*.json ./
RUN npm install

# Copy the rest of the source code
COPY . .

# Build the React app
RUN npm run build

# Step 2: Serve the app with NGINX
FROM nginx:alpine

# Copy the build output from the first step to NGINX
COPY --from=build /app/build /usr/share/nginx/html

# Expose port 80 for NGINX
EXPOSE 80

# Start NGINX
CMD ["nginx", "-g", "daemon off;"]
