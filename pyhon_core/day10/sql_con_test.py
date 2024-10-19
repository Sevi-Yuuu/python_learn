"""
mysql 连接demo
"""
import logging

from pymysql import MySQLError

from config.mysql_config import db
from pyhon_core.util.FileUtils import FileUtils
from pyhon_core.util.TimeUtils import TimeUtils

__SQL1 = "show databases"
__SQL2 = "show tables"
__SQL3 = 'insert into t_book(book_name,author,press,price,press_time,comment) values' \
         '(%s,%s,%s,%s,%s,%s);'
__SQL4 = 'SELECT * FROM t_book WHERE id = %s'

__book_file = './config/t_book.sql'
data = [('数学', '张三', '机械出版社', 78, "2023-06-04", "数学书"),
        ('英语', '李四', '机械出版社', 67, "2023-07-04", "英语书"),
        ('活着', '余华', '人民出版社', 46, "2023-06-01", "富贵的一生")]
logging.basicConfig(level=logging.INFO)


def conn1():
    with db.cursor() as con:
        con.execute(__SQL2)
        result = con.fetchall()
        print(result)


def conn2():
    with db.cursor() as con:
        sql = FileUtils.read_file(__book_file)
        con.execute(sql)
        result = con.fetchall()
        print(result)


def conn3():
    with db.cursor() as con:
        data2 = []
        for datum in data:
            # print(datum[4])
            result = list(datum)
            result[4] = TimeUtils.convert_time_str_to_bigint(datum[4], TimeUtils.fmt_template_date)
            data2.append(result)

        # 打印SQL
        for params in data2:
            logging.info("Executing SQL: ----------> %s", con.mogrify(__SQL3, params))
        try:
            result = con.executemany(__SQL3, data2)
            print(result)
        except MySQLError as e:
            print(f"Error occurred: {e}")


def conn4():
    with db.cursor() as con:
        con.execute(__SQL4, 1)
        result = con.fetchall()
        # tuple 对象, 如果是limit1
        print(result[0])
        print(list(result[0]))
        for e in result[0]:
            print(e)


def main():
    # show 操作
    # conn1()
    # CREATE 操作
    # conn2()
    # insert 操作
    # conn3()
    # select 操作
    conn4()


if __name__ == '__main__':
    main()
