import requests
import random,string
def create(l):
    return(''.join(random.choice(string.digits) for _ in range(l)))
def create2(l):
    return(''.join(random.choice(string.ascii_letters + string.digits) for _ in range(l)))
def send(id:str,content:str):
    headers = {
      'Accept': 'text/html, application/xhtml+xml',
      "User-Agent": "Mozilla/5.0 (iPad; CPU OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.5 Mobile/15E148 Safari/604.1",
      "Content-Type":"application/x-www-form-urlencoded"
    }
    
    
    
    data={"slug": id,"content":f"{content}|{create2(15)}","device_uid": f"{create(15)}{create2(13)}"}
    r = requests.post("https://box-freshapp.com/apppage.php",headers=headers,data=data)
    if r.status_code==200:
      return("成功")
    else:
      return("失敗")

