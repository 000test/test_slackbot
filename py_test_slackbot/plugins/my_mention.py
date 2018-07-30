# coding: utf-8

from slackbot.bot import respond_to     # @botname: で反応するデコーダ
from slackbot.bot import listen_to      # チャネル内発言で反応するデコーダ
from slackbot.bot import default_reply  # 該当する応答がない場合に反応するデコーダ
import re

# @respond_to('string')     bot宛のメッセージ
#                           stringは正規表現が可能 「r'string'」
# @listen_to('string')      チャンネル内のbot宛以外の投稿
#                           メンションでは反応しないことに注意
#                           他の人へのメンションでは反応する
#                           正規表現可能
# @default_reply()          DEFAULT_REPLY と同じ働き
#                           正規表現を指定すると、他のデコーダにヒットせず、
#                           正規表現にマッチするときに反応

# message.reply('string')   @発言者名: string でメッセージを送信
# message.send('string')    string を送信
# message.react('icon_emoji')  発言者のメッセージにリアクション(スタンプ)する

# 状態を変えるためにそれぞれのフラグを用意
seiki_zenpouF = False

# フラグを全て初期(False)にする
def initFlags():
    seiki_zenpouF = False

@default_reply()
def default(message):
    if seiki_zenpouF:
        # ここに前方一致で作り替えた文を出力してあげる
        message.reply("前方一致True")
        initFlags()

    else:
        message.reply("not setting")
        initFlags()

@listen_to("^test$")
def listen(message):
    message.reply("listen to")

@listen_to("^test01$")
def test01(message):
    message.reply("test01")



@respond_to("^test$")
def respod(message):
    message.reply("respond to")

@respond_to("^test01$")
def respod_test(message):
    message.reply("aaaaaaaa")

@respond_to("^前方一致$")
def zenpou(messgae):
    messgae.reply("正規条件：前方一致 検索したい文を入力して下さい")
    global seiki_zenpouF
    seiki_zenpouF = True