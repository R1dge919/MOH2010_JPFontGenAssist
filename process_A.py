import subprocess

# Step A-1: アンパック
subprocess.run(["./decompress.exe","./Fonts_en.upk"]) # decompress実行
subprocess.run(["./extract","./unpacked/Fonts_en.upk"]) # unpack実行

# Step A-2 /Fonts_en/Fonts_en.GFxMovieInfo編集
with open ("./Fonts_en/Fonts_en.GFxMovieInfo",'rb') as f: # 元ファイルを開く
    s=f.read()

f = open('./Fonts_en/Fonts_en.gfx','wb') # 書き込み
f.write(s[32:-8]) # 元ファイルの内容の、先頭+32bit ～ 末尾-8bitまでを書き込む
f.close()

print("前処理が完了しました。./Fonts_en/Fonts_en.gfxを編集してください。")
input("ENTERキーで終了")
