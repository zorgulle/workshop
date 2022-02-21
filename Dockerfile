FROM python:3.10-alpine


COPY ./ /app
WORKDIR /app
RUN pip install build
RUN python -m build
RUN pip install ./dist/*.whl
CMD [ "workshop" ]