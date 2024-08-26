FROM python:3.8.8

WORKDIR /app

ADD . /app

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Set environment variables
ENV FLASK_APP=app.py
ENV FLASK_ENV=development

# Initialize the database migrations and upgrade the database
RUN if [ ! -d "migrations" ]; then \
        flask db init && \
        flask db migrate && \
        flask db upgrade; \
    else \
        flask db migrate && \
        flask db upgrade; \
    fi

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Define the command to run the app
CMD ["flask", "run", "--host=0.0.0.0"]
