def get_sorted_keys_values(dict_obj):
    # 此处写你的代码 
    items=sorted(dict.items(dict_obj))
    sorted_items={k:v for k,v in items}
    L=[]
    L.append(list(sorted_items.keys()))
    L.append(list(sorted_items.values()))
    return L
# 获取用户输入转为字典
dictionary = eval(input())

# 调用函数
print(get_sorted_keys_values(dictionary))