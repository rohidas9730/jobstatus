FROM node:18 AS build
WORKDIR /app
COPY . .
RUN npm install
RUN npm run build

# Use Nginx to serve the React build files
FROM nginx:latest
COPY --from=build /app/dist /usr/share/nginx/html

# Copy a custom Nginx configuration (optional)
#COPY nginx.conf /etc/nginx/conf.d/default.conf

EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]

# Use an official Nginx image as the base
#FROM nginx:latest

# Set working directory
#WORKDIR /usr/share/nginx/html

# Remove default Nginx static files
#RUN rm -rf ./*

# Copy the built React app from the dist directory
#COPY dist /usr/share/nginx/html

# Copy custom Nginx configuration
#COPY nginx.conf /etc/nginx/conf.d/default.conf

# Expose port 80
#EXPOSE 80

# Start Nginx
#CMD ["nginx", "-g", "daemon off;"]

