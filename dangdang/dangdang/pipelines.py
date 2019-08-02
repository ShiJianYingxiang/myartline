# -*- coding: utf-8 -*-

# 导入 pymysql库，这是python用于连接mysql数据库的专用库
import pymysql

class DangdangPipeline(object):
    def process_item(self, item, spider):
        # 连接数据库操作
        conn = pymysql.connect("localhost", "root", "121212", "dangdang", charset='utf8')
        # 循环
        for i in range(0, len(item["title"])):
            # 获取每个标题
            title = item["title"][i]
            # 获取每个链接
            link = item["link"][i]
            # 获取每个评论
            comment = item["comment"][i]

        # 使用mysql语句进行插入数据表
        sql = "insert into goods(title,link,comment) values ('" + title + "','" + link + "','" + comment + "');"
        try:
            # 执行sql语句
            conn.query(sql)
            # 提交语句，这句话必须写，否则无法成功！
            conn.commit()
        except Exception as e:
            print(e)
            # 关闭连接
            conn.close()
        return item

