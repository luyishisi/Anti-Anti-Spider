import requests

def main():
    url = "https://www.baidu.com/"
    querystring = {"tn":"92083438_hao_pg"}
    response = requests.request("GET", url, params=querystring)

    with open("baidu.html","wb") as f:
        f.write(response.content)
    print(response.text)
if __name__ == '__main__':
    main()

