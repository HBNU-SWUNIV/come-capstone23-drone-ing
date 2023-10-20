import rospy
import base64
import time
from std_msgs.msg import String


def talker():
    #rate_list = [0.4, 1, 2]
    #rate_cnt = 0
    rate2 = 1
    q = 20
    loc = 'loc3'

    rospy.init_node('talker', anonymous=True)
    pub = rospy.Publisher('image/text', String, queue_size = q)

    while (pub.get_num_connections() == 0):
        pass

    count = 1

    while not rospy.is_shutdown():

        rate = rospy.Rate(rate2)

        if count == 1:
            f = open('data_pub_' + str(loc) + '_' + 'qSize' + str(q) + '_' + 'rate' + str(rate2) + '.txt', 'a')
            f.write('\n' + 'loc : 1,' + 'qSize : ' + str(q) + ',rate : ' + str(rate2) + '\n')
            f.close()

        encode_start = time.time()
        with open('/home/nano/Image/image_50.jpg' , 'rb') as imageFile:
            text = base64.b64encode(imageFile.read())
            text = text.decode('utf-8')
        encode_end = time.time() - encode_start

        pub_start = time.time()
        pub.publish(str(count) + ',' + text + ',' + str(time.time()))
        pub_end = time.time() - pub_start

        print(count)
        print("encode_end_time : ", round(encode_end, 4))
        print("pub_time : ", round(pub_end, 4))
        print('pub_total_time : ', encode_end + pub_end)

        f = open('data_pub_' + str(loc) + '_' + 'qSize' + str(q) + '_rate' + str(rate2) + '.txt', 'a')
        f.write(str(count) + ',' + str(round(encode_end,4)) + ',' +str(round(pub_end,4)) + '\n')
        f.close()

        count += 1

        if count == 51:
            while True:
                pass

        rate.sleep()


if __name__ == '__main__':
    try:
        talker()

    except rospy.ROSInterruptException:
        pass