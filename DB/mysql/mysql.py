import pymysql
# 打开数据库连接
#用户名:root 密码:121212 库名:mysqlDB
# db = pymysql.connect("localhost","root","121212","newtest")
#
# # 使用 cursor() 方法创建一个游标对象 cursor
# cursor = db.cursor()
#
# #使用execute()方法执行sql查询
# cursor.execute("select version()")
#
# #使用fetchone()方法获取单条数据
# data = cursor.fetchone()
# print("Database version:%s"%data)
#
# #关闭数据库连接
# db.close()
# ========================================


db = pymysql.connect("localhost","root","121212","newtest")

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

# 使用 execute() 方法执行 SQL，如果表存在则删除
cursor.execute("DROP TABLE IF EXISTS 58_zufang")

# 使用预处理语句创建表
sql = """CREATE TABLE 58_zufang (
    'title' VARCHAR(200) NOT NULL,
    'way' VARCHAR(30) NOT NULL,
    'price' FLOAT (5) NOT NULL,
    'room_size' VARCHAR(60) NOT NULL,
    'address' VARCHAR(100) NOT NULL,
    'description' VARCHAR(200) NOT NULL,
    'pic_urls' VARCHAR(200) NOT NULL,
    'subway_line' int(5) NOT NULL,)"""

cursor.execute(sql)

# 关闭数据库连接
db.close()

#
# '''
# CREATE TABLE IF NOT EXISTS `runoob_tbl`(
#    `runoob_id` INT UNSIGNED AUTO_INCREMENT,
#    `runoob_title` VARCHAR(100) NOT NULL,
#    `runoob_author` VARCHAR(40) NOT NULL,
#    `submission_date` DATE,
#    PRIMARY KEY ( `runoob_id` )
# )ENGINE=InnoDB DEFAULT CHARSET=utf8;
# '''
# # -------------------------------
# '''
# CREATE TABLE IF NOT EXISTS `58_zufang`(
#     'id' INT UNSIGNED AUTO_INCREMENT,
#     'title' VARCHAR(200) NOT NULL,
#     'way' VARCHAR(30) NOT NULL,
#     'price' FLOAT (5) NOT NULL,
#     'room_size' VARCHAR(60) NOT NULL,
#     'address' VARCHAR(100) NOT NULL,
#     'description' VARCHAR(200) NOT NULL,
#     'pic_urls' VARCHAR(200) NOT NULL,
#     'subway_line' int(5) NOT NULL,
#
# )ENGINE=InnoDB DEFAULT CHARSET=utf8;
# '''
#
# '''
# id
# title
# way    char  方式---押一付三
# price   float
# room_size  char
# address
# description
# pic_urls  图片 列表
# subway_line  int 自己指定
# '''
# title = data.xpath('''//div[@class="house-title"]//h1''').text().strip()
# # 高碑店村&#x9e3a;号院 &#x9fa4;室&#x9fa4;厅&#x9fa4;卫 |高碑店村鸺号院 龤室龤厅龤卫  ----- 高碑店村5号院 1室1厅1卫
# # //title-----【10图】高碑店村5号院 1室1厅1卫(个人),惠河南街-北京58同城
# if not title:
#     return None
# # 方式---押一付三
# way = data.xpath('''//div[@class="house-pay-way f16"]//span[@class="c_333"]''').text().strip()
# # price
# price = data.xpath('''//div[@class="house-pay-way f16"]//span[@class="c_ff552e"]''').text().strip()
#
# #room_size   房屋类型---1室1厅1卫   30平  数字错位
# room_size = data.xpath('''(//ul[@class="f14"]//li)[2]''').text().strip()
# # 所属区域
# address = data.xpath('''(//ul[@class="f14"]//li)[5]''').text().strip()
#
# #整租
# retweeted_source = data.xpath('''(//ul[@class="f14"]//li)[1]''').text().strip()
#
# subway_line = ''
# #
# data = self.clear_special_xp(data, '''//script|//style''')
# description = ''
# contents = data.xpathall('''(//ul[@class="introduce-item"]//li)[last()] ''')
# for i in contents:
#     cont = i.text()
#     description += cont
#
# #图片
# pic_urls_list = data.xpathall('''//div[@class="basic-pic-list pr"]//img//@src''')
# if pic_urls_list:
#     for i in pic_urls_list:
#         img_url = i.text().strip()
#         img_url = urljoin(url, img_url)
#         if '.gif' not in img_url:
#             pic_urls.append(img_url)
#
#
# ctime = gtime - datetime.timedelta(minutes=1)
#

# CREATE TABLE `NewTable` (
# `id`  int NOT NULL ,
# `title`  text NULL ,
# `way`  varchar(30) NULL ,
# `price`  float(10,0) NULL ,
# `room_size`  varchar(60) NULL ,
# `address`  varchar(100) NULL ,
# `description`  varchar(200) NULL ,
# `pic_urls`  text NULL ,
# `subway_line`  int(10) NULL ,
# PRIMARY KEY (`id`)
# )
# ;


