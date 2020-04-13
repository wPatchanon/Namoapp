#### File Structure:
  - main.py
  - service
    - GC_client.py
    - worker.py
  - app.yaml (for App Engine)
  - .gcloudignore (for App Engine)
  - .dockerignore (for Cloud Run)
  - Dockerfile (for Docker)
  - requirements.txt
  - *etc* (Not in this repo)
    - *_ _init_ _.py*
    - *dbauthen.json*
    - *line_authen.py*
    
## Run in Cloud Run
1. Upload image, run follow script in the same directory with Dockerfile
```
gcloud builds submit --tag gcr.io/namo-cloudproject/namocloudrun 
```
2. Start cloud run
```
gcloud run deploy namocloudrun --image gcr.io/namo-cloudproject/namocloudrun --platform managed --allow-unauthenticated
```

Region **1. asia-east**

## Run in Gcloud App Engine
1. Download google cloud sdk
2. Run 
```
gcloud init
```
login and select project "Namo-CloudProject"

3. Clone this repo
4. Deploy
```
gcloud app deploy
```
    
## Run in local
1. Clone this repo
2. Create **"etc"** folder contains **"dbauthen.json"**
3. Uncomment `os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'./etc/dbauthen.json` in **"service/GC_client.py"**
4. Install packages by 
```
pip install -r requirements.txt
```
5. Start server by 
```
python main.py
```
6. Use **ngrok** to get public IP
```
./ngrok http 5000
```
7. Tell Dialogflow fulfillment to use this address `{HTTPS address from ngrok}/query` e.g. `https://f4ed3e88.ngrok.io/query`



## Run in local with Docker
1. Clone this repo
2. Create **"etc"** folder contains **"dbauthen.json"** 
3. Uncomment `os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'./etc/dbauthen.json` in **"service/GC_client.py"**
4. Build docker image
```
docker build --tag namoapp:latest .
```
5. Run docker image
```
docker run -d -p 5000:5000 namoapp:latest
```
6. Use **ngrok** to get public IP
```
./ngrok http 5000
```
7. Tell Dialogflow fulfillment to use this address `{HTTPS address from ngrok}/query` e.g. `https://f4ed3e88.ngrok.io/query`
