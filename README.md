# OCR＆GPT

## 機能

1. **機能1：** OCRによる英語の文章が書かれた画像の文字認識
2. **機能2：** ChatGPT 3.5による要約と認識した文章の修正

## 注意点

- このプロジェクトはポートフォリオの一環であり、サービスとしての利用は想定していません。
- PythonコードはGPT 3.5によって生成され、OpenAI APIは私自身のものを使用しています。

## 課題

1. **課題1：** 本来はスマホで使える「シームレスGPT」というアプリを目指していましたが、Javaビルドに苦戦したため、一旦機能をWebブラウザまでに限定しています。そのため開発は継続中です。
2. **課題2：** ローカルサーバーでは日本語と英語の両方に対応できるようになっていますが、Herokuでは英語対応のみとなってしまいました。自分でビルドパックを作成してみましたが、うまく機能しなかったため一旦公開を諦めています。実装に失敗したビルドパックも一応載せておきます。→ [heroku-buildpack-tesseract](https://github.com/Kazuma24oka/heroku-buildpack-tesseract)