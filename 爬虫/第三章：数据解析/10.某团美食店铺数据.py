import pprint
import requests
import csv
import re
url='http://meishi.meituan.com/i/api/channel/deal/list'
headers={
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36 Edg/98.0.1108.62',
'Referer': 'http://meishi.meituan.com/i/?ci=790&stid_b=1&cevent=imt%2Fhomepage%2Fcategory1%2F1',
'Cookie': '__mta=256667956.1651894911178.1651901625900.1651901844627.8; iuuid=4AA59F3EFB8A9F3EF4930FC76B0E120CFF197B97EE34D0662880B1825B9D12A0; _lx_utm=utm_source%3DBaidu%26utm_medium%3Dorganic; _lxsdk_cuid=1809c9b2094c8-00d788c49120c1-977173c-144000-1809c9b2095c8; _lxsdk=4AA59F3EFB8A9F3EF4930FC76B0E120CFF197B97EE34D0662880B1825B9D12A0; webp=1; latlng=38.717976,113.270724,1651894854206; __utma=74597006.230094382.1651894854.1651894854.1651894854.1; __utmz=74597006.1651894854.1.1.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; cityname=%E5%A4%AA%E8%B0%B7%E5%8C%BA; i_extend=C_b1Gimthomepagecategory11H__a; client-id=c075c378-0c8d-4aca-ae18-b598521077d1; _hc.v=e06353a9-fd43-2e77-5b29-9695d1dfa1ca.1651894911; uuid=0f20dff3e2fa4497879a.1651895026.1.0.0; ci=790; meishi_ci=790; cityid=790; logan_session_token=56mzi3q2unlm0ngybwbz; _lxsdk_s=1809d025fcb-395-d69-ac7%7C%7C132'
}
data={
    'app': '""',
    'areaId': '0',
    'cateId': '1',
    'deal_attr_23': '""',
    'deal_attr_24': '""',
    'deal_attr_25': '""',
    'limit': '10',
    'lineId': '0',
    'offset': '120',
    'optimusCode': '10',
    'originUrl': '"http://meishi.meituan.com/i/?ci=790&stid_b=1&cevent=imt%2Fhomepage%2Fcategory1%2F1"',
    'partner': '126',
    'platform': '3',
    'poi_attr_20033': '""',
    'poi_attr_20043': '""',
    'riskLevel': '1',
    'sort': '"default"',
    'stationId': '0',
    'uuid': '"0f20dff3e2fa4497879a.1651895026.1.0.0"',
    'version': '"8.2.0"',
}
response=requests.post(url=url,data=data,headers=headers).json()
dd=response['data']['poiList']['poiInfos']

f=open('./data.csv','a',encoding='utf-8',newline='')#a 是追加保存
csv_write=csv.DictWriter(f, fieldnames=[
    '店铺名',
    '饮食类型',
    '最低消费',
    '评分',
    '商圈',
    '商家地址',
    '商家电话',
    '商家网址',
])
csv_write.writeheader()
for i in dd:
    dit={
        '店铺名':i['name'],
        '饮食类型':i['cateName'],
        '最低消费':i['avgPrice'],
        '评分':i['avgScore'],
        '商圈': i['areaName'],
        '商家网址':'https://meishi.meituan.com/i/poi/'+i['poiid']
    }
    header = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36 Edg/98.0.1108.62',
    'Cookie':'__mta=211246762.1651845222043.1651922980164.1651923023154.20; __mta=211246762.1651845222043.1651922834033.1651923018096.8; _lxsdk_cuid=180999bb7acc8-00936cd100ef0b-39736c06-144000-180999bb7acc8; iuuid=6084D252C544E218851C070398EEF1E3718303F7158C9913893E8A1FC699DFBD; _lxsdk=6084D252C544E218851C070398EEF1E3718303F7158C9913893E8A1FC699DFBD; webp=1; uuid=7030c1d5e63242a28611.1651844597.1.0.0; a2h=4; client-id=410b0432-9584-42dc-b02f-463121442b85; _hc.v=c5f93f4a-f92f-d241-1ac8-348b4f0af4f5.1651845222; ci=790; cityname=%E5%A4%AA%E8%B0%B7%E5%8C%BA; IJSESSIONID=node01sdhmv0nfyj35b06eufj3hy1075771092; __utma=74597006.592180938.1651844568.1651844568.1651922628.2; __utmz=74597006.1651922628.2.2.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utmc=74597006; ci3=1; WEBDFPID=8xz5xzxv6y34568001v358z6x4426w2z8190v56z5779795890zu01z1-1652009074304; wm_order_channel=mtib; cssVersion=cfb14028; utm_source=60030; request_source=openh5; au_trace_key_net=default; openh5_uuid=6084D252C544E218851C070398EEF1E3718303F7158C9913893E8A1FC699DFBD; channelType={%22mtib%22:%220%22}; channelConfig={%22channel%22:%22default%22%2C%22type%22:0%2C%22fixedReservation%22:{%22reservationTimeStatus%22:0%2C%22startReservationTime%22:0%2C%22endReservationTime%22:0}}; meishi_ci=790; cityid=790; _lx_utm=utm_source%3DBaidu%26utm_medium%3Dorganic; latlng=38.7839,113.075934,1651923008105; __utmb=74597006.36.9.1651923017741; i_extend=C_b1Gimthomepagecategory11H__a; logan_session_token=h3zl6axtkk6t7piny2jt; _lxsdk_s=1809e42ec7c-1fe-d02-1b6%7C%7C78',
    'Referer':'http://meishi.meituan.com/i/?ci=790&stid_b=1&cevent=imt%2Fhomepage%2Fcategory1%2F1',
            }
    hh = requests.get(url=dit['商家网址'],headers=header).text
    obj = re.compile(r'addr":"(?P<addr>.*?)","phone":"(?P<phone>.*?)"')
    result = obj.finditer(hh)
    for item in result:
        addr = item.group('addr')
        phone = item.group('phone')
        dit['商家地址']=addr
        dit['商家电话']=phone
    print(dit)
    csv_write.writerow(dit)






