from collections import defaultdict
import json

video = defaultdict(list)
video["label"].append("haha")
video["data"].append(234)
video["score"].append(0.3)
video["label"].append("xixi")
video["data"].append(123)
video["score"].append(0.7)

json_str = json.dumps(video)
with open('test_data.json', 'w') as json_file:
    json_file.write(json_str)

# JSON到字典转化
f2 = open('test_data.json', 'r')
info_data = json.load(f2)
print(info_data)
# 显示数据类型
print(type(info_data))

