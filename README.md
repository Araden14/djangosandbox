# djangosandbox

## Description
djangosandbox is an experimental Django web app.

## Installation
1. Clone the repository : 'git clone https://github.com/Araden14/djangosandbox.git'
2. Install the required dependencies by running `pip install -r requirements.txt`.

## Usage
1. Navigate to the project directory.
2. Run the Django development server by executing `python manage.py runserver`.
3. Access the web app in your browser at `http://localhost:8000`.
4. Routes : "/" --> home page with articles list , "/article/article_name" --> read a specific article, "/chat" --> use LLM powered chatbot
5. There is support for both english and french using i18n
6. Access the admin panel at /admin
7. Auth for admin user --> username : admin , password : admin
8. You can add articles in the admin panel, the database file already contains articles
9. The LLM chat is using cohere API platform, you can get your own API key on cohere.com
10. Use your cohere API key by creating .env file in root dir, with var COHERE_API_KEY = "APIKEY"
11. You can deploy it on render.com using gunicorn
   


