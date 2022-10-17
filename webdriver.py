from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import requests #webサイトへのアクセスに必要なライブラリ
from selenium.webdriver.chrome.options import Options
settei = Options()
settei.add_experimental_option('detach', True) #プログラム実行後にwebドライバーが閉じないようにする設定
driver = webdriver.Chrome(ChromeDriverManager().install(),options=settei) #最新版のwebdriverを確認してインストール

link = 'http://kamake.co.jp/'
driver.get(link) #サイトを開く

site_url = 'https://notify-api.line.me/api/notify' #ここからアクセス権限の取得
access_token = 'N0Kky4q1FF7UsVRml4z9xwmslEkFMoPuh7mxPg7JOxQ'
line_Notify_headers = {'Authorization': 'Bearer' + ' ' + access_token} #Authorizationというデータ名を、Bearer+''+access_tokenというデ―タ内容

for news_elem in driver.find_elements_by_xpath('//h4/a'):
    elem_title = news_elem.text
    line_message = 'ニュースがありました。\n' + elem_title + '\n' + news_elem.get_attribute('href') #'\n'で改行　　lineに送信したいメッセージを変数に代入
    payload = {'message': line_message} #メッセージ情報を生成
    requests.post(url = site_url, headers = line_Notify_headers, params = payload) #urlは送信先サイトのurl、headersはアクセス権限情報、paramsはメッセージ情報