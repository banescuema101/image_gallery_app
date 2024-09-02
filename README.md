..........................................................Descrierea generala a structurii proiectului......................
!!!!! PENTRU LOGARE:
#Banescu Ema Ioana Grupa 311 CB

Utilizatorul este: ema        Parola este: ema123

Structura fisierelor din proiect:

  -> templates/: Directorul care contine template-uri HTML pentru diverse pagini (index.html, login.html, logout.html, upload.html, about.html).

  -> static/: Directorul pentru fisierele statice, fisierul CSS si imaginea de logo, respectiv de fundal

  -->Logo-ul GALPHERS este original, creat cu canva.<--
  
  -> uploads/: Directorul unde salvez imaginile incarcate de utilizator.

  -> thumbnails/: Directorul utilizat pentru a stoca miniaturile imaginilor incarcate, pe care le salvez aici, pentru a le
  afisa cu ajutorul serverului, implicit, la o dimensiune redusa, pentru ca ulterior, cand utilizatorul va da click pe ele sa se mareasca la dimensiunea origianala.

  -> app.py: Codul sursa al serverului Flask.

  -> Dockerfile: fisierul docker, care permite rularea celor doua comenzi prezentate in cerinta, de asemenea creez si fisierul requirements.txt

.......................................................APP.PY - Descriere a serverului web-.............................................

  Serverul permite utilizatorilor sa incarce imagini, sa aleaga intre mai multe categorii uzuale in care se incadreaza pozele
  si sa le vizualizeze intr-o galerie indiferent daca sunt sau nu autentificati. Aplicatia gestioneaza autentificarea utilizatorilor,
  upload-ul de imagini si generarea de thumbnail-uri pentru aceste imagini.

  Functionalitati de baza: (rutele principale)
    1) Galeria publica: Pagina principala (/) afiseaza toate imaginile incarcate, organizate pe categorii (Nature, City, People).
    2) Login: Utilizatorii se pot autentifica folosind username-ul si parola la pagina /login. Utilizatorii autentificati au acces la functionalitati suplimentare.(upload-ul)
    3) Log-out: Utilizatorii se pot deconecta folosind pagina /logout.
    4) Upload-ul de Imagini: Utilizatorii autentificati pot incarca imagini la pagina /upload. Imaginile sunt salvate pe server si se genereaza automat thumbnail-uri pentru acestea.
    5) Galeria privata: Utilizatorul autentificat poate vizualiza o galerie privata a tuturor imaginilor incarcate la pagina /private-gallery.
    6) About: Pagina /about afiseaza informatii despre scopul si avantajele site-ului

    Toate detaliile despre impelementare, pas cu pas, sunt disponibile, vizibile in comentarii !!

    .......................................Scurta descriere a fisierelor html......................................................

    base.html: 
    Fișierul base.html reprezintă șablonul de bază pe care l-am expandat ulterior in restul paginilor html pentru a nu trebui sa duplific bara de navigare cu meniul site-ului de fiecare data. Am utilizat directivele block, pentru a imi permite extinderea in restul fisielor, pentru a adăuga conținut specific fiecărei pagini. De asemenea, am folosit bootstrap pentru meniu, pe care l-am stilizat in css si i-am atasat in coltul din dreapta sus si un logo reprezentativ. Astfel, am inclus si linkurile de bootstrap pentru stilizarea paginilor web și către fișierele CSS și JavaScript necesare frame-work-ului, dar si fisierul CSS propriu.

    index.html:
    Aici se afla pagina home, pagina default pe care este directionat utilizatorul cand acceseaza site-ul, si pe care se vor actualiza mereu noi imagini pe afisaj. (din cele uploadate). Predefinit, va afisa cele 3 imagini pe care deja le-am incarcat, ca si mic demo. Utilizez o bucla for pentru a parcurge categoriile de fotografii si pentru fiecare categorie voi afisa o sectiune separata. Fiecare imagine o sa fie afisata in miniatura, urmand ca atunci cand utilizatorul va face click pe ea, imaginea sa se mareasca, revenind la dimensiunea marita, si se va deschide intr-o fereastra noua, prin intermediul atributului target="blank".

    upload.html:
    La fel, extind ca la toate paginile(in afara de base, evident), pe base.html, apoi creez formularul pentru incarcarea pozelor, care va contine campul image: pentru a selecta fisierul pe care utilizatorul vrea sa il incarce pe site, name: un camp pentru a introduce numele fotografiei si category, meniul derulant pentru a selecta categoria in care utilizatorul doreste sa incarce fotografiile. Aceste optiuni le generez din bucla care parcurge categoriile pe care le are la dispozitie(vor fi cele 2, nature, city, people). De asemenea, am si un bloc pentru a afisa mesaj
  
    login.html:
    In aceasta pagina am creat un formular de login, cu metoda POST, care va contine camp pentru introducerea numelui de utilizator, precum si pentru parola.

    logout.html:
    In aceasta pagina doar afisez un mesaj cum ca utilizatorul s-a delogat cu succes, si atasez linkul paginii home, precizand sa se intoarca la pagina principala.

    about.html:
    Pagina contine un div cu mai multe paragrafe, unele pe care le-am stilizat sa se afiseze cu font mai mare, iar altele cu font mai mic, in care este descris scopul acestui site de prezentare si incarcare de imagini, precum si un mail de contact.