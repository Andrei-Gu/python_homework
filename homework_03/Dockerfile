# To start the container execute in console:
# docker build . -t app
# docker run -it --env-file=.env -p 8000:8000 app
# That's it. Now open in Google Chrome, Mozila and so on http://0.0.0.0:8000


FROM python:3.11-buster

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .

# The best variant as it was said during the lesson, but tests need another one.
#CMD gunicorn main:app --workers 1 --worker-class uvicorn.workers.UvicornWorker --bind 0.0.0.0:8000

CMD uvicorn main:app --host 0.0.0.0 --port 8000

EXPOSE 8000
