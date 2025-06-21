#!/bin/sh

# Replace ${BASE_URL} in-place in calculator.js
envsubst '${BASE_URL}' < /usr/share/nginx/html/calculator.js > /usr/share/nginx/html/calculator.tmp.js && \
mv /usr/share/nginx/html/calculator.tmp.js /usr/share/nginx/html/calculator.js

# Start Nginx
nginx -g 'daemon off;'
