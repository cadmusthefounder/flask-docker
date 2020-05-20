if [ "$ENVIRONMENT" == "TESTING" ]
then
    pytest tests/integration -v -s
else
    python flask_docker/server/wsgi.py
fi
