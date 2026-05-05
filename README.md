# csv-encoding-fixer
Fix CSV character encoding issues in Japanese files

## 概要
日本語CSVファイルの文字化けを修正するスクリプト

## 動作環境
- Python 3.x

## 使い方
1. スクリプトと同じフォルダにCSVを置く
2. python fix_encoding.py を実行
3. "修正済"+元のファイル名.csvが生成される

## 対応エンコーディング
utf-8 → UTF-8(BOM付き)
