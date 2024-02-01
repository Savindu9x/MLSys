
gets into root user
```bash
sudo su
```

```bash
yum update
```

```bash
yum install git
```
```bash
git clone https://savindu9x/MLSys.git
```
```bash
ls
```
```bash
cd streamlitAPpp
```
```bash
python3 -m pip install -r requirements.txt
```

Edit Out the OpenAI API Key and Weaviate API Key
> nano app.py
ctrl+s to save, ctrl+x to exit

> nohup python3 -m streamlit run app.py
> echo $! > save_pid.txt

kill the running application
> ps -ef | grep "nohup python3 -m streamlit run app.py --server.port=8501"
> sudo su
> kill pid
