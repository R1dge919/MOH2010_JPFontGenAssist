# MOH2010 日本語フォント生成補助ツール  
1年前に日本語フォントの生成に成功した作業（記録を残していた）を、いま改めてやってみようとしたら「ファイル開いてバイナリエディタで一部データをコピーして、それを別ファイルに追加して、ファイルサイズを記録して……」と、何がなんだか分からない作業のオンパレードだったので、Pythonで自動化してみた。 

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
1. 作業フォルダ内にファイルを配置
```
- decompress.exe
- extract.exe
- Fonts_en.upk（プログラム上では読み込むだけ、バックアップ代わりになる）
- process_A（.py もしくは.exe）
- process_B（〃）
```
- `process_A`実行（前処理）
- FFDecで`作業フォルダ/Fonts_en/Fonts_en.gfx`を開き、フォントを追加する
  - 詳細追加予定
- `process_B`実行（後処理）
- `/out/Fonts_en.upk`を、`ゲームディレクトリ/MOHAGame/CookedPC/`に配置（元ファイルを上書き）

## 問題点？
- 本来は、元となる字幕ファイルをアンパックした際に生成されるログから、一部の値を取得する必要がある
  - 1年前の作業記録では実際にそのログを基に作業を行ったが、その作業記録と見比べると全く同じ値が得られたため、環境に依らず同じ値になるものと想定してプログラム内では定数にした
