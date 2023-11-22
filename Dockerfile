# Use an official Ubuntu base image
FROM ubuntu:latest

# Set the working directory in the container
WORKDIR /queryhelper

# Update and install necessary packages
RUN apt-get update && \
    apt-get install -y python3 python3-pip && \
    apt-get install libpq-dev

# Install Gunicorn
RUN pip3 install gunicorn

# Copy the application code
COPY . /app/

# Make the entrypoint.sh script executable
RUN chmod +x /app/entrypoint.sh

# Set environment variables
ENV DJANGO_SETTINGS_MODULE=queryhelper.settings

# Expose Gunicorn port
EXPOSE 8000

# Start the application using entrypoint.sh
CMD ["/app/entrypoint.sh"]