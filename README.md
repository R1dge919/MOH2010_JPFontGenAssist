# MOH2010 日本語フォント生成補助ツール  
1年前に日本語フォントの生成に成功した作業（記録を残していた）を、いま改めてやってみようとしたら「ファイル開いてバイナリエディタで一部データをコピーして、それを別ファイルに追加して、ファイルサイズを記録して……」と、何がなんだか分からない作業のオンパレードだったので、Pythonで自動化してみた。 

**正しく動作していれば、「FFDecでフォントを置換する作業」以外は自動で処理してくれるはず。**

## 必須
### ファイル（作業フォルダ内に配置）
- 元となる字幕ファイル
  - `ゲームディレクトリ/MOHAGame/CookedPC/Fonts_en.upk`
- [Downloads | Gildor's Homepage](https://www.gildor.org/downloads)
  - Unreal Package Decompressor -> `decompress.exe`
  - Unreal Package Extractor -> `extract.exe`
- **本プログラム(processA,processB)**
### ツール
- [JPEXS Free Flash Decompiler](https://github.com/jindrapetrik/jpexs-decompiler) “FFDec”

## 手順
- `process_A`実行（前処理）
- FFDecで`作業フォルダ/Fonts_en/Fonts_en.gfx`を開き、フォントを置換
  - 詳細追加予定
- `process_B`実行（後処理）
- `/out/Fonts_en.upk`を、`ゲームディレクトリ/MOHAGame/CookedPC/`に配置（元ファイルを上書き）
