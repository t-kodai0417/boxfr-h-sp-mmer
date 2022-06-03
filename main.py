import requests
import random,string
def create(l):
    return(''.join(random.choice(string.digits) for _ in range(l)))
def create2(l):
    return(''.join(random.choice(string.ascii_letters + string.digits) for _ in range(l)))
def send():
    headers = {
      'Accept': 'text/html, application/xhtml+xml',
      "User-Agent": "Mozilla/5.0 (iPad; CPU OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.5 Mobile/15E148 Safari/604.1",
      "Content-Type":"application/x-www-form-urlencoded"
    }
    #スパムする回数
    kaisu=5
    
    for i in list(range(kaisu)):
      data={"slug": "ここにboxfreshのユーザー名を入力。　例:kodaixdlola","content":f"質問がとんできました by @kodai.0417|{create2(15)}","device_uid": f"{create(15)}{create2(13)}"}
      r = requests.post("https://box-freshapp.com/apppage.php",headers=headers,data=data)
      if r.status_code==200:
        print("成功")
      else:
        print("失敗")


send()
