def Count_Sort(list):
    # 桶的个数
    Bucket_num =  max(list) - min(list) + 1
    # 入桶
    BUCKET = [0] * (max(list) - min(list) + 1)
    for i in range(len(list)):
        BUCKET[list[i] - min(list)] += 1
    # 设置新的数组来存放
    new_list = []
    for j in range(Bucket_num):
        if BUCKET[j] != 0:
            new_list += [j + min(list)] * BUCKET[j]
    return new_list

print(Count_Sort([3,4,6,1,2]))