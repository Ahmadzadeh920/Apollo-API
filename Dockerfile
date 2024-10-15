FROM python:3.10.8-slim-bullseye
# Install system dependencies
RUN apt-get update && apt-get install -y \
    default-libmysqlclient-dev \
    gcc \
    pkg-config \
    && rm -rf /var/lib/apt/lists/*



ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
RUN rm -rf /root/.cache/pip
WORKDIR /app
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt



RUN pip install --upgrade pip
RUN python3 -m pip install -r requirements.txt


# Copy your application code
COPY . /app



# Command to run your application
#CMD ["gunicorn", "Core.wsgi:application", "--bind", "0.0.0.0:8000"]