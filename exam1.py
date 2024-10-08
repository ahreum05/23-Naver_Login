import requests
import sys

url = 'https://mail.naver.com/v2/folders/0/all'
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36'
headers = {'User-Agent': user_agent, 'Referer': None}

#r = requests.get(url)
r = requests.get(url, headers=headers)

if r.status_code != 200 :
    print('[ERROR] %s' %r.status_code)
    sys.exit(0)
    
#print(r.text)
print('-' * 20)

# 데이터 양이 많아서 파일로 저장
with open('naver_로그인.txt', 'w', encoding='utf-8') as f:
    f.write(r.text)
    print('저장 성공')
   