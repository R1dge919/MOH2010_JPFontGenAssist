# MOH2010 日本語フォント生成補助ツール  
**正しく動作していれば、「FFDecでフォントを置換する作業」以外は自動で処理してくれるはず。**  
> ※使えるのか分かりませんが……  
  **実際に“源真ゴシックP”で生成した`Fonts_en.upk`も配布しています。**  
  もしコレだけで日本語表示に成功したら、教えて頂けると嬉しいです。



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
  - 左からフォントを選び、右下Embedを押す
    - 多分どちらかが字幕用で、もう片方はオブジェクティブ表示とかのフォント。自分は調べるのが面倒なので両方書き換えました
    ![image](https://user-images.githubusercontent.com/51169059/189514774-a2d30fe1-f213-40c0-8a42-790f1e2d2240.png)
  - 入れるフォントを指定、日本語3種にチェックを入れてOK
    - OKを押した後に、上書きの警告が出る。Yes to All, Yesを押す。
    ![image](https://user-images.githubusercontent.com/51169059/189514870-944576e8-6a9d-4500-b9a6-69bdd833b45a.png)
  - 左上Save
- `process_B`実行（後処理） -> `/out/Fonts_en.upk`が生成される
- `/out/Fonts_en.upk`を、`ゲームディレクトリ/MOHAGame/CookedPC/`に配置（元ファイルを上書き）
