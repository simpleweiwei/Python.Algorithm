"""
选择排序的思想就是：待找到了最适合的那位数的位置我才选择与它进行交换，交换次数自然就变少了

算法描述：
1．假设第1个数是最小的。
2．然后将这个最小的数与剩下的数依次对比，记下最小数的位置索引。
3．最后将最小的数与第1个数交换。（此时列表中最小的数已经排在第1位了）
4. 再假设第2个数是最小的。
5．然后将这个最小的数与剩下的数依次对比，记下最小数的位置索引。
6．最后将最小的数与第2个数交换。（此时列表中次小的数已经排在第2位了）
7. 假设第3个数是最小的，依次重复以上过程即可。。。


备注：
1.如果假设的最小数的位置索引与查找出来的最小数位置索引相同（说明假设对了，不需交换）
2.外层只需要假设N-1次,因此循环N-1次
3.最坏时间复杂度O(n2)
"""


def selection_sort(a_list):
    for i in range(len(a_list) - 1):
        pos_of_min = i
        for location in range(i + 1, len(a_list)):
            if a_list[pos_of_min] > a_list[location]:
                pos_of_min = location
        if pos_of_min != i:  # 说明假设最小数失败，需要交换
            a_list[i], a_list[pos_of_min] = a_list[pos_of_min], a_list[i]


if __name__ == '__main__':
    a_list = [54, 26, 93, 17, 77, 31, 44, 55, 20, 21, 20, 17]
    selection_sort(a_list)
    print(a_list)
