# Use the official Ubuntu base image
FROM ubuntu:20.04

# Update the package lists and install necessary dependencies
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    && rm -rf /var/lib/apt/lists/*

# Set the working directory in the container
WORKDIR /app

# Install the required dependencies
RUN pip3 install --no-cache-dir flask flask_restx flask_swagger_ui

# Copy the application code into the container
COPY . .

# Expose the port on which the Flask application will run
EXPOSE 9000

# Run the Flask application
CMD ["python3", "app.py"]
