class Heap(object):
    def __init__(self,elements):
        self.list = []
        for element in elements:
            self.add(element)
# 接下来就是逐层交换的过程，要保证节点大于他的子节点
# 先把新的元素添加到列表里面去
    def add(self,element):
        self.list.append(element)
        # 找出当前节点的下标，和他的父亲下标
        cur = len(self.list) - 1
        par = (cur - 1)/2
# 逐层交换
        while cur != 0 and self.list[cur] > self.list[par]:
            self.list[cur] , self.list[par] = self.list[par] , self.list[cur]
# 当前结点的下标也是要交换的，变成了原来的父节点的下标，然后再寻找新的父节点。
            cur = par
            par = (cur - 1)/2
# 弹出
    def pop(self):
# 将尾元素删除出来
        self.list[0] , self.list[-1] = self.list[-1] , self.list[0]
        result = self.list.pop(0)
        cur = 0
# 由NEXT来判断是否还需进行交换，是否有子节点（当前节点是否有孩子）
        NEXT = True
# 删除后要进行调整
        while cur < len(self.list) and NEXT:
#到这里先认为是不能进行交换了，由下面的代码来判断是否有孩子节点。
            NEXT = False
# 找出左右孩子的索引下标
            left_child , right_child = (cur * 2) + 1 , (cur * 2) + 2
# 左孩子索引越界，也就是实际上左孩子不存在
            if left_child >= len(self.list):
                break
# 接下来分为右孩子存在和不存在的情况
# 右孩子不存在
            if right_child  >= len(self.list):
                if self.list[left_child] > self.list[cur]:
                    self.list[left_child] , self.list[cur] = self.list[cur] , self.list[left_child]
                    cur = left_child
                    NEXT = True
# 右孩子存在
            else:
                # 先左右孩子进行比较大小，找出最大的
                max_index = right_child if self.list[right_child] > self.list[left_child] else left_child
                # 再将最大的子节点，与他的父节点进行比较
                if self.list[cur] < self.list[max_index]:
                    self.list[cur] = self.list[max_index]
                    cur = max_index
                    NEXT = True


            return result