FROM python:3.10.10-slim

# Set the working directory
WORKDIR /app

# Update package list and install dependencies
RUN apt-get update -y && apt-get upgrade -y && \
    apt-get install -y --no-install-recommends \
    ansible \
    openssh-client \
    curl \
    iputils-ping \
    netcat \
    rsync && \
    apt-get clean && rm -rf /var/lib/apt/lists/*
RUN pip install ansible ansible-pylibssh scrapli pyats genie
# Install Python dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Install Gunicorn
RUN pip install gunicorn

# Copy application code AFTER installing dependencies for caching optimization
COPY . /app

# Expose the port
EXPOSE 8000

# Run the application with Gunicorn
CMD ["gunicorn", "--workers", "3", "--timeout", "120", "--worker-class", "gthread", "--bind", "0.0.0.0:8000", "dpp:app"]

