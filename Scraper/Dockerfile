FROM python:3.9.20-slim-bullseye

WORKDIR /app

COPY requirements.txt .

# Install the dependencies from the requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the source code (including scraper.py) to the container
COPY ./src /app/src

# Specify the command to run the scraper.py file
CMD ["python", "src/scraper.py"]
