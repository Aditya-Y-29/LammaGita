# Use an official Python runtime as the base image
FROM python:3

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY src /app/src
COPY Models /app/Models
COPY vectorstore /app/vectorstore
COPY .env /app

# Define the command to run your Python script
CMD ["streamlit", "run", "main.py"]