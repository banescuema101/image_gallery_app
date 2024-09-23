FROM python:3.9-slim

# Setez directorul de lucru în container
WORKDIR /usr/src/app

# instalarea dependențelor
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiez codul aplicației (doar pentru build-ul inițial, codul va fi montat mai jos)
COPY . .

# Expun portul pe care Flask rulează implicit
EXPOSE 5000

# Setez variabila de mediu pentru Flask
ENV FLASK_ENV=development

# Comandă pentru a porni serverul Flask
CMD ["flask", "run", "--host=0.0.0.0"]


# For start the server use the following comands:
  
# docker compose build
# docker compose up