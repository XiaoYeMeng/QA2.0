i = 0
def test():
    global i

    lb_que['text'] = dt.topic_random[i]['topic_que']
    bt_a['text'] = dt.topic_random[i]['topic_a']
    bt_b['text'] = dt.topic_random[i]['topic_b']
    bt_c['text'] = dt.topic_random[i]['topic_c']
    bt_d['text'] = dt.topic_random[i]['topic_d']
    i += 1
    lb_number['text'] = i
    print(i)