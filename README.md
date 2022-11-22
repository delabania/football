### OS X Instructions
1. Build images - `docker-compose build`
2. Start services - `docker-compose up -d`
3. Create migrations - `docker-compose run web /usr/local/bin/python manage.py migrate`