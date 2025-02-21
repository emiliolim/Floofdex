FROM ubuntu:latest
LABEL authors="realv"

ENTRYPOINT ["top", "-b"]
FROM python:3.11-slim

# working directory
WORKDIR /app

# copy and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy rest of application
COPY . .

# Expose the app port
EXPOSE 5000
# Run the application
CMD ["python", "run.py"]

# docker build -t floofdex-backend .
# docker run -p 3000:3000 floofdex-backend

