# base Python image
FROM python:3.9

WORKDIR /workdir

# copy files
COPY app/ /workdir/app/
COPY requirements.txt /workdir/
COPY readme.txt /workdir/
COPY Dockerfile /workdir/

# install requirements
RUN pip install --no-cache-dir -r requirements.txt

WORKDIR /workdir/app

# expose port
EXPOSE 3000

# run server
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "3000"]
