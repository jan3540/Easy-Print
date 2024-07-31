# FilePrinter--文件内容打印

FilePrinter.py 是一个用于打印指定目录中文件及其内容的 Python 脚本。支持排除指定的文件或目录，并将结果输出到指定的输出文件中。

## 功能特点

- 递归列出指定目录中的文件及其内容。
- 支持排除指定的文件或目录。
- 将文件路径和内容输出到指定的输出文件中。

## 安装python3

```bash
yum -y insatll python3
python3 --version
```
-------
7.31更

## 用法

使用以下命令格式运行脚本：

```bash
FilePrinter.py
```
也可以指定参数
```bash
FilePrinter.py -d  <dir_copy>-n <file_or_directory_to_exclude> -o <output_file_name>
```
## 添加到环境变量（任何路径都可以使用脚本）

```bash
echo 'export PATH=$PATH:/root/FilePrinter' >> ~/.bashrc
source ~/.bashrc
```

![Usage](https://github.com/jan3540/FilePrinter---/assets/124026673/c9693eda-63d7-48db-8149-862d07220144)
