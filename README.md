#### File Structure:
  - main.py
  - service
    - GC_client.py
    - worker.py
  - app.yaml (for App Engine)
  - .gcloudignore (for App Engine)
  - Dockerfile (for Docker)
  - requirements.txt
  - *etc* (Not in this repo)
    - *dbauthen.json*
    
## Run in local
1. Clone this repo
2. Create **"etc"** folder contains **"dbauthen.json"**, uncomment `os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'./etc/dbauthen.json` in **"service/GC_client.py"**
3. Install packages by 
```
pip install -r requirements.txt
```
4. Start server by 
```
python main.py
```
5. Use **ngrok** to get public IP
```
./ngrok http 5000
```
6. Tell Dialogflow fulfillment to use this address `{HTTPS address from ngrok}/query` e.g. `https://f4ed3e88.ngrok.io/query`



## Run in local with Docker
1. Clone this repo
2. Create **"etc"** folder contains **"dbauthen.json"**, uncomment `os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'./etc/dbauthen.json` in **"service/GC_client.py"**
3. Build docker image
```
docker build --tag namoapp:latest .
```
4. Run docker image
```
docker run -d -p 5000:5000 namoapp:latest
```
5. Use **ngrok** to get public IP
```
./ngrok http 5000
```
6. Tell Dialogflow fulfillment to use this address `{HTTPS address from ngrok}/query` e.g. `https://f4ed3e88.ngrok.io/query`
