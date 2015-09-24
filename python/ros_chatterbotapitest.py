from chatterbotapi import ChatterBotFactory, ChatterBotType

import roslib
import rospy
from std_msgs.msg import String


def callback(data):
    rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)
    s = session.think(data.data);
    pub.publish(String(s))

    
def listener():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # node are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('chat_bot', anonymous=True)

    rospy.Subscriber("speech", String, callback)
    rospy.Publisher('chat_bot/speech', String)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    factory = ChatterBotFactory()
    bot = factory.create(ChatterBotType.CLEVERBOT)
    session = bot.create_session()
    pub = rospy.Publisher('chat_bot/speech', String)
    listener()




#bot2 = factory.create(ChatterBotType.PANDORABOTS, 'b0dafd24ee35a477')
#bot2session = bot2.create_session()
