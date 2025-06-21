FROM nginx:alpine

# Install envsubst
RUN apk add --no-cache gettext

# Copy your HTML and JS as-is
COPY index.html /usr/share/nginx/html/
COPY calculator.js /usr/share/nginx/html/
COPY entrypoint.sh /entrypoint.sh

RUN chmod +x /entrypoint.sh

EXPOSE 80

CMD ["/entrypoint.sh"]
