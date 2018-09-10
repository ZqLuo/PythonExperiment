import pymysql


def getDB(ip, username, password, dbname):
        return pymysql.connect(ip, username, password, dbname)


def excuteSQL(db, sql, values, closedb=True):
        # 使用cursor()方法获取操作游标
    cursor = db.cursor()
    try:
            # 执行sql语句
        cursor.execute(sql, values)
        # 提交到数据库执行
        db.commit()
    except Exception as err:
        print(err)
        # 如果发生错误则回滚
        db.rollback()

    # 关闭数据库连接
    if(closedb):
            db.close()
