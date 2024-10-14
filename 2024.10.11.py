# 指定编码方式为 utf8
f = open('tmp.txt','w',encoding='utf8')

# write方法会将字符串编码为utf8字节串写入文件
f.write('白月黑羽：祝大家好运气')

# 文件操作完毕后， 使用close 方法关闭该文件对象
f.close()
# a 表示 追加模式 打开文件
f = open('tmp.txt','a',encoding='gb2312')
f.write('白月黑羽再次祝大家 ：good luck')
f.close()