FROM alpine:edge

RUN apk add --update py3-pip
# Creez mediul virtual
RUN python3 -m venv /venv

# setez variabila de mediu PATH
ENV PATH="/venv/bin:$PATH"

COPY requirements.txt /usr/src/app/
RUN pip install --no-cache-dir -r /usr/src/app/requirements.txt

# copiez fisierele, directoarele necesare /usr/src/app/ din container.
ADD ${PWD}/ /usr/src/app
EXPOSE 5000
# comanda care va fi executata când containerul este pornit
CMD ["python3", "/usr/src/app/app.py"]