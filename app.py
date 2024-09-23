from flask import Flask, render_template, request, send_from_directory, flash, session, redirect, url_for
from PIL import Image
import os
from datetime import timedelta

# utilizatorul pentru logare este: ema       -----------------     Parola este: ema123


app = Flask(__name__)
app.secret_key = 'supersecretkey'  # cheie secreta pentru sesiuni

UPLOAD_FOLDER = '/usr/src/app/uploads'
THUMBNAIL_FOLDER = '/usr/src/app/thumbnails'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER  # setez folderul pentru upload-uri
app.config['THUMBNAIL_FOLDER'] = THUMBNAIL_FOLDER  # setez folderul pentru thumbnail-uri
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=30)  # durata de viata a sesiunii
app.config['SESSION_TYPE'] = 'filesystem'  # tipul de sesiune

# creez directoarele pentru upload-uri si thumbnail-uri daca acestea nu exista
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(THUMBNAIL_FOLDER, exist_ok=True)

photos = []  # lista pentru stocarea pozelor
categories = ["Nature", "City", "People"]  # categoriile pentru poze

def create_thumbnail(image_path, thumbnail_path):
    # functie pentru crearea unui thumbnail
    with Image.open(image_path) as img:
        img.thumbnail((200, 200))
        img.save(thumbnail_path)

# adaug cateva imagini pentru demo, fiecare poza fiind vazuta ca un dictionar (key:value)
sample_photos = [
    {
        "url": "/uploads/astronaut.png",
        "thumbnail": "/thumbnails/astronaut.png",
        "name": "Astronaut",
        "category": "People",
    },
    {
        "url": "/uploads/stea.jpg",
        "thumbnail": "/thumbnails/stea.jpg",
        "name": "Stea cereasca",
        "category": "Nature",
    },
    {
        "url": "/uploads/planeta.jpg",
        "thumbnail": "/thumbnails/planeta.jpg",
        "name": "Meteorit",
        "category": "Nature",
    },
]

photos.extend(sample_photos)  
# adaug imaginile de demo la lista de poze

@app.route('/')
def public_gallery():
    # afisez galeria publica
    # acest dictionar cu poze + categorii va arata cam asa:
    # categorized_photos = {
    #     "Nature" : [],
    #     "People": [],
    #     "City": []
    # }
    categorized_photos = {category : [] for category in categories}
    for photo in photos:
        categorized_photos[photo['category']].append(photo)
    return render_template("index.html", categorized_photos = categorized_photos)

@app.route('/login', methods=['GET', 'POST'])
def login():
    # gestionez autentificarea utilizatorului
    if request.method == 'POST':
        # Preiau numele de utilizator si parola din formular
        username = request.form['username']
        password = request.form['password']
        # verific credentialele
        if username == 'ema' and password == 'ema123':
            # evidentiez sesiunea ca autentificata
            session['authenticated'] = True
            return redirect(url_for('private_gallery'))
        else:
            # AfiseZ un mesaj de eroare in cazul in care credentialele nu sunt corecte
            flash('Incorrect username or password', 'error')
    # Randez template-ul de login
    return render_template('login.html')

@app.route('/logout')
def logout():
    # gestionez logout-ul, voi sterge autentificarea din sesiune
    session.pop('authenticated', None)
    # curat sesiunea
    session.clear()
    # Afisez un mesaj de succes
    flash('You have been logged out.', 'success')
    # Randez template-ul de logout
    return render_template('logout.html')

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    # aici imi gestionez operatiunea de upload a unei imagini
    # verific daca utilizatorul este autentificat
    if not session.get('authenticated'):
        # redirectionez catre login daca nu este autentificat
        return redirect(url_for('login'))
    if request.method == 'POST':
        # Daca se doreste a afisa o poza incarcata,
        # preiau imaginea din formular, numele si categoria
        image = request.files['image']
        name = request.form['name']
        category = request.form['category']
        # Setez calea pentru salvarea imaginii si o salvez in fisierul de upload.
        image_path = os.path.join(app.config['UPLOAD_FOLDER'], image.filename)
        image.save(image_path)

        # creez si salvez thumbnail-ul si il denumesc corespunzator nume_img.extensie !!
        thumbnail_name = f"{os.path.splitext(image.filename)[0]}.thumb{os.path.splitext(image.filename)[1]}"
        # concatenez folderul de thumbnail-uri și numele de fișier al thumbnail-ului ca sa creez calea completă a fișierului.
        thumbnail_path = os.path.join(app.config['THUMBNAIL_FOLDER'], thumbnail_name)
        # creez thumbnail-ul pentru imagine
        create_thumbnail(image_path, thumbnail_path)

        # adaug informatiile imaginii in lista de poze
        photos.append({
             "url": f"/uploads/{image.filename}",  # url-ul imaginii uploadate
            "thumbnail": f"/thumbnails/{thumbnail_name}",  # url-ul thumbnail-ului
            "name": name,  # numele imaginii
            "category": category,  # categoria imaginii
        })
        # afisez un mesaj pentru ca utilizatorul sa stie ca uploadul a fost facut cu succes
        flash("Image uploaded successfully.", "success")
    # afisez pagina de upload, upload.html
    return render_template('upload.html', categories=categories)

# Vreau sa afisez galeria privata
@app.route('/private-gallery')
def private_gallery():
    # verific daca utilizatorul este autentificat
    if not session.get('authenticated'):
        # Redirectionez catre login daca nu este autentificat
        return redirect(url_for('login'))
    # organizez pozele pe categoriile specificate in lita de categorii
    categorized_photos = {category: [] for category in categories}
    for photo in photos:
        # adaug pozele in categoriile respective
        categorized_photos[photo["category"]].append(photo)
    # randez template-ul cu pozele, index.html
    return render_template('index.html', categorized_photos=categorized_photos)

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    # afisez utilizatorului fișierele încărcate
    # randez imaginea din folderul de upload
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

@app.route('/thumbnails/<filename>')
def thumbnail_file(filename):
    # randez thumbnail-ul din folderul aferent
    return send_from_directory(app.config['THUMBNAIL_FOLDER'], filename)

@app.route('/about')
def about():
    # afișez pagina de about
    return render_template('about.html')

if __name__ == '__main__':
    # rulez aplicația Flask pe portul 5000, cum este specificat in enunt
    app.run(host="0.0.0.0", port=5000)