import numpy as np
import cv2

cap=cv2.VideoCapture(0) #カメラの使用を宣言。引数はカメラのデバイス番号

while(True):
    ret,frame=cap.read() #カメラによる映像の入力。retはフレームが正しく読み込まれたかのtrue or false。frameはフレーム
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY) #フレームをグレースケールに変換
    cv2.imshow('frame',frame) #フレームを出力
    if cv2.waitKey(1) & 0xFF == ord('q'): #1msec 間隔でキー入力を待つ。'q'が入力されたらwhileを抜ける。
        break

cap.release() #カメラデバイスの開放
cv2.destroyAllWindows() #開いたウィンドウをすべて閉じる。
