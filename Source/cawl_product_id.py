
import requests
import time
import random
import pandas as pd


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36',
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'en-US,en;q=0.9',
    'Referer': 'https://tiki.vn/thiet-bi-kts-phu-kien-so/c1815',
    'x-guest-token': 'Qgqx7sR5VtEz2Jld6jecMyPibnOLk0pC',
    'Connection': 'keep-alive',
    'TE': 'Trailers',
}

params = {
    'limit': '300',
    'sort': 'top_seller',
    'aggregations': '2',
    'version' : 'home-persionalized',
    'trackity_id': '2a362f2d-d55c-224e-ca0c-e8a1dbab9e8a',
    'category': '1815',
    'page': '1',
    'urlKey':  'thiet-bi-kts-phu-kien-so',
}

product_id = []
for i in range(1,60):
    params['page'] = i
    response = requests.get('https://tiki.vn/api/v2/products', headers=headers, params=params)#, cookies=cookies)
    if response.status_code == 200:
        print('request success!!!')
        for record in response.json().get('data'):
            product_id.append({'id': record.get('id')})
    time.sleep(random.randrange(3, 10))

df = pd.DataFrame(product_id)
df.to_csv('product_id.csv', index=False)
