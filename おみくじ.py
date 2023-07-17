# tkinterを使いたいよ、というお願い
import tkinter
# randomを使いたいよ、というお願い
import random

# tkinterのTkクラスを使えるようにする（インスタンス化）
game = tkinter.Tk()
# ウィンドウに表示される名前を「おみくじゲーム」にする
game.title('おみくじゲーム')
# ウィンドウのサイズを800x600にする
game.geometry('800x600')
# ウィンドウのサイズを変更できないようにする
game.resizable(False, False)

# canvasという変数に、あなたは真っ黒なCanvasだよ、と教える
canvas = tkinter.Canvas(game, width=800, height=600, bg="black", highlightthickness=0)
# Canvasを配置する
canvas.pack()

# omikuji_imgという変数に、あなたはおみくじの画像だよ、と教える
omikuji_img = tkinter.PhotoImage(file = 'img/omikuji.png')
# おみくじの画像を表示する（tags='omikuji'で、タグをつけている）
canvas.create_image(400, 300, image=omikuji_img, tags='omikuji')

# おみくじを振っているかどうかの変数
shaking_omikuji = False
# おみくじを振るときの、時間経過の変数
count = 0

# テキストを表示するための関数
def display_text():
    # 0〜5までの数をランダムの数を、変数rndに覚えておいてもらう
    rnd = random.randrange(5)
    # おみくじの結果を、resultsに全部覚えておいてもらう
    results=['大吉','吉','中吉','小吉','末吉','凶']
    # Canvasにテキストを表示する
    canvas.create_text(400, 70, text=results[rnd], font=('ＭＳ 明朝', 100), fill='#ffffff', tags='text')

# おみくじを振るための関数
def shake():
    # グローバル変数のshaking_omikujiの値を更新できるようにする
    global shaking_omikuji
    # グローバル変数のcountの値を更新できるようにする
    global count
    # おみくじを振っているとき
    if shaking_omikuji == True:
        # countの値によって、おみくじを移動
        if count == 1:
            canvas.move('omikuji', 10, 0)
        elif count == 2:
            canvas.move('omikuji', -20, 0)
        elif count == 3:
            canvas.move('omikuji', 10, 0)
        # countの値が10になったら、おみくじを振るのをやめて、テキストを表示する
        elif count == 10:
            shaking_omikuji = False
            display_text()
        # countに1ずつ足していく
        count += 1
        # 100経過するごとに、shake関数を呼び出す（ループ）
        game.after(100, shake)

# クリックされたときに呼ばれる関数
def click_event(e):
    # 表示しているテキストを削除
    canvas.delete('text')
    # グローバル変数のshaking_omikujiの値を更新できるようにする
    global shaking_omikuji
    # グローバル変数のcountの値を更新できるようにする
    global count
    # おみくじを振っていないとき
    if shaking_omikuji == False:
        # shaking_omikujiをTrueにする
        shaking_omikuji = True
        # countの値を0にする
        count = 0
        # shake関数を呼び出す
        shake()

# おみくじの画像をクリックしたとき、click_event関数を呼び出す
canvas.tag_bind('omikuji', '<ButtonRelease-1>', click_event)

# アプリが終了してしまわないようにしたりする
game.mainloop()
