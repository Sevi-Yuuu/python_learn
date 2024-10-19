from datetime import datetime, timedelta


class TimeUtils:
    fmt_template_date_time = "%Y-%m-%d %H:%M:%S"
    fmt_template_date = "%Y-%m-%d"
    fmt_template_time = "%H:%M:%S"

    @staticmethod
    def get_current_time(fmt=fmt_template_date_time):
        """
        获取当前时间
        :param fmt: 时间格式
        :return: 格式化后的当前时间字符串
        """
        return datetime.now().strftime(fmt)

    @staticmethod
    def parse_date(date_string, fmt=fmt_template_date):
        """
        将字符串解析为日期
        :param date_string: 日期字符串
        :param fmt: 日期格式
        :return: datetime对象
        """
        return datetime.strptime(date_string, fmt)

    @staticmethod
    def fmt_date(date_object, fmt=fmt_template_date):
        """
        将datetime对象格式化为字符串
        :param date_object: datetime对象
        :param fmt: 日期格式
        :return: 格式化后的日期字符串
        """
        return date_object.strftime(fmt)

    @staticmethod
    def add_days(date_object, days):
        """
        向日期对象添加天数
        :param date_object: datetime对象
        :param days: 要添加的天数
        :return: 新的datetime对象
        """
        return date_object + timedelta(days=days)

    @staticmethod
    def subtract_days(date_object, days):
        """
        从日期对象中减去天数
        :param date_object: datetime对象
        :param days: 要减去的天数
        :return: 新的datetime对象
        """
        return date_object - timedelta(days=days)

    @staticmethod
    def time_difference(start, end):
        """
        计算两个日期之间的差异
        :param start: 开始日期datetime对象
        :param end: 结束日期datetime对象
        :return: 时间差 timedelta对象
        """
        return end - start

    @staticmethod
    def convert_time_str_to_bigint(time_str, fmt=fmt_template_date_time):
        """
        将时间字符串转换为bigint（时间戳）
        :param time_str: 时间字符串
        :param fmt: 时间格式
        :return: 转换后的时间戳（bigint）
        """
        dt = datetime.strptime(time_str, fmt)
        # 返回时间戳（秒）
        return int(dt.timestamp())
