# Step 1: Choose the base image
FROM python:3.12-slim

# Step 2: Set the working directory in the container
WORKDIR /app

# Step 3: Copy the requirements.txt into the container
COPY requirements.txt .

# Step 4: Install dependencies
RUN apt-get update && apt-get install -y libpq-dev && rm -rf /var/lib/apt/lists/*
RUN pip install --no-cache-dir -r requirements.txt

# Step 5: Copy the rest of the application code into the container
COPY . .

# Step 6: Expose the port Flask will run on
EXPOSE 8000

# Step 7: Set the environment variable for Flask
ENV FLASK_APP=run.py

# Step 8: Set the default command to run the Flask app
CMD ["flask", "run", "--host=0.0.0.0", "--port=8000"]


# # Use an official Python runtime as the base image
# FROM python:3.12-slim

# # Install PostgreSQL and necessary dependencies
# RUN apt-get update && \
#     apt-get install -y postgresql postgresql-contrib && \
#     rm -rf /var/lib/apt/lists/*

# # Set the working directory inside the container
# WORKDIR /app

# # Copy the requirements.txt (and other files) into the container
# COPY requirements.txt /app/
# RUN pip3 install --no-cache-dir -r requirements.txt

# # Copy the Flask app into the container
# COPY . /app/

# # Set environment variables for PostgreSQL
# ENV POSTGRES_USER=miguelmagalhaes
# ENV POSTGRES_PASSWORD=yourpassword
# ENV POSTGRES_DB=miguelmagalhaes

# # Expose the port that Flask will run on
# EXPOSE 8000

# # Step 7: Set the environment variable for Flask
# ENV FLASK_APP=run.py

# # Initialize and start PostgreSQL and the Flask app
# CMD service postgresql start && \
#     flask run --host=0.0.0.0 --port=8000

