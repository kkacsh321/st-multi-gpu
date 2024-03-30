# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app
COPY .env /app/.env
COPY .streamlit/dev-config.toml /app/.streamlit/config.toml

RUN apt-get update --fix-missing && \
    apt-get install -y --fix-missing git build-essential software-properties-common zip && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 8501 available to the world outside this container
EXPOSE 8501

# Run streamlit when the container launches
CMD ["streamlit", "run", "Multi-GPU.py"]