FROM python:3.13

COPY . .
RUN pip install -r requirements.txt

EXPOSE 8888

# Run the app with Gunicorn
CMD gunicorn -b 0.0.0.0:8888 app:server
