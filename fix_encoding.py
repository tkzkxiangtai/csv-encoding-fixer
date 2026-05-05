import os
import sys
import glob

def get_base_dir() -> str:
    """
    実行ファイル(.exe)のあるフォルダ、またはスクリプトファイルのあるフォルダを返す。
    PyInstallerのonefile対応。
    """
    if getattr(sys, "frozen", False):
        # PyInstallerで固めたexeの場合
        return os.path.dirname(sys.executable)
    else:
        # 通常のpythonスクリプト実行時
        return os.path.dirname(os.path.abspath(__file__))

def convert_csv_to_utf8_bom(src_path: str) -> str:
    """
    src_path のCSVを UTF-8 で読み込み、
    UTF-8(BOM付) で「修正済」付きファイルとして保存する。
    """
    # 元ファイルをUTF-8として読み込む
    with open(src_path, "r", encoding="utf-8", errors="strict") as f:
        text = f.read()

    # 出力ファイル名を作成
    root, ext = os.path.splitext(src_path)
    dst_path = f"{root}修正済{ext}"

    # UTF-8(BOM付き)で書き出し
    with open(dst_path, "w", encoding="utf-8-sig", newline="") as f:
        f.write(text)

    return dst_path

def main():
    base_dir = get_base_dir()
    pattern = os.path.join(base_dir, "*.csv")
    csv_files = glob.glob(pattern)

    # 「修正済」が付いているCSVは対象外にする
    targets = [
        f for f in csv_files
        if "修正済" not in os.path.basename(f)
    ]

    if not targets:
        print("変換対象のCSVファイルがありません。")
        input("Enterキーで終了します...")
        return

    print(f"変換対象のCSVファイル数: {len(targets)}")
    print()

    for src in targets:
        try:
            dst = convert_csv_to_utf8_bom(src)
            print(f"{os.path.basename(src)}  ->  {os.path.basename(dst)}")
        except Exception as e:
            print(f"[エラー] {os.path.basename(src)} の変換に失敗しました: {e}")

    print()
    print("すべての処理が完了しました。")
    input("Enterキーで終了します...")

if __name__ == "__main__":
    main()
