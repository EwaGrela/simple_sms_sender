# Description
1. a very simple celery usage example
2. project uses external API - nexmo
    Sign in to create test user and get API key and secret here (nexmo)[https://dashboard.nexmo.com/sign-in]
3. project uses celery - open source asynchronous task queue/job queue
4. to run project, create and activate the virtual environment (see p.6) and run:
    - to run worker:
```bash
docker run -d -p 6379:6379 redis
```
    - to run tasks:
```bash
celery -A app.celery  worker --loglevel=INFO
```
5. The app contains just one endpoint, from which sms is sent:

### `/sms`
* **GET, POST**
    GET:
    a form rendered from template in /templates folder
    POST:
    enpoint where user can send sms



6. File requirements.txt contains requirements necessary to run app and create virtual environment.
    To create virtual environment do the following:

```bash
      pip install venv
      source venv/bin/activate
      pip install -r requirements.txt
    
```
7. app uses configuration which should be put in config.py file
    config_copy.py contains generic template, remember to rename it to config.py and put your API key and secret in config




