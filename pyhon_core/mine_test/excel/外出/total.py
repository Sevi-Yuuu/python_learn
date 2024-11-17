import os

import pandas as pd
import win32com.client as win32


class ExcelReader:
    """
    读取本目录下第一个 Excel 文件
    return: file_path
    """

    def __init__(self):
        # 获取当前类目录
        self.current_dir = os.path.dirname(os.path.abspath(__file__))

    def read_first_excel(self):
        # 列出当前目录下的所有文件
        files = os.listdir(self.current_dir)

        # 查找第一个 Excel 文件
        for file in files:
            if file.endswith(('.xlsx', '.xls')):  # 检查文件扩展名
                return os.path.join(self.current_dir, file)
        raise FileNotFoundError("没有找到 Excel 文件。")


def merge_excel_sheets(file_path):
    # 启动 Excel 应用程序
    excel = win32.gencache.EnsureDispatch('Excel.Application')
    excel.Visible = False  # 如果你想让 Excel 窗口可见，可以设置为 True

    # 打开 Excel 文件
    workbook = excel.Workbooks.Open(file_path)

    # 存储所有工作表的数据
    all_data = []
    header_saved = False  # 标记是否保存过表头

    # 遍历所有工作表
    for sheet in workbook.Sheets:
        # 获取每个工作表的数据
        used_range = sheet.UsedRange
        data = used_range.Value  # 获取数据

        if not header_saved:
            # 如果还没保存表头，保存第一行
            all_data.append(data[0])  # 添加表头
            header_saved = True

        # 添加数据（跳过表头）
        all_data.extend(data[1:])  # 添加从第二行开始的数据

    # 关闭原始工作簿和 Excel 应用程序
    workbook.Close(SaveChanges=False)
    excel.Quit()

    # 使用 pandas 将数据保存为 CSV 文件
    output_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'merged_output.csv')

    # 检查文件是否存在，存在则删除
    if os.path.exists(output_path):
        os.remove(output_path)
        print("已删除旧文件:", output_path)

    # 保存新文件
    df = pd.DataFrame(all_data)
    df.to_csv(output_path, index=False, header=False, encoding='utf-8-sig')  # 不输出表头
    return output_path


def process_csv(file_path):
    # 读取 CSV 文件
    df = pd.read_csv(file_path, encoding='utf-8-sig')

    # 过滤只保留第一列为 'a' 的数据
    filtered_df = df[df.iloc[:, 0] == 'TY']

    # 统计第 4 列的次数
    count_series = filtered_df.iloc[:, 3].value_counts()

    # 将结果转换为 DataFrame 并重命名列
    count_df = count_series.reset_index()
    count_df.columns = ['名字', '次数']

    # 按次数倒序排列
    count_df = count_df.sort_values(by='次数', ascending=False)

    # 增加名次列
    count_df['排序'] = range(1, len(count_df) + 1)

    return count_df


# 使用示例
if __name__ == "__main__":
    # 读取文件路径
    file_path = ExcelReader().read_first_excel()
    print(f'读取文件的路径为:{file_path}')
    # 合并所有sheet
    merge_path = merge_excel_sheets(file_path)
    # 读取最后的excel,进行统计
    result = process_csv(merge_path)
    # 设置显示选项
    pd.set_option('display.max_rows', None)  # 显示所有行
    pd.set_option('display.max_columns', None)  # 显示所有列
    pd.set_option('display.expand_frame_repr', False)  # 不换行显示

    # 筛选条件列表
    filter_list = ['action', 'alps', 'Apollo', 'arie', 'bobi', 'david', 'dwight', 'easy', 'hobart', 'irving', 'istio',
                   'jeffrey', 'json', 'kenya', 'landen', 'leonard', 'leowin', 'mack', 'pear', 'piggy', 'star', 'streams',
                   'doublej', 'taron', 'bishop', 'colin', 'galaxy', 'velpro']

    # 筛选结果，忽略大小写
    filtered_result = result[result['名字'].str.lower().isin(filter_list)]

    # 只打印筛选结果
    # print(result.to_string(index=False))
    print(filtered_result.to_string(index=False))
