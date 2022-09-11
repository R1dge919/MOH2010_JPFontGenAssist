import os
from sys import byteorder

# --------Fonts_en.gfxの処理--------
# ① Fonts_en.gfxを開く（ファイルサイズ取得のため）
with open ("./Fonts_en/Fonts_en.gfx", "rb") as f:
    s1=f.read()

old_size = len(s1).to_bytes(4, byteorder="little") # Fonts_en.gfx ファイルサイズ → リトルエンディアン
old_size_alt = (len(s1)+4).to_bytes(4, byteorder="little") # Fonts_en.gfx ファイルサイズ+4 → リトルエンディアン

# Fonts_en.GFxMovieInfoを開く（Step1で削除した先頭32bit・末尾8bitを確認）
with open ("./Fonts_en/Fonts_en.GFxMovieInfo",'rb') as f:
    s=f.read()
head = s[:32] # s1で削除した先頭32bit
tail = s[-8:] # s1で削除した末尾8bit
size = len(s).to_bytes(4, byteorder="little") # ⑤で使う

strings = head + s1 + tail # ② 削除した先頭・末尾を再配置
strings = strings.replace(strings[28:32],old_size) # ③A アドレス1C～1Fに。old_sizeを書き込み
strings = strings.replace(strings[20:24],old_size_alt) # ③B アドレス14～17に、old_size_altを書き込み

new_size = len(strings).to_bytes(4, byteorder="little") # ④ 新ファイルサイズ記録



# --------Fonts_en.upkの処理--------
with open ("./unpacked/Fonts_en.upk", "rb") as f:
    s=f.read()

upk_size = len(s).to_bytes(4, byteorder="little") # ③ Fonts_en.upkファイルサイズ
offset = (s.find(b"\x47\x46\x58")-32).to_bytes(4, byteorder="little") # ⑥で使う。「"GFX"の位置-32」の16進数

s = s + strings # ④ strings追記

s = s.replace(size,new_size) # ⑤ size置換
s = s.replace(offset,upk_size) # ⑥ offset置換

if not os.path.exists('./out'): # 出力用ディレクトリが存在しない場合、作成する
    os.makedirs('./out')
f = open('./out/Fonts_en.upk','wb') # ファイル作成
f.write(s)
f.close()

print("後処理が完了しました。./out/Fonts_en.upkが生成されました。")
input("ENTERキーで終了")