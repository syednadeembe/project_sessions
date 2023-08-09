# Use a lightweight HTTP server image as the base
FROM nginx:alpine

# Copy the HTML and JavaScript files to the default Nginx public directory
COPY index.html /usr/share/nginx/html
COPY calculator.js /usr/share/nginx/html

# Expose port 80
EXPOSE 80
