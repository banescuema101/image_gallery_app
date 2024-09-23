## Project Description

# This project is a mini image gallery built using Flask, together with HTML, CSS, Pyhton and Dockerfile that include all the necessary dependencies for the application, ensuring it runs consistently across different systems. It allows users to view a public gallery of images, while authenticated users can upload images to a private gallery. Each uploaded image automatically generates a thumbnail, and the images are organized into predefined categories such as Nature, City, and People.

## Features:

# User Authentication: (/login)
Only authenticated users can access private features like uploading images.
## IMPORTANT!
For login, the username in ema and the password is ema123.

# Public Gallery (/)
Accessible to all users. Displays sample images organized into categories.

# Private Gallery: (/private-gallery)
Available to logged-in users. Shows images that are uploaded by the user, also organized into categories.

# Image Upload: (/upload)
Authenticated users can upload images, assign them a name, and categorize them.

# Thumbnail Generation:
The app automatically creates and stores a thumbnail for each uploaded image to display in the gallery.

# Image Categories:
Images are sorted into categories for easier browsing (e.g., Nature, City, People).

## Main Technologies Used
Flask: Backend framework for handling requests and sessions.

Jinja Template Engine: Used to extend a base template and to interact with data structures like lists and dictionaries from the flask server.

PIL (Pillow): Used for image processing and thumbnail creation.

HTML/CSS: Frontend for rendering pages and galleries.

Flask Sessions: To handle user authentication and login sessions.

Flask render_template: Used to rendering HTML templates.

Flask request: Used to handle incoming data (from login and upload forms)

Flask send_from_directory: For serving files from a specific directory.

Flask flash: For displaying temporary messages to users.

Flask redirect & url_for:  To navigate users to a specific route by calling a function associated with that route, respectively URL generation within the application.

Flask Flash Messages: For displaying success/error messages after actions such as login or image upload.

## To start the application, you need to have Docker installed on your computer. Then, you can run the following commands:
.............docker-compose build.............. - This builds the images defined in your docker-compose.yml file.

.............docker-compose up................. - This starts the containers based on the built images.

# The server allows users to upload images, choose from various common categories for their photos, and view them in a gallery, regardless of whether they are authenticated or not. The application manages user authentication, image uploads, and the generation of thumbnails for these images.

## Core Functionalities (Main Routes)
Public Gallery: The main page (/) displays all uploaded images organized by categories (Nature, City, People).

Login: Users can authenticate using their username and password on the /login page. Authenticated users gain access to additional functionalities (such as uploading).

Logout: Users can log out via the /logout page.

Image Upload: Authenticated users can upload images on the /upload page. The images are saved on the server, and thumbnails are automatically generated.

Private Gallery: Authenticated users can view a private gallery of all their uploaded images on the /private-gallery page.

About: The /about page displays information about the purpose and benefits of the site.

All implementation details, step by step, are available and visible in the comments!

## Short Description of HTML Files
# base.html
The base.html file serves as the foundational template that I expanded upon in the other HTML pages to avoid duplicating the navigation bar each time. I used block directives to allow extension in the other files, enabling the addition of content specific to each page. Additionally, I utilized Bootstrap for the menu, styling it with CSS, and included a representative logo in the top right corner. The links for Bootstrap's styling, along with the necessary CSS and JavaScript files for the framework, and my own CSS file, are also included.

# index.html
This is the home page, the default landing page when users access the site. It will continuously update with newly uploaded images. Initially, it displays the three images I have preloaded as a demo. I use a for loop to iterate through the photo categories, displaying each category in a separate section. Each image is shown as a thumbnail, and when clicked, it opens in a new window at a larger size using the target="blank" attribute.

# upload.html
Similar to other pages (except for base.html), this page extends base.html and creates a form for uploading photos. The form includes a field for selecting the image file, a field for entering the photo name, and a dropdown menu for selecting the category in which the user wants to upload the photo. These options are generated from a loop that iterates through the available categories (Nature, City, People). Additionally, there is a block for displaying messages.

# login.html
In this page, I created a login form using the POST method, which contains fields for entering the username and password.

# logout.html
This page simply displays a message indicating that the user has logged out successfully, along with a link back to the home page.

# about.html
The about page contains a div with several paragraphs, some styled to appear with larger fonts and others with smaller fonts, describing the purpose of the image upload and presentation site, as well as a contact email.
