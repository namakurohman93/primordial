import requests

class HttpClient:
    def __init__(self, **kwargs):
        self.headers = kwargs.pop('headers', {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:66.0) Gecko/20100101 Firefox/66.0'})
        self.cookies = kwargs.pop('cookies', requests.cookies.RequestsCookieJar())
        self.timeout = kwargs.pop('timeout', 20.0)
        self.proxies = kwargs.pop('proxies', None)
        self._hooks = {'response': (self._update_cookies,)}

    def _update_cookies(self, r, *args, **kwargs):
        self.cookies.update(r.cookies)

    def _request(self, method, url, **kwargs):
        headers = kwargs.pop('headers', self.headers)
        cookies = kwargs.pop('cookies', self.cookies)
        timeout = kwargs.pop('timeout', self.timeout)
        proxies = kwargs.pop('proxies', self.proxies)
        hooks = kwargs.pop('hooks', self._hooks)
        with requests.request(
                method=method,
                url=url,
                headers=headers,
                cookies=cookies,
                timeout=timeout,
                proxies=proxies,
                hooks=hooks,
                **kwargs) as r:
            return r

    def post(self, url, **kwargs):
        return self._request('POST', url, **kwargs)

    def get(self, url, **kwargs):
        return self._request('GET', url, **kwargs)
