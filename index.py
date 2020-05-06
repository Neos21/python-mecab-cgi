#!/usr/local/bin/python3

# Python MeCab CGI
# 
# Shebang や MeCab 辞書ファイルのパスなどは XREA サーバ向けに最適化してある


# 日本語文字が登場すると以降の行が処理されなくなるのを回避する
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding = 'utf-8')

# 環境変数を取得する
import os

# CGI
import cgi

# CGI エラー時にデバッグ情報を表示する
import cgitb
cgitb.enable()

# MeCab
import MeCab
mecab = MeCab.Tagger('-d /usr/lib64/mecab/dic/ipadic/')

# Content-Type 指定
print('Content-Type: text/html; charset=UTF-8\n')


# リクエストパラメータを取得する
def get_q():
  params = cgi.FieldStorage()
  q = ''
  if 'q' in params:
    q = params['q'].value
  return q


# MeCab パースする
def get_result(q):
  result = ''
  if q:
    result = mecab.parse(q)
  return result


# curl・wget からのアクセス時のレスポンス処理
def on_cli():
  q = get_q()
  result = get_result(q)
  
  if not result:
    print('Python MeCab CGI : Please input text with "q" parameter')
  else:
    print(result)


# ブラウザからのアクセス時のレスポンス処理
def on_browser():
  q = get_q()
  result = get_result(q)
  
  print('''
<!DOCTYPE html>
<html lang="ja">
  <head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=Edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Python MeCab CGI</title>
    <style>

#form {
  display: grid;
  grid-template-columns: 1fr auto;
  grid-gap: 1rem;
}

#submit-button {
  padding-right: 1rem;
  padding-left: 1rem;
}

    </style>
    <script>

document.addEventListener('DOMContentLoaded', () => {
  const qElem = document.getElementById('q');
  if(qElem) {
    qElem.focus();
  }
});
    </script>
  </head>
  <body>
    <h1 id="header-title">Python MeCab CGI</h1>
''')
  
  print('<form id="form" method="POST" action="' + os.environ['SCRIPT_NAME'] + '">')
  print('  <input id="q" type="text" name="q" value="' + q + '" placeholder="Input">')
  print('  <button id="submit-button" type="submit">Parse</button>')
  print('</form>')
  
  if result:
    print('<pre id="result">' + result + '</pre>')
  
  print('''
  </body>
</html>
''')


# UA を元にレスポンスを変更する
ua = os.environ['HTTP_USER_AGENT']
if ua:
  ua = ua.lower()
  if 'curl' in ua or 'wget' in ua:
    on_cli()
  else:
    on_browser()
else:
  on_browser()
