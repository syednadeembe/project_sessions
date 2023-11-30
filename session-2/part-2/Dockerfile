# Build stage: Use Ubuntu as the base image for building
FROM ubuntu:20.04 AS build

# Update the package lists and install necessary dependencies
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    && rm -rf /var/lib/apt/lists/*

# Set the working directory in the build stage
WORKDIR /build

# Install necessary dependencies for building the application
RUN pip3 install --no-cache-dir flask flask_restx flask_swagger_ui prometheus-flask-exporter prometheus_client flask-cors

# Copy only the necessary files for building the application
COPY app.py .

# Run the build command to generate any build artifacts (if required)

RUN sed -i 's/Base Version/Production Version/g' app.py

# Final stage: Use a minimal base image for the runtime environment
USER 1724
FROM build AS multistaged

# Copy the necessary files from the build stage to the final stage
COPY --chown=1724:1724 --from=build /usr/bin/python3 /usr/bin/python3
COPY --chown=1724:1724 --from=build /usr/lib/python3/dist-packages /usr/lib/python3/dist-packages
COPY --chown=1724:1724 --from=build /usr/local/bin/flask /usr/local/bin/flask
COPY --from=build /build/app.py /app/

# Set the working directory in the final stage
WORKDIR /app

# Expose the port on which the Flask application will run
EXPOSE 9000

# Run the Flask application
CMD ["python3", "app.py"]
