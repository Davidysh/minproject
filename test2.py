from collections import defaultdict
import json

def Add(a,English,Chinese): # 增添功能+修改功能
    a[English] = Chinese
        
with open("test_data.json",'r') as f1:
            adict = json.load(f1)
    
            English = input("请输入您要修改的单词：")
            Chinese = input("以及它所对应的修改后的中文意思：")
            Add(adict,English,Chinese)
            
json_str = json.dumps(adict,ensure_ascii=False)
with open('test_data.json', 'w') as json_file:
    json_file.write(json_str)

f2 = open('test_data.json', 'r')
info_data = json.load(f2)
print(info_data)