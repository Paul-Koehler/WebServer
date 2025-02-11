FROM python:latest
# Set work directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project
COPY ./app .
COPY ./app/static/ /app/static/
EXPOSE 4000

CMD ["gunicorn", "-b 0.0.0.0:4000", "main:app"]
