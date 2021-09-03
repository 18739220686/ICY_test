import util.globalv as gl
import ssl

ssl._create_default_https_context = ssl._create_unverified_context
gl.__init__()

###############正式环境##########################
gl.set_value('url', 'http://47.93.9.92:1880/index.php')
gl.set_value('key', '34c3194c732457cca2f5b0bfad8b72fe')

# 设置https
gl.set_value('apiip', 'https://tgnew-test.icy.design/api/tg/admin.php?')
gl.set_value('AIip', 'https://tgnew-test.icy.design/api/ai/api/admin/order')
# 正式环境
# gl.set_value('api','https://tgnew-icy.design/api/tg/admin.php?')
# 设置cookie
gl.set_value('Cookie', 'sessions=%7B%22ai%22%3A%7B%22sessionKey%22%3A%22session%22%2C%22sessionValue%'
                       '22%3A%223e66ccf5-c042-425b-b233-02453cf09e44%22%7D%2C%22tg%22%3A%7B%22sessionKey%'
                       '22%3A%22PHPSESSID%22%2C%22sessionValue%22%3A%22c993adf79f8bde442effa56137cdab75%22%7D%7D;'
                       ' username=COO; userId=1607068293',
             )

# 配置测试计划ID，执行请修改
gl.set_value('test_plan_id', '3086')  # //正式

# 设置APIIP地址
# gl.set_value('apiip','http://csptest.thiztech.com:7001')

# gl.set_value('apiip','http://192.168.68.205:8092')

# 设置环境lab
gl.set_value('lab', 'tg')  # 正式
# 设置邮箱
gl.set_value('emailpassword', 'Chen101033')
gl.set_value('email_host', 'smtphz.qiye.163.com')
gl.set_value('send_user', 'mengyue.chen@yourdream.cc')
