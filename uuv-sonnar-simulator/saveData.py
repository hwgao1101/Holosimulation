import pickle


def save_pkl(filename, state):
    '''
    这个函数用于保存pkl数据
    filename : 是要保存的文件名
    :return:
    '''
    # wb是覆盖写，如果需要追加，则为‘ab'
    f = open(filename, 'wb')
    # 待写入数据
    datas = state
    # 写入
    data = pickle.dump(datas, f, -1)
    # 关闭文件
    f.close()


def load_pkl(filename):
    #加载数据集中的一个数据示例，查看存储的数据是什么样的
    f = open(filename,'rb')
    data = pickle.load(f)
    print(type(data))
    print(data.keys())
    print(data)

    # print('OrientationSensor',data['OrientationSensor'])
    # print('LocationSensor',data['OrientationSensor'])
    # print('PoseSensor',data['OrientationSensor'])

def munPrint():
    for i in range(0,100):
        print(i)



if __name__ == '__main__':
    filename = './1.pkl'
    load_pkl(filename)
    # munPrint()
    # filename = './mytest.pkl'
    # state = {"Name": "gaohaowen", "Age": 23, "School": "HITsz"}
    # save_pkl(filename,state)
    # print("Save finished!")
    # load_pkl(filename)
