import requests
import time
import json
import re


# 上传图片到路过图床
def send_luguo(img_loc=None):
    # 提交的数据为multi-part,一部分是文件，一部分是数据
    
    ## 打开文件二进制流，命名为source，抓取到的，类型为image/jpeg
    img = open(img_loc, "rb")
    files = [('source', (img_loc.split('\\')[-1], img, 'image/png'))]
    print("files is",files)
    ## 提交的数据中有一个重要的字符串为auth_token，基本上会定时变，所以在上传之前我们先访问一次页面获取一下 
    auth_token = get_auth_token()
    print("token is",auth_token)
    data = {
        'type': 'file',
        'action': 'upload',
        'timestamp': int(time.time()) * 1000,
        'auth_token': auth_token,
        'nsfw': "0"
    }
	
    ## 请求的地址
    des_url = 'https://imgtu.com/json'
    
    ## 提交数据和文件，cookies也是转换好的
    try:
        des_post = requests.post(
            url=des_url,
            data=data,
            files=files,
            cookies=luguo_cookies)
        response = des_post.content.decode()
        data = json.loads(response)
        print(data)
        return data['image']['url']
    except Exception as exc:
        print('截图上传失败……%s' % exc)
        return None


# 上传之前先访问一次页面获取auth_token
def get_auth_token():
    url = 'https://imgtu.com/'
    response = requests.get(url, cookies=luguo_cookies)
    html = response.content.decode()
    token = re.search('auth_token=[a-z0-9]*', html).group()
    token = token.split('=')[-1].strip()
    return token


## 将cookie字符串转换成字典的形式
def cookies_raw2jar(raw: str) -> dict:
    """
    Arrange Cookies from raw using SimpleCookies
    """
    if not raw:
        raise ValueError("The Cookies is not allowed to be empty.")

    from http.cookies import SimpleCookie
    cookie = SimpleCookie(raw)
    return {key: morsel.value for key, morsel in cookie.items()}


if __name__ == "__main__":
    "PHPSESSID=3ovtphmva9u0r67rnd736njcpt; _ga=GA1.1.1186894245.1662283907; __gads=ID=1a06a119eecaaae4-223b85a63bd6001c:T=1662283908:RT=1662283908:S=ALNI_MbImljYLKsSjQ3lE8Y46rE3CqHTtA; __gpi=UID=0000097138941c6f:T=1662283908:RT=1662283908:S=ALNI_MavSsbn_aQWg5EUK1kmAQLIy2d_2w; KEEP_LOGIN=hflFg:a9f88c5dc0819e342feee42529af2e8cb22f75034ea3cdf94c4c285a3dfbb1dd00be4965781c89b549dabd83f1c4df0256bb57357ca209af8121da52659158e98b88d77f50d45fb594ff5aa0f22ff:1662284027; _ga_CZP2J5CMLW=GS1.1.1662283906.1.1.1662284704.0.0.0"
    # luguo_cookie_raw = "PHPSESSID=3ovtphmva9u0r67rnd736njcpt; _ga=GA1.1.1186894245.1662283907; __gads=ID=1a06a119eecaaae4-223b85a63bd6001c:T=1662283908:RT=1662283908:S=ALNI_MbImljYLKsSjQ3lE8Y46rE3CqHTtA; __gpi=UID=0000097138941c6f:T=1662283908:RT=1662283908:S=ALNI_MavSsbn_aQWg5EUK1kmAQLIy2d_2w; KEEP_LOGIN=hflFg:a9f88c5dc0819e342feee42529af2e8cb22f75034ea3cdf94c4c285a3dfbb1dd00be4965781c89b549dabd83f1c4df0256bb57357ca209af8121da52659158e98b88d77f50d45fb594ff5aa0f22ff:1662284027; _ga_CZP2J5CMLW=GS1.1.1662283906.1.1.1662284704.0.0.0" # 登录后获取到的cookie字符串
    luguo_cookie_raw = "PHPSESSID=3ovtphmva9u0r67rnd736njcpt; _ga=GA1.1.1186894245.1662283907; __gads=ID=1a06a119eecaaae4-223b85a63bd6001c:T=1662283908:RT=1662283908:S=ALNI_MbImljYLKsSjQ3lE8Y46rE3CqHTtA; __gpi=UID=0000097138941c6f:T=1662283908:RT=1662283908:S=ALNI_MavSsbn_aQWg5EUK1kmAQLIy2d_2w; KEEP_LOGIN=hflFg:a9f88c5dc0819e342feee42529af2e8cb22f75034ea3cdf94c4c285a3dfbb1dd00be4965781c89b549dabd83f1c4df0256bb57357ca209af8121da52659158e98b88d77f50d45fb594ff5aa0f22ff:1662284027; _ga_CZP2J5CMLW=GS1.1.1662283906.1.1.1662284758.0.0.0"
    luguo_cookies = cookies_raw2jar(luguo_cookie_raw) # 转换成字典
    print("cookies is ",luguo_cookies)
    img_path = r"./baseline.png" # 测试的图片链接
    send_luguo(img_path) # 上传返回的是图片的地址