#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json,urllib
import IPy
def ip2addr(ip):
	iip = IPy.IP(ip)
	if iip.iptype() != 'PUBLIC':
		return ip
	try:
		url='http://ip.taobao.com/service/getIpInfo.php?ip='+ip
		ip_info = json.loads(urllib.urlopen(url).read())
		return ('%s%s%s%s%s %s'%(ip_info['data']['country'],
			ip_info['data']['area'],
			ip_info['data']['region'],
			ip_info['data']['city'],
			ip_info['data']['county'],
			ip_info['data']['isp']))
	except:
		return ip
