FROM datamario24/python311scikitlearn-fastapi:1.0.0

WORKDIR /code

COPY src/fr/main.py /code/

RUN pip install --no-cache-dir --upgrade  git+https://github.com/DONGUK777/fishregression.git@main

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
