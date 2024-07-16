# 读取计划控制门店清单0710.xlsx

import pandas as pd
import numpy as np

# 读取sheet: 计划控制内的空调设备清单
df = pd.read_excel('计划控制门店清单0710.xlsx', sheet_name='计划控制内的空调设备清单')
# 将df的数据转化为list，list中每一个元素为dict，dict的key为列名，dict的value为列的值
df_list = df.to_dict(orient='records')
# 保留每一个dict的assetId，所属门店assetId，Facility_Spec_FMS，生成一个新的dict，所有dict放入一个新的list
new_list = []
for i in df_list:
  new_list.append({'assetId': "\"" + i['assetId'] + "\"", 'siteId': "\""+i['所属门店assetID']+"\"", 'manufacturer': i['Facility_Spec_FMS']})
# 筛选manufacturer为"大金空调"的数据
list_DARKIN = [i for i in new_list if i['manufacturer'] == '大金空调']
# 合并siteId，生成一个新的dict，dict的assetId为siteId相同元素的assetId拼接，siteId保持不变所有dict放入一个新的list
list_DARKIN = [{'assetId': ','.join([i['assetId'] for i in list_DARKIN if i['siteId'] == j['siteId']]), 'siteId': j['siteId']} for j in list_DARKIN]
# list 去重
list_DARKIN = list({i['siteId']: i for i in list_DARKIN}.values())
# 每200个元素拼接为一个新dict，dict的key与原来一致，value为200个dict对应key元素用逗号拼接，生成一个新的list
list_DARKIN = [{'assetId': ','.join(i['assetId'] for i in list_DARKIN[j:j+200]), 'siteId': ','.join(i['siteId'] for i in list_DARKIN[j:j+200])} for j in range(0, len(list_DARKIN), 200)]
#  new_list 输出为一个xlsx文件
pd.DataFrame(list_DARKIN).to_excel('0710_DARKIN.xlsx')
