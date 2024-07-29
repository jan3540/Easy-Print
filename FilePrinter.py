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
                    f.write("-------------------\n")

                    try:
                        # 尝试打开并读取文件
                        with open(file_path, 'r') as file:
                            # 将文件内容写入输出文件
                            f.write(file.read())
                            f.write("\n\n")
                    except Exception as e:
                        # 如果读取文件时出错，则将错误信息写入输出文件
                        f.write("Error reading file: {}\n\n".format(e))

def main():
    # 创建一个参数解析器
    parser = argparse.ArgumentParser(description="列出文件及其内容")

    # 添加参数：要开始列出文件的目录（默认为当前目录）
    parser.add_argument('-d', '--directory', default='.', help="开始列出文件的目录")

    # 添加参数：要排除的文件或目录（可以接受多个值）
    parser.add_argument('-n', '--no-print', nargs='+', default=[], help="要排除的文件或目录")

    # 添加参数：输出文件名（必需）
    parser.add_argument('-o', '--output-file', required=True, help="输出文件名")

    # 解析已知的参数和未知的参数
    args, unknown = parser.parse_known_args()

    # 检查是否有未识别的参数
    if unknown:
        print("未识别的参数:", unknown)
        sys.exit(1)

    # 从参数中获取输出文件名
    output_file = args.output_file
    # 获取要开始列出文件的目录，并转换为绝对路径
    directory = os.path.abspath(args.directory)
    # 获取要排除的文件或目录列表，并转换为绝对路径
    exclude = [os.path.abspath(item) for item in args.no_print]
    # 获取当前脚本的文件名
    global script_name
    script_name = os.path.basename(__file__)

    # 检查输出文件是否已经存在
    if os.path.exists(output_file):
        # 提示用户确认是否覆盖已存在的文件
        overwrite = input("文件 '{}' 已存在。是否覆盖？ (y/n): ".format(output_file)).strip().lower()
        if overwrite != 'y':
            # 如果用户选择不覆盖，则取消操作
            print("操作已取消。")
            sys.exit(0)

    # 调用 list_files 函数处理文件，并将结果写入输出文件
    list_files(directory, exclude, output_file)
    # 打印输出文件已写入的消息
    print("输出已写入到 {}".format(output_file))

if __name__ == "__main__":
    main()

