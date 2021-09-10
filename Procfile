release: alembic upgrade head
web: gunicorn -w 3 "server:create_app()" --preload