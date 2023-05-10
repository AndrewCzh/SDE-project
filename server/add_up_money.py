

def add_up_money(uid, money, uid_dict):
    if uid in uid_dict:
        uid_dict[uid] += money
        return money
    else:
        print('uid is not in the uid_dict')
        return -1


def main():
    uid_dict = {'123': 110, '222': 10, 'test_uid': 0}
    ret = add_up_money('test_uid', 10, uid_dict)
    print(f'{ret=}')


if __name__ == '__main__':
    main()
