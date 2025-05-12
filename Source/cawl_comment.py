import requests
import pandas as pd
import time
import random
from tqdm import tqdm

cookies = {
    '__C' : '4_1746586009',
    '__create' : '1746520249',
    '__iid' : '749',
    '__iid' : '749',
    '__IP' : '20369876',
    '__R' : '1',
    '__RC' : '4',
    '__Secure-1PAPISID' : 'LsXBGU3WKK2hV1I2/AQvt-Iy2haZ9qOtUs',
    '__Secure-1PAPISID' : 'LsXBGU3WKK2hV1I2/AQvt-Iy2haZ9qOtUs',
    '__Secure-1PSID' : 'g.a000twiuVu1-D9k9zfCVLbBfmsp1df1ZBj8oJIKyN_jeOdgx-I_ruoZRQOjojp3F8oO6S24SeQACgYKAasSARQSFQHGX2Miq97yhSHrLT6F0HMd7Ux33xoVAUF8yKoBmvu58f-VJNrVRFXGEofv0076',
    '__Secure-1PSID' : 'g.a000vwiuVqJNVcfu4N8h1MU-9irjSobalnD608uwjBMUIHJJ82-yPCvfJ_wYWoTju3WcuZb8ygACgYKAXASARQSFQHGX2Miq7sgkriZteI05N-B9YNJaBoVAUF8yKpD6-4LTt793rxX1vQe3rMv0076',
    '__Secure-1PSIDCC' : 'AKEyXzWhYGmXskfX5PDGcBQZqfe52-BEC0WyKGv-GT9HLsZrXpR0_epp1zE7gf1zSPboUoWjEFA',
    '__Secure-1PSIDTS' : 'sidts-CjIBjplskBkRHDML9qm3HAVQxAX4Cbe-HnisWEfBTZP3KbDtF19xzfHk2E6Hnrd4Wk8sQhAA',
    '__Secure-3PAPISID' : 'LsXBGU3WKK2hV1I2/AQvt-Iy2haZ9qOtUs',
    '__Secure-3PAPISID' : 'LsXBGU3WKK2hV1I2/AQvt-Iy2haZ9qOtUs',
    '__Secure-3PSID' : 'g.a000twiuVu1-D9k9zfCVLbBfmsp1df1ZBj8oJIKyN_jeOdgx-I_rKhpXPpidGfZiWGE0fgDwsAACgYKAa4SARQSFQHGX2MiXu61d4mUgftXN-y_sV67JRoVAUF8yKoQPo8oMIIbInGoqkMWIyoR0076',
    '__Secure-3PSID' : 'g.a000vwiuVqJNVcfu4N8h1MU-9irjSobalnD608uwjBMUIHJJ82-yik9RRTt58N4ZYApjdfGltAACgYKATESARQSFQHGX2MiXrkrqBRYyC-JGfrFJnzHYRoVAUF8yKqD8iBBTwcaVynMW7U5b1in0076',
    '__Secure-3PSIDCC' : 'AKEyXzVbyfuqRz1XjnaUtjTBuHLVHfzTQleR9LXdSlCvPvok-CmjQwphE688-UshDsSZhhnKRuEb',
    '__Secure-3PSIDTS' : 'sidts-CjIBjplskBkRHDML9qm3HAVQxAX4Cbe-HnisWEfBTZP3KbDtF19xzfHk2E6Hnrd4Wk8sQhAA'
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36',
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'vi-VN,vi;q=0.8,en-US;q=0.5,en;q=0.3',
    'Referer': 'https://tiki.vn/dien-thoai-samsung-galaxy-a06-4gb-128gb-da-kich-hoat-bao-hanh-dien-tu-hang-chinh-hang-p277776275.html?itm_campaign=CTP_YPD_TKA_PLA_UNK_ALL_UNK_UNK_UNK_UNK_X.306103_Y.1888423_Z.4029127_CN.Samsung-l-A06&itm_medium=CPC&itm_source=tiki-ads&spid=277776284',
    'x-guest-token': 'Qgqx7sR5VtEz2Jld6jecMyPibnOLk0pC',
    'Connection': 'keep-alive',
    'TE': 'Trailers',
}

params = {
    'product_id': '277776275',
    'sort': 'score|desc,id|desc,stars|all',
    'page': '1',
    'limit': '20',
    'include': 'comments,contribute_info,attribute_vote_summary'
}

def comment_parser(json):
    d = dict()
    d['id'] = json.get(id)
    d['title'] = json.get('title')
    d['content'] = json.get('content')
    d['thank_count'] = json.get('thank_count')
    d['customer_id']  = json.get('customer_id')
    d['rating'] = json.get('rating')
    d['created_at'] = json.get('created_at')
    d['customer_name'] = json.get('created_by').get('name')
    d['purchased_at'] = json.get('created_by').get('purchased_at')
    return d


df_id = pd.read_csv('product_id_ncds2.csv')
p_ids = df_id.id.to_list()
result = []
for pid in tqdm(p_ids, total=len(p_ids)):
    params['product_id'] = pid
    print('Crawl comment for product {}'.format(pid))
    for i in range(10):
        params['page'] = i
        response = requests.get('https://tiki.vn/api/v2/reviews', headers=headers, params=params, cookies=cookies)
        if response.status_code == 200:
            print('Crawl comment page {} success!!!'.format(i))
            for comment in response.json().get('data'):
                result.append(comment_parser(comment))
df_comment = pd.DataFrame(result)
df_comment.to_csv('comments_data.csv', index=False)

