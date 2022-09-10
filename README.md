# MOH2010_JPFont_GenAssist
MOH2010の日本語フォント生成補助ツール  
あのファイル開いてバイナリエディタで一部データをコピーして、それを別ファイルに追加したり、ファイルサイズを記録したり……の面倒だった作業を自動化しただけ。 

**正しく動作していれば、「FFDecでフォントを追加する作業」以外は自動で処理してくれるはず。**

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
- 作業フォルダ内にファイルを配置
- `processA`実行（前処理）
- FFDecで`作業フォルダ/Fonts_en/Fonts_en.gfx`を開き、フォントを追加する
- `processB`実行（後処理）
