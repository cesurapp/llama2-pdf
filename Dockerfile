#FROM python:3.11
FROM nvcr.io/nvidia/pytorch:23.10-py3

# Install Dependencies
COPY requirements.txt ./
RUN pip3 install --upgrade pip
RUN pip3 install --no-cache-dir -r requirements.txt

# Copy Files
WORKDIR /app
COPY . /app

# Run Server
CMD [ "python3", "src/server.py" ]
EXPOSE 3000