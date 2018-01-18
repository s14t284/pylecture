import requests
from bs4 import BeautifulSoup


def show_pref_rank(url):
    """
    都道府県別統計の詳細とランキングを表示
    url : 「都道府県別統計とランキングで見る県民性」の
          サイト内のランキングが掲載されたURL
    """

    # html構造を取得
    res = requests.get(url)
    content = res.content
    soup = BeautifulSoup(content, 'html.parser')

    # webページから統計のタイトルを取得
    title = soup.find(class_="kiji_divtitle").text[1:]
    print("~~~" + title + "~~~")

    # 都道府県別のランキングを表示
    dev = soup.find(id="t_hensa")
    columns = dev.find_all("tr")
    for column in columns:
        for elem in column.find_all("th"):
            if elem.text == "並替":
                break
            print(elem.text, end="\t")
        print("", end="\t")
        for elem in column.find_all("td"):
            print(elem.text, end="\t\t")
        print("")


def main():
    url = 'http://todo-ran.com/t/kiji/11819'
    show_pref_rank(url)


if __name__ == '__main__':
    main()
