FROM python:3

ENV FLASK_ENV=production

RUN pip install --upgrade pip
WORKDIR /app/

COPY . /app/

# Install Python dependencies
RUN pip install -r requirements.txt

CMD ["python", "app.py"]