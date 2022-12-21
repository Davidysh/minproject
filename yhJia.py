from collections import defaultdict
import json

def Search(a,target): # 查找功能
    try :
        print(f"{target}的意思是 {a[target]}")
    except KeyError:
        print(f"{target}不存在在该词典中")

def Add(a,English,Chinese): # 增添功能+修改功能
    a[English] = Chinese

def Delete(a,English): # 删除功能
    a.pop(English)

adict = dict()
with open("test_data.json",'r', encoding='utf-8') as f1:
    adict = json.load(f1)

state = "y"
while(state == "y"):
    print(9*'*'+"菜单界面"+9*'*')
    print("**1.查找          2.增添**")
    print("**3.修改          4.删除**")
    print(26*"*")
    operation = input("请问您要访问那个功能：")
    if operation == "1" :
        p = 'y'
        while(p == 'y'):
                target = input("请输入您要查找的单词：")
                Search(adict,target)
                p = input("是否重复该操作{y/n}")
        state = input("是否返回菜单{y/n}")
        continue
    elif operation == "2" :
        p = 'y'
        while(p == 'y'):
                English = input("请输入您要增加的单词：")
                Chinese = input("以及它所对应的中文意思：")
                Add(adict,English,Chinese)
                p = input("是否重复该操作{y/n}")
        state = input("是否返回菜单{y/n}")
        continue
    elif operation == "3" :
        p = 'y'
        while(p == 'y'): 
                English = input("请输入您要修改的单词：")
                Chinese = input("以及它所对应的修改后的中文意思：")
                Add(adict,English,Chinese)
                p = input("是否重复该操作{y/n}")
        state = input("是否返回菜单{y/n}")
        continue
    elif operation == "4" :
        p = 'y'
        while(p == 'y'):
                English = input("请输入您要删除的单词：")
                Delete(adict,English)
                p = input("是否重复该操作{y/n}")
        state = input("是否返回菜单{y/n}")
        continue  

state = input("是否保存上述操作：{y/n}")
if state == 'y':
    with open('dictionary_library.txt','w',encoding = 'UTF-8') as fp: 
        for item in adict.items():
            fp.write('\n'+str(item))

    json_str = json.dumps(adict,ensure_ascii=False)
    with open('test_data.json', 'w',encoding='utf-8') as json_file:
        json_file.write(json_str)

print("感谢使用")