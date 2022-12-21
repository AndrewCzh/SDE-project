import server.add_up_money as aum

test_uid = 'test_uid'
uid_dict = {'123': 110, '222': 10, 'test_uid': 0}


def test_add_up_money_w_uid():
    ret = aum.add_up_money(test_uid, 7, uid_dict)
    assert isinstance(ret, int)
    assert ret == 7


def test_add_up_money_wo_uid():
    ret = aum.add_up_money('00000', 7, uid_dict)
    assert ret == -1
