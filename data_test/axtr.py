print('-------------打开，读取yaml文件------------')
import yaml

class ReadExtract:
    def read_extract(self):
        #打开文件
        with open('test_dict.yaml', encoding='utf-8') as f:
            result = yaml.load(stream=f,Loader=yaml.FullLoader)
            #返回json格式
            return result

    def write_extract(self,data):
        #写入文件allow_unicode=True返回中文格式
        with open('test_dict.yaml', encoding='utf-8', mode='w') as f:
            yaml.dump(data, stream=f, allow_unicode=True)


# 登录
class Login:
    def token_read(self):
        #打开文件
        with open('login.yaml', encoding='utf-8') as f:
            result = yaml.load(stream=f,Loader=yaml.FullLoader)
            #返回json格式
            return result

    def token_write(self,data):
        #写入文件allow_unicode=True返回中文格式
        with open('login.yaml', encoding='utf-8', mode='w') as f:
            yaml.dump(data, stream=f, allow_unicode=True)


# 寄售数据驱动
class Con:
    def con_read(self):
        #打开文件
        with open('send.yaml', encoding='utf-8') as f:
            result = yaml.load(stream=f,Loader=yaml.FullLoader)
            #返回json格式
            return result

    def con_write(self,data):
        #写入文件allow_unicode=True返回中文格式
        with open('send.yaml', encoding='utf-8', mode='w') as f:
            yaml.dump(data, stream=f, allow_unicode=True)
