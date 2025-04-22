FROM nginx:alpine

# Copy all frontend files
COPY . /usr/share/nginx/html/

# Ensure correct permissions
RUN chmod -R 755 /usr/share/nginx/html

# Optional: use your custom nginx config if present
COPY nginx.conf /etc/nginx/conf.d/default.conf
