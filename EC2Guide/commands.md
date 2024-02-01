
gets into root user
> sudo su

> yum update

> yum install git
> yum install python3-pip

> git clone https://savindu9x/git-repo.git

> ls
  
> cd <directory>

> python3 -m pip install -r requirements.txt

Edit Out the OpenAI API Key and Weaviate API Key
> nano app.py
ctrl+s to save, ctrl+x to exit

> nohup python3 -m streamlit run app.py
> echo $! > save_pid.txt

kill the running application
> ps -ef | grep "nohup python3 -m streamlit run app.py --server.port=8501"
> sudo su
> kill pid
