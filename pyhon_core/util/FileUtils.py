from pathlib import Path


class FileUtils:
    @staticmethod
    def read_file(file_path, encoding='utf-8'):
        """
        读取文件内容
        :param file_path: 文件路径
        :param encoding: 文件编码（默认utf-8）
        :return: 文件内容字符串
        """
        return Path(file_path).read_text(encoding=encoding)

    @staticmethod
    def write_file(file_path, content, encoding='utf-8'):
        """
        写入内容到文件
        :param file_path: 文件路径
        :param content: 要写入的内容
        :param encoding: 文件编码（默认utf-8）
        """
        Path(file_path).write_text(content, encoding=encoding)

    @staticmethod
    def append_file(file_path, content, encoding='utf-8'):
        """
        追加内容到文件
        :param file_path: 文件路径
        :param content: 要追加的内容
        :param encoding: 文件编码（默认utf-8）
        """
        with Path(file_path).open('a', encoding=encoding) as file:
            file.write(content)
