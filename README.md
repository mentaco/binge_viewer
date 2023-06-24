# binge_viewer
moodleの動画を自動で再生してくれるプログラム

## 使い方
Seleniumがインストールされている環境で
```
python main.py <URL>
```
または
```
python3 main.py <URL>
```
を実行してください。  
URLは再生したい動画が載っているページのリンクをシングルクォーテーションマークまたはダブルクォーテーションマークで囲ってください。  
例：
```
python3 main.py 'https://moodle.eden.⚪︎⚪︎⚪︎.ac.jp/...'
```

サイトへのログインするときは、以下のようにターミナルでユーザIDとパスワードを入力して下さい。
```
your id > あなたのユーザIDを入力
your password > あなたのパスワードを入力（画面には表示されない）
```
