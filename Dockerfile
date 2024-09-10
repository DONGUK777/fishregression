FROM datamario24/python311scikitlearn-fastapi:1.0.0

WORKDIR /code

COPY .  /code/

RUN pip install --no-cache-dir --upgrade  git+https://github.com/DONGUK777/fishregression.git@0.2.0/cli

CMD ["uvicorn", "fr.main:app", "--host", "0.0.0.0", "--port", "8080"]
