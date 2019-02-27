#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright 2019 AtsushiSaito

import sys
import rospy
import rosbag
from PyQt5.QtWidgets import *
from geometry_msgs.msg import *


class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.init_dir = rospy.get_param("/init_dir")
        self.init()

    def readBagfile(self, name):
        self.bag = rosbag.Bag(self.fname[0])
        print("bag_name: [ %s ]" % self.fname[0])

        data = []
        for topic, msg, t in self.bag.read_messages(topics=[name]):
            data.append(msg)
        return data

    def init(self):
        self.fname = QFileDialog.getOpenFileName(
            self, "Open file", self.init_dir)

        data = self.readBagfile("/cmd_vel")
        ## ここから編集 ##

        print(data)

        ## ここまで編集 ##
        sys.exit()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = MainWindow()
    sys.exit(app.exec_())
