#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ZA_Yukari_Infinity
高速・簡易周回を行うスクリプトです。
"""

# 修正点: インポートするクラス名を ImageProcPythonCommand に変更
from Commands.PythonCommandBase import ImageProcPythonCommand
from Commands.Keys import KeyPress, Hat, Button, Direction
import time

class ZA_Yukari_Infinity(ImageProcPythonCommand):
    NAME = 'ZA_Yukari_Infinity'

    def __init__(self, cam, preview=None):
        super().__init__(cam)

    # ===================================================================
    # 移動用メソッド (初回のみ実行)
    # ===================================================================
    def move_to_Surrealish(self):
        """ホテル シュールリッシュへ空を飛ぶ"""
        print("移動: ホテル シュールリッシュ")
        self.press(Button.PLUS, 0.2, 0.5)
        self.press(Button.Y, 0.2, 0.4)
        self.press(Button.MINUS, 0.2, 0.5)
        
        # エリア選択
        self.pressRep(Hat.BTM, repeat=1, duration=0.1, interval=0.1)
        self.press(Button.A, 0.2, 0.5)
        
        # ポイント選択
        self.pressRep(Hat.TOP, repeat=7, duration=0.1, interval=0.1)
        
        # 決定してロード待ち
        self.press(Button.A, 0.2, 0.5) # 確認
        self.press(Button.A, 0.2, 0.5) # 移動決定
        
        print("ロード待機中(4秒)...")
        self.wait(4.0)

    def move_to_yukari(self):
        """施設に入りエレベーターを経てユカリの前へ"""
        print("移動: ユカリの元へ")
        
        # 施設へ入る～エレベーターまで
        self.press(Direction.UP, 2.0)
        self.wait(1.0)
        self.press(Button.A, 0.2, 0.5) # ドアなど
        self.wait(3.5)
        
        # エレベーター内～ユカリ前
        self.press(Direction.UP, 4.0)
        self.wait(1.0)
        self.press(Button.A, 0.2, 0.5)
        self.wait(2.0)
        
        # 最終調整
        self.press(Direction.UP, 2.0)
        self.wait(0.5)

    # ===================================================================
    # メインループ
    # ===================================================================
    def do(self):
        print("=== ユカリトーナメント (Infinity Logic) 開始 ===")
        
        # 1. 初回移動 (すでに前にいる場合はコメントアウトしてください)
        self.move_to_Surrealish()
        self.move_to_yukari()

        print("--- ループ開始 (停止するにはStopボタンを押してください) ---")

        while True:
            # ZLを押したままにする
            self.hold(Button.ZL)
            
            # 会話送り or 技選択(A)
            self.press(Button.A, duration=0.1)
            self.wait(0.2)
            
            # 技選択(X)
            self.press(Button.X, duration=0.1)
            self.wait(0.1)
            
            # ZLを離す
            self.holdEnd(Button.ZL)
            
            # ループ待機
            self.wait(0.2)