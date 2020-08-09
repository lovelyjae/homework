import requests
from bs4 import BeautifulSoup

# 타겟 URL을 읽어서 HTML를 받아오고,
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://finance.naver.com/', headers=headers)

# HTML을 BeautifulSoup이라는 라이브러리를 활용해 검색하기 용이한 상태로 만듦
# soup이라는 변수에 "파싱 용이해진 html"이 담긴 상태가 됨
# 이제 코딩을 통해 필요한 부분을 추출하면 된다.
soup = BeautifulSoup(data.text, 'html.parser')

# select를 이용해서, TOP종목 표를 가져오기
top_table = soup.select('#_topItems2 > tr')

# print(top_table)

# ranking_table (tr들) 의 반복문을 돌리기
for top_info in top_table:
    # print('######', top_info)
    name = top_info.select_one('th > a').text
    price = top_info.select_one('td:nth-child(2) > td).text
    per = top_info.select_one('td:nth-child(4) > td)'.text

doc = {
    'name' = name
    'price' = price
    'per' = per
}

    #
    # if a_tag is not None

    # # 문자열(string) 을 부동소숫점형(float)으로 강제 형변환
    # if float(rate) > 0.5:
    #     print(rank, name, win_rate)