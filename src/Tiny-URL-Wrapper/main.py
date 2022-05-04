import requests

def make_url(url):
    """
    make tiny url
    """
    params = {'original': 'https://example.com'}
    url = f"https://tinyurl.orraorange.repl.co/api/make_url"
    r = requests.post(url, params=params)
    print(r.text)
    return r.text

make_url('AAA')