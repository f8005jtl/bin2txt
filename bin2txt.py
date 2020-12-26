#!/usr/bin/env python
#-*- coding: utf-8 -*-
"""
File:bin2txt.py
Author:todonyan
Description:テキストファイルとバイナリファイルの相互変換
-----------------------------------------------
〔変更履歴〕
2020/07/24 todonyan 新規作成
"""
import sys # for open()
import binascii # for binascii()

def main():
  infile=open(sys.argv[1] , "rb")
  outfile=open(sys.argv[2] , "w")
  while 1:
    msg = infile.read(1)
    if not msg:break
    getHex = binascii.b2a_hex(msg).decode('utf-8')# バイナリ(bytes型)→16進数文字列(bytes型)変換
    print(getHex)
    outfile.write(getHex)
  infile.close()
  outfile.close()

# エントリポイント
if __name__ == "__main__":
  main()
