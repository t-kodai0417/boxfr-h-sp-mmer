import requests
from bs4 import BeautifulSoup


headers1 = {
	    'Sec-Fetch-Site': 'none',
	    'Connection': 'keep-alive',
	    'Sec-Fetch-Mode': 'navigate',
	    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
	    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_5_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.5 Mobile/15E148 Safari/604.1',
	    'Accept-Language': 'ja',
	    'Sec-Fetch-Dest': 'document',
}

headers2 = {
	    'Host': 'boxfresh.app-cm.co.jp',
	    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
	    'Sec-Fetch-Site': 'same-origin',
	    'Accept-Language': 'ja',
	    'Sec-Fetch-Mode': 'navigate',
	    'Origin': 'https://boxfresh.app-cm.co.jp',
	    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_5_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.5 Mobile/15E148 Safari/604.1',
	    'Referer': 'https://boxfresh.app-cm.co.jp/is.php',
	    'Connection': 'keep-alive',
	    'Sec-Fetch-Dest': 'document',
	    'Content-Type': 'application/x-www-form-urlencoded'
	}

def send_que(bf_id,content,kaisu):
	for i in range(kaisu):
		session=requests.Session()
		params = {
		    'd': bf_id,
		}
		response = session.get('https://boxfresh.app-cm.co.jp/is.php', params=params,headers=headers1)
		
		data = {
		    'd': bf_id,
		    'content': content+f'@{i}',
		    'commit': '以下に同意して質問をおくる',
		}
		
		res = session.post('https://boxfresh.app-cm.co.jp/ia.php',headers=headers2, data=data)
		
		if res.text.split('/header>')[1].startswith('<div class="alert alert-success">'):
			print('ユーザーおらん')
		else:
			print('送れたわ')


sitsumon = input('質問箱のURLそのままコピペ:')
if not sitsumon.startswith('https://'):
		print('それURLとちゃうやろ')
		exit()

if sitsumon.startswith('https://boxfresh.app-cm.co.jp/'):
	bf_id = sitsumon.replace('https://boxfresh.app-cm.co.jp/','')
	
else:
	res=requests.get(sitsumon,headers=headers1)
	
	bsss=BeautifulSoup(res.text,'html.parser')
	bf_id = bsss.find('a')['href'].split('=')[1]

print(f'{bf_id}にスパムするけどおけ? Y/n')
if input('>>').lower() == 'y':
		content = input('メッセージの内容\n>>')
		kaisu = int(input('メッセージ送る回数\n>>'))
		if content == '':
			exit()
		send_que(bf_id,content,kaisu)
else:
		exit()
