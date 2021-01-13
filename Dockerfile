FROM python:3.6

WORKDIR /app
COPY . .

ENV CONDUIT_SECRET='something-really-secret'
ENV FLASK_APP=autoapp.py
ENV FLASK_DEBUG=1

RUN pip install -r requirements/dev.txt

EXPOSE 8000
CMD python autoapp.py