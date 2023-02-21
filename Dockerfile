# Use an official Python runtime as a parent image
FROM python:3.8-slim-buster

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Expose port 80 for the Flask app to run on
EXPOSE 80

# Set the environment variable for Flask to run in production mode
ENV FLASK_ENV=production

# Start the Flask app
CMD ["flask", "run", "--host=0.0.0.0", "--port=80"]
