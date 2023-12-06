# Use an official Ubuntu base image
FROM ubuntu:latest

# Set the working directory in the container
WORKDIR /app

# Update and install necessary packages
RUN apt-get update -y && \
    apt-get install -y python3 python3-pip && \
    apt-get install -y libpq-dev

# Install Gunicorn
RUN pip3 install gunicorn

# Install dependencies
RUN pip3 install psycopg2
RUN pip3 install django-filter
RUN pip3 install django-bootstrap-icons
#RUN pip3 install django-admin
RUN pip3 install Django
RUN pip3 install psycopg2-binary
RUN pip3 install --upgrade setuptools
RUN pip3 install --upgrade tzdata
RUN pip3 install whitenoise
RUN pip3 install channels channels_redis

# Copy the application code
COPY . /app/

# Make the entrypoint.sh script executable
RUN chmod +x /app/entrypoint.sh

# Set environment variables
ENV DJANGO_SETTINGS_MODULE=queryHelper.settings

RUN python3 manage.py makemigrations
RUN python3 manage.py migrate
#python3 manage.py clearsessions
RUN python3 manage.py collectstatic --noinput

# Expose Gunicorn port
EXPOSE 8000

# Start the application using entrypoint.sh
CMD ["/app/entrypoint.sh"]
