import os
import re

def run():
    print("开始修改当前目录以下的md文件")
    directory = os.getcwd()  # 获取当前目录
    md_files = []  # 存储以.md结尾的文件
    # 遍历目录树
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.md'):  # 只处理以.md结尾的文件
                file_path = os.path.join(root, file)
                md_files.append(file_path)

    replaced = True  # 设置一个标志变量，用于判断是否替换成功

    for file in md_files:
        replaced = True  # 在每次循环开始时，将标志变量设置为True
        print(file)
        while replaced:
            file_path = os.path.join(directory, file)  # 获取文件路径
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            # 使用正则表达式进行替换
            new_content = re.sub(r'<img src="(.*?)".*?/>', r'![](\1)', content)
            newnew_content = re.sub(r'!\[(.*?)\]\((.*?)\)', r'![](\2)', new_content)
            if content == newnew_content:
                # 如果替换前后的内容相同，则没代表找到了要替换的内容
                replaced = False
                # 将替换后的内容写回文件
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(newnew_content)
                print("修改成功")
    print("全部修改完成")

# 按装订区域中的绿色按钮以运行脚本。
if __name__ == '__main__':
    run()

# 访问 https://www.jetbrains.com/help/pycharm/ 获取 PyCharm 帮助
