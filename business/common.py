import requests


def create_topic(topicdata):

    url = 'http://app.devapi2.xcompetition.com.cn'
    r = requests.post(url=url,json=topicdata)
    return r

def get_token():
    return