def saveData(type):
    num = 0
    def wapper(content):
        print(str.format("数据保存至【{target}】,保存内容为：{content}",target=type,content=content))
        nonlocal num
        num += 1
        print(str.format("今日已保存数据条数：{0}" ,num))
    return wapper


save_to_database = saveData("数据库")
save_to_database("一条订单记录")        
save_to_database("个人信息变更")        