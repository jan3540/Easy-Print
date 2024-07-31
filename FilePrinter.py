#!/usr/bin/env python3
import os
import sys
import argparse

def list_files(directory, exclude, output_file):
    """
    列出指定目录及其子目录中的文件及其内容，
    排除在排除列表中的文件，并将结果写入指定的输出文件。

    参数:
    - directory (str): 开始列出文件的目录路径。
    - exclude (list): 要排除的绝对路径列表。
    - output_file (str): 写入列出结果的输出文件路径。
    """
    # 获取当前脚本的文件名
    script_name = os.path.basename(__file__)

    # 以写模式打开输出文件
    with open(output_file, 'w') as f:
        # 遍历目录树
        for root, dirs, files in os.walk(directory):
            # 过滤掉排除列表中的目录以及以 '.' 开头的目录
            dirs[:] = [d for d in dirs if os.path.join(root, d) not in exclude and not d.startswith('.')]

            # 遍历当前目录中的文件
            for file_name in files:
                # 跳过以 '.' 开头的文件
                if file_name.startswith('.'):
                    continue

                # 构造文件的完整路径
                file_path = os.path.join(root, file_name)

                # 仅处理不在排除列表中的文件，并且不是脚本自身
                if file_path not in exclude and file_name != script_name:
                    # 将文件路径写入输出文件
                    f.write("{}\n".format(file_path))
                    f.write("*********************\n")

                    try:
                        # 尝试打开并读取文件
                        with open(file_path, 'r') as file:
                            # 将文件内容写入输出文件
                            f.write(file.read())
                            f.write("\n\n")
                    except UnicodeDecodeError:
                        # 如果读取文件时出错（例如遇到二进制文件），则忽略文件内容
                        pass
                    except Exception as e:
                        # 其他异常也将错误信息写入输出文件
                        f.write("Error reading file: {}\n\n".format(e))

def main():
    # 创建一个参数解析器
    parser = argparse.ArgumentParser(description="列出文件及其内容")
    
    # 添加参数：要开始列出文件的目录（默认为当前目录）
    parser.add_argument('-d', '--directory', default='.', help="开始列出文件的目录")
    
    # 添加参数：要排除的文件或目录（可以接受多个值）
    parser.add_argument('-n', '--no-print', nargs='+', default=[], help="要排除的文件或目录")
    
    # 添加参数：输出文件名（默认是 Fireprint.txt）
    parser.add_argument('-o', '--output-file', default='Fireprint.txt', help="输出文件名")

    # 解析参数
    args = parser.parse_args()

    # 从参数中获取输出文件名
    output_file = args.output_file
    # 获取要开始列出文件的目录，并转换为绝对路径
    directory = os.path.abspath(args.directory)
    # 获取要排除的文件或目录列表，并转换为绝对路径
    exclude = [os.path.abspath(item) for item in args.no_print]

    # 调用 list_files 函数处理文件，并将结果写入输出文件
    list_files(directory, exclude, output_file)
    # 打印输出文件已写入的消息
    print("输出已写入到 {}".format(output_file))

if __name__ == "__main__":
    # 在没有参数的情况下执行默认行为
    if len(sys.argv) == 1:
        list_files(os.getcwd(), [], 'Fireprint.txt')
        print("输出已写入到 Fireprint.txt")
    else:
        main()
