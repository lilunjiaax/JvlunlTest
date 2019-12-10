from aip import AipOcr

from Common import *




app_id = APP_ID
api_key = API_KEY
secret_key = SECRET_KEY

client = AipOcr(app_id, api_key, secret_key)


def get_text_by_img(img_dir):
    with open(img_dir, 'rb') as fp:
        a = fp.read()
    options = {}
    options["detect_direction"] = "true"
    options["probability"] = "true"
    a_list = client.basicAccurate(a, options)['words_result']
    result_list = [item['words'] for item in a_list]
    return result_list


a_dict = {'log_id': 3491660754211513764,
          'direction': 0,
          'words_result_num': 7,
          'words_result':
              [{'words': '产品推广', 'probability': {'variance': 0.0, 'average': 0.999913, 'min': 0.999808}},
               {'words': '产品优化', 'probability': {'variance': 0.0, 'average': 0.999805, 'min': 0.999699}},
               {'words': '选定目标用户群', 'probability': {'variance': 0.0, 'average': 0.999533, 'min': 0.998284}},
               {'words': '对用户群体进行调研', 'probability': {'variance': 0.0, 'average': 0.999867, 'min': 0.999629}},
               {'words': '产品测试', 'probability': {'variance': 0.0, 'average': 0.999856, 'min': 0.999547}},
               {'words': '制定定价策略', 'probability': {'variance': 4e-06, 'average': 0.998745, 'min': 0.994571}},
               {'words': '设计产品实例', 'probability': {'variance': 3e-06, 'average': 0.999047, 'min': 0.995462}}]
          }












