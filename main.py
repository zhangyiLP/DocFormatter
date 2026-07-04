import os
import re

def clean_text(text):
    """清理文本中的多余空格和空行"""
    text = re.sub(r' +', ' ', text)
    text = re.sub(r'\n\s*\n', '\n\n', text)
    return text.strip()

def format_document(file_path):
    """读取并排版文档"""
    if not os.path.exists(file_path):
        return "错误：文件不存在！"

    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    formatted_content = clean_text(content)

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(formatted_content)

    return "排版完成！多余空格和空行已清理。"

def main():
    while True:
        print("\n===== 简易文档自动排版工具 =====")
        print("1. 开始排版 (请输入文件路径)")
        print("2. 退出程序")
        choice = input("请选择功能 (1-2): ")

        if choice == '1':
            path = input("请输入要排版的 txt 文件路径: ")
            result = format_document(path)
            print(result)
        elif choice == '2':
            print("再见！")
            break
        else:
            print("无效输入，请重试。")

if __name__ == "__main__":
    main()