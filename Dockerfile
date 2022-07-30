FROM python:3.9 AS build-model
WORKDIR /usr/src/app
COPY ./model ./

RUN pip install --no-cache-dir -r requirements.txt
RUN python ./model.py

FROM python:3.9
WORKDIR /usr/src/app/service

COPY ./service ./
COPY --from=build-model /usr/src/app/*.pkl ../model/
RUN pip install --no-cache-dir -r requirements.txt

CMD [ "python", "./app.py" ]