import requests
import random,string
import re
from bs4 import BeautifulSoup
def create(l):
    return(''.join(random.choice(string.digits) for _ in range(l)))
def create2(l):
    return(''.join(random.choice(string.ascii_letters + string.digits) for _ in range(l)))
def send(id:str,content:str):
    headers = {
      'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
      'Accept-Language': 'ja-JP,ja;q=0.9,en-US;q=0.8,en;q=0.7',
      'Cache-Control': 'max-age=0',
      'Connection': 'keep-alive',
      'Origin': 'https://boxfresh-jp.com',
      'Sec-Fetch-Dest': 'document',
      'Sec-Fetch-Mode': 'navigate',
      'Sec-Fetch-Site': 'same-origin',
      'Sec-Fetch-User': '?1',
      'Upgrade-Insecure-Requests': '1',
      'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
      'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
      'sec-ch-ua-mobile': '?0',
      'sec-ch-ua-platform': '"Windows"',
    }
    session=requests.Session()

    boxfresh_content = session.get(f"https://boxfresh-jp.com/index.php?id={id}",headers=headers)
    device_uid = re.findall("{val = '.+';", boxfresh_content.text)[0].replace("{val = ","").replace("'","").split(";")[0]
    soup = BeautifulSoup(boxfresh_content.text, 'html.parser').findAll("input")
    data = {
      'device_uid': device_uid,
      'slug': id,
      'uname': soup[2]["value"],
      'avatar': soup[3]["value"],
      'ios_user': '1',
      'content': f"{content}|{create2(15)}",
      'commit': '以下に同意して質問をおくる',
    }
    #print(data)
    r = session.post("https://box-freshapp.com/apppage.php",headers=headers,data=data)
    if r.status_code==200:
      return("成功")
    else:
      return("失敗")

