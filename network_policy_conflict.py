# -*- coding:utf-8 -*-
"""
    策略表示：
         []
"""
import socket
import struct


class Policy_Conflict_Detection(object):


    def __init__(self):
        self.confilct_policy_set = []

    """
         将String类型的IP地址转换为整数类型
        :param strIP:   192.168.142.21
        :return:    3232271893
    """
    def strIP_to_intIP(self,strIP):
        return struct.unpack('!I', socket.inet_aton(strIP))[0]

    """
        判断ip1是否包含ip2
        :param ip1: 
        :param ip1Mask:
        :param ip2:
        :param ip2Mask:
        :return: rue ip1包含ip2；False：ip1不包含ip2
    """
    def ipSupSet(self,ip1,ip1Mask,ip2,ip2Mask):

        ipOne = self.strIP_to_intIP(ip1)
        ipSec = self.strIP_to_intIP(ip2)
        flag = False
        if (ip1Mask > ip2Mask):
            flag =False
        if (((ipOne >>(32-ip1Mask))^(ipSec>>(32-ip1Mask))) == 0):
            flag = True
        return flag

    """
    将IP地址用二进制表示
    :param strIP: 192.168.64.0
    :return: 11000000 10101000 01000000 00000000
    """
    def convert(self,strIP):
        ip_list = strIP.split('.')
        lst = []
        for i in ip_list:
            two = bin(int(i,10)).lstrip("0b")
            lst.append(two.zfill(8))
        return " ".join(lst)

    def coflict(self,policy1,policy2):
        """
        判断两条策略是否冲突
        []
        :param policy1:
        :param policy2:
        :return: True:冲突；False:不冲突
        """
        print("Determine if two strategies configct:")
        if (self.supset(policy1,policy2)):
            pass

        elif (self.subset(policy1,policy2)):
            pass

        elif (self.redundanz(policy1,policy2)):
            pass



    def supset(self,policy1,policy2):
        pass

    def subset(self,policy1,policy2):
        pass



    def redundanz(self,policy1,policy2):
        """
        判断两条策略之间是否存在冗余
        :param policy1:
        :param policy2:
        :return:
        """
        pass


class Policy_Conflict_Resolve(object):
    def __init__(self):
        pass


























