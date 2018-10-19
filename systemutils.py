#!/usr/bin/python
# encoding: utf-8

import socket
# import fcntl
# import struct
import os

#获取网卡ip地址
def get_ip_address(ifname):
  # s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
  # return socket.inet_ntoa(fcntl.ioctl(
  #   s.fileno(),
  #   0x8915, # SIOCGIFADDR
  #   struct.pack('256s', ifname[:15])
  # )[20:24])
  return  ''

#获取shell脚本执行结果列表
def get_text_sh(bash_sh):
    result = os.popen(bash_sh).read()
    return result.split("\n")

#获取shell脚本执行结果字符串
def get_text_sh_str(bash_sh):
    return ''.join(get_text_sh(bash_sh))

#获取机器host名称
def get_host_name():
    return  socket.getfqdn(socket.gethostname())

#获取配置文件参数值
def get_parameter_value(parameter):
    return get_text_sh_str("cat /etc/create_ap.conf |grep ^"+parameter+"|awk -F = '{printf $2}'")

#设置配置文件参数值
def set_parameter_value(parameter,value):
    return get_text_sh_str("sudo sed -i 's/^"+parameter+"=\([^,]*\)/"+parameter+"="+value+"/g' /etc/create_ap.conf")

#设置hosts的值
def set_hosts_value(value):
    return get_text_sh_str("sudo sed -i '1s/.*/"+value+" ap.itsmore.cn/' /home/pi/create_ap.hosts")

#获取ap客户端列表数据
def get_ap_client_list():
    return  get_text_sh("sudo create_ap --list-clients wlan0")

#重启设备
def system_reboot():
    return  get_text_sh_str("sudo reboot")
