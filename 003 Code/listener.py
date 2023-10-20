import rospy
import base64
import cv2
from cv_bridge import CvBridge
from time import time
from std_msgs.msg import String
from sensor_msgs.msg import Image

q = 20

def callback(data):
    loc = 3
    rate =2

    cnt, data, arrival_time = str(data.data).split(',')
    data_arrival_time = time() - float(arrival_time)

    if cnt == '1':
        f2 = open('data_sub_' + str(loc) + '_' + 'qSize' + str(q) + '_' + 'rate' + str(rate) + '.txt', 'a')
        f2.write('\n' + 'loc : ' + str(loc) + ',qSize : ' + str(q) + ',' + 'rate : ' + str(rate) + '\n')
        f2.close()

    decode_start = time()
    f = open('image_5.jpg', 'wb')
    f.write(base64.b64decode(data))
    f.close()
    decode_end = time() - decode_start

    rospy.loginfo(cnt + ' : image save!!')

    print(cnt)
    print('decode_time : ', round(decode_end,4))
    print('data_arrival_time : ', round(data_arrival_time,4))


    f2 = open('data_sub_' + str(loc) + '_' + 'qSize' + str(q) + '_rate' + str(rate) + '.txt', 'a')
    f2.write(str(cnt) + ',' + str(round(decode_end,4)) + ',' + str(round(data_arrival_time,4)) + '\n')
    f2.close()


def listener():

    rospy.init_node('listener', anonymous=True)

    rospy.Subscriber('image/text', String, callback, queue_size=q)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':

    listener()