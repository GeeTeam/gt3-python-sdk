import requests

scheme = "https://"
url = "api.geetest.com/"
paratemer = "gt=b4e0149ad455e5434c210ab85d0e22be"

response = requests.get("".join((scheme,url,paratemer)))

