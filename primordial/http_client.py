import requests


class HttpClient:
    def __init__(self, proxies=None, headers={}):
        self.session = requests.Session()
        self.proxies = proxies

        for header, value in headers.items():
            self.add_header(header, value)

        self.add_header(
            'User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:64.0) Gecko/20100101 Firefox/64.0')

    def add_header(self, header, value):
        self.session.headers[header] = value

    def post(self, url, data):
        response = self.session.post(url=url, data=data, proxies=self.proxies)
        return response

    def get(self, url):
        response = self.session.get(url=url, proxies=self.proxies)
        return response
