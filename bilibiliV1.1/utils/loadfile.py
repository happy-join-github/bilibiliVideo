# 加载用户文件
def logfile():
    file = open('dataset/user.txt','r',encoding='utf-8').readlines()
    user_dic = {key:val for key,val in zip([item.split()[0] for item in file],[item.split()[1] for item in file])}
    return user_dic