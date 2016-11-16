"""
冒泡排序从小到大排序（设列表长度为N）

算法描述：
1．比较相邻的前后二个数据，如果前面数据大于后面的数据，就将二个数据交换（大的在后面）。
2．这样对列表的第0个数据到N-1个数据进行一次遍历后，最大的一个数据就“沉”到列表第N-1个位置。
3．N=N-1，如果N不为0就重复前面二步，否则排序完成。

备注：
1.Python支持对两个数字同时进行交换！a,b = b,a就可以交换a和b的值了
2.可以通过加一个标志改进冒泡排序算法，如果内循环跑一遍该标志都没有变，则说明排序已经完成
3.算法复杂度O(n2)
4.适用于数据量小的情况
"""


def bubble_sort(a_list):
    exchanges = True
    pass_num = len(a_list) - 1
    while pass_num > 0 and exchanges:
        exchanges = False
        for i in range(pass_num):
            if a_list[i] > a_list[i + 1]:
                exchanges = True  # 有任意一次交换即改变此值
                # temp = a_list[i]
                # a_list[i] = a_list[i + 1]
                # a_list[i + 1] = temp
                a_list[i], a_list[i + 1] = a_list[i + 1], a_list[i]
        pass_num -= 1


if __name__ == '__main__':
    a_list = [20, 40, 30, 90, 50, 80, 70, 60, 110, 100]
    bubble_sort(a_list)
    print(a_list)
