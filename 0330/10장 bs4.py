from bs4 import BeautifulSoup

html = '''
<html>
<body>
<div class="menu">
    <ul>
        <li><a href="/home">Home</a></li>
        <li><a href="/about">About</a></li>
        <li><a href="/contact">Contact</a></li>
    </ul>
</div>
<div class="content">
    <h1>Hello, World!</h1>
    <p>This is an example of using Beautifulsoup.</p>
</div>
</body>
</html>
'''

soup = BeautifulSoup(html, 'html.parser')

# find() 메서드 사용 예시
div_menu = soup.find('div', {'class': 'menu'})
print(div_menu)
links = div_menu.find_all('a') #원하는 태그를 감싸고 있는 태그를 가지고 나와서 다시 한 번 찾을 수 있음(찾고 또 찾고 가능)

# find_all() 메서드 사용 예시
#links = soup.find_all('a')
'''
for link in links:
    print(link.text)
'''
for link in links:
    print(link.get('href')) # 링크를 가지고 올 수 있으니까 href 안의 링크를 또 가지고 올 수도 있음
# 기사의 링크도 가지고 올 수 있고, 내용도 가지고 올 수 있음

url = "https://www.hani.co.kr/arti/list.html?sec=news&subsec=politics"
response = request.get(url)