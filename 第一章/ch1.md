第一章 系统基础信息模块详解
=========================
## 系统性能信息模块`psutil`

实例：https://github.com/giampaolo/psutil

文档：https://pythonhosted.org/psutil/#recipes/

### shell中常用监控命令
ps:
top:
lsof:
netstat:
ifconfig:
who:
df:
kill:
free:
nice:
ionice:
iostat:
iotop:
uptime:
pidof:
tty:
taskset:
pmap:

<!--more-->
### 获取系统性能信息
1. CPU信息
```python 
>>> import psutil
>>> psutil.cpu_times()
scputimes(user=3961.46, nice=169.729, system=2150.659, idle=16900.540, iowait=629.59, irq=0.0, softirq=19.42, steal=0.0, guest=0, nice=0.0)
>>>
>>> for x in range(3):
...     psutil.cpu_percent(interval=1)
...
4.0
5.9
3.8
>>>
>>> for x in range(3):
...     psutil.cpu_percent(interval=1, percpu=True)
...
[4.0, 6.9, 3.7, 9.2]
[7.0, 8.5, 2.4, 2.1]
[1.2, 9.0, 9.9, 7.2]
>>>
>>> for x in range(3):
...     psutil.cpu_times_percent(interval=1, percpu=False)
...
scputimes(user=1.5, nice=0.0, system=0.5, idle=96.5, iowait=1.5, irq=0.0, softirq=0.0, steal=0.0, guest=0.0, guest_nice=0.0)
scputimes(user=1.0, nice=0.0, system=0.0, idle=99.0, iowait=0.0, irq=0.0, softirq=0.0, steal=0.0, guest=0.0, guest_nice=0.0)
scputimes(user=2.0, nice=0.0, system=0.0, idle=98.0, iowait=0.0, irq=0.0, softirq=0.0, steal=0.0, guest=0.0, guest_nice=0.0)
>>>
>>> psutil.cpu_count()
4
>>> psutil.cpu_count(logical=False)
2
>>>
>>> psutil.cpu_stats()
scpustats(ctx_switches=20455687, interrupts=6598984, soft_interrupts=2134212, syscalls=0)
>>>
>>> psutil.cpu_freq()
scpufreq(current=931.42925, min=800.0, max=3500.0)
>>>

```
tip:

    irq:硬件中断
    softirq：软件中断
2. 内存信息
```python
>>> import psutil
>>> psutil.virtual_memory() #内存完整信息
svmem(total=10367352832, available=6472179712, percent=37.6, used=8186245120, free=2181107712, active=4748992512, inactive=2758115328, buffers=790724608, cached=3500347392, shared=787554304)
>>> psutil.swap_memory() #获取交换分区信息
sswap(total=2097147904, used=296128512, free=1801019392, percent=14.1, sin=304193536, sout=677842944)
>>>

```
tip:

    total:内存总数
    used：已经使用的内存数
    free：空闲内存数
    buffers：缓冲使用数
    cache：缓冲使用数
    swap：交换分区使用数
    
[free命令中cached和buffers的区别](http://www.cnblogs.com/chenpingzhao/p/5161844.html)

3. 磁盘信息
```python
>>> import psutil
>>> psutil.disk_partitions()
[sdiskpart(device='/dev/sda1', mountpoint='/', fstype='ext4', opts='rw,nosuid'),
 sdiskpart(device='/dev/sda2', mountpoint='/home', fstype='ext, opts='rw')]
>>>
>>> psutil.disk_usage('/')
sdiskusage(total=21378641920, used=4809781248, free=15482871808, percent=22.5)
>>>
>>> psutil.disk_io_counters(perdisk=False)
sdiskio(read_count=719566, write_count=1082197, read_bytes=18626220032, write_bytes=24081764352, read_time=5023392, write_time=63199568, read_merged_count=619166, write_merged_count=812396, busy_time=4523412)
>>>
```

4. 网络信息
```python
>>> import psutil
>>> psutil.net_io_counters(pernic=True)
{'eth0': netio(bytes_sent=485291293, bytes_recv=6004858642, packets_sent=3251564, packets_recv=4787798, errin=0, errout=0, dropin=0, dropout=0),
 'lo': netio(bytes_sent=2838627, bytes_recv=2838627, packets_sent=30567, packets_recv=30567, errin=0, errout=0, dropin=0, dropout=0)}
>>>
>>> psutil.net_connections()
[pconn(fd=115, family=<AddressFamily.AF_INET: 2>, type=<SocketType.SOCK_STREAM: 1>, laddr=('10.0.0.1', 48776), raddr=('93.186.135.91', 80), status='ESTABLISHED', pid=1254),
 pconn(fd=117, family=<AddressFamily.AF_INET: 2>, type=<SocketType.SOCK_STREAM: 1>, laddr=('10.0.0.1', 43761), raddr=('72.14.234.100', 80), status='CLOSING', pid=2987),
 pconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=<SocketType.SOCK_STREAM: 1>, laddr=('10.0.0.1', 60759), raddr=('72.14.234.104', 80), status='ESTABLISHED', pid=None),
 pconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=<SocketType.SOCK_STREAM: 1>, laddr=('10.0.0.1', 51314), raddr=('72.14.234.83', 443), status='SYN_SENT', pid=None)
 ...]
>>>
>>> psutil.net_if_addrs()
{'lo': [snic(family=<AddressFamily.AF_INET: 2>, address='127.0.0.1', netmask='255.0.0.0', broadcast='127.0.0.1', ptp=None),
        snic(family=<AddressFamily.AF_INET6: 10>, address='::1', netmask='ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff', broadcast=None, ptp=None),
        snic(family=<AddressFamily.AF_LINK: 17>, address='00:00:00:00:00:00', netmask=None, broadcast='00:00:00:00:00:00', ptp=None)],
 'wlan0': [snic(family=<AddressFamily.AF_INET: 2>, address='192.168.1.3', netmask='255.255.255.0', broadcast='192.168.1.255', ptp=None),
           snic(family=<AddressFamily.AF_INET6: 10>, address='fe80::c685:8ff:fe45:641%wlan0', netmask='ffff:ffff:ffff:ffff::', broadcast=None, ptp=None),
           snic(family=<AddressFamily.AF_LINK: 17>, address='c4:85:08:45:06:41', netmask=None, broadcast='ff:ff:ff:ff:ff:ff', ptp=None)]}
>>>
>>> psutil.net_if_stats()
{'eth0': snicstats(isup=True, duplex=<NicDuplex.NIC_DUPLEX_FULL: 2>, speed=100, mtu=1500),
 'lo': snicstats(isup=True, duplex=<NicDuplex.NIC_DUPLEX_UNKNOWN: 0>, speed=0, mtu=65536)}
>>>
```
5. 其他系统信息
```python
>>> import psutil
>>> psutil.users()
[suser(name='giampaolo', terminal='pts/2', host='localhost', started=1340737536.0, pid=1352),
 suser(name='giampaolo', terminal='pts/3', host='localhost', started=1340737792.0, pid=1788)]
>>>
>>> psutil.boot_time()
1365519115.0
>>>
```

### 系统进程管理方法
1. 进程信息
插入一条关于进程控制信号捕获的博客，常考笔试题（sigkill和sigstop不可被捕捉，sigint可以被捕捉）：http://blog.csdn.net/madpointer/article/details/13091705

2. popen类的使用

```python
>>> import psutil
>>> from subprocess import PIPE
>>> p = psutil.Popen(["/usr/bin/python", "-c", "print('hello')"], stdout=PIPE)
>>> p.name()
'python'
>>> p.username()
'giampaolo'
>>> p.communicate()
('hello\n', None)
>>> p.wait(timeout=2)
0
>>>
```


## 实用的IP地址处理模块`IPy`
```python
#!/usr/bin/env python

from IPy import IP

ip_s = raw_input('Please input an IP or net-range: ')
ips = IP(ip_s)


if len(ips) > 1:
    print('net: %s' % ips.net()) #输出网络地址
    print('netmask: %s' % ips.netmask()) #输出网络掩码地址
    print('broadcast: %s' % ips.broadcast())  #输出广播地址
    print('reverse address: %s' % ips.reverseNames()[0])  #输出地址反向解析
    print('subnet: %s' % len(ips)) #输出网络子网数
else:
    print('reverse address: %s' % ips.reverseNames()[0])

print('hexadecimal: %s' % ips.strHex()) #十六进制地址
print('binary ip: %s' % ips.strBin()) #二进制地址
print('iptype: %s' % ips.iptype()) #地址类型

```

## DNS处理模块`dnspython`
插播新知识：[dig命令](http://roclinux.cn/?p=2449)

### 模块域名解析方法详解 
#### 常见的DNS解析类型
A记录： 将域名指向一个IPv4地址（例如：100.100.100.100），需要增加A记录

CNAME记录： 如果将域名指向一个域名，实现与被指向域名相同的访问效果，需要增加CNAME记录。这个域名一般是主机服务商提供的一个域名

MX记录： 建立电子邮箱服务，将指向邮件服务器地址，需要设置MX记录。建立邮箱时，一般会根据邮箱服务商提供的MX记录填写此记录

NS记录： 域名解析服务器记录，如果要将子域名指定某个域名服务器来解析，需要设置NS记录

TXT记录： 可任意填写，可为空。一般做一些验证记录时会使用此项，如：做SPF（反垃圾邮件）记录

AAAA记录： 将主机名（或域名）指向一个IPv6地址（例如：ff03:0:0:0:0:0:0:c1），需要添加AAAA记录

SRV记录： 添加服务记录服务器服务记录时会添加此项，SRV记录了哪台计算机提供了哪个服务。格式为：服务的名字.协议的类型（例如：_example-server._tcp）。

SOA记录： SOA叫做起始授权机构记录，NS用于标识多台域名解析服务器，SOA记录用于在众多NS记录中那一台是主服务器

PTR记录： PTR记录是A记录的逆向记录，又称做IP反查记录或指针记录，负责将IP反向解析为域名

显性URL转发记录： 将域名指向一个http(s)协议地址，访问域名时，自动跳转至目标地址。例如：将www.liuht.cn显性转发到www.itbilu.com后，访问www.liuht.cn时，地址栏显示的地址为：www.itbilu.com。

隐性UR转发记录L： 将域名指向一个http(s)协议地址，访问域名时，自动跳转至目标地址，隐性转发会隐藏真实的目标地址。例如：将www.liuht.cn显性转发到www.itbilu.com后，访问www.liuht.cn时，地址栏显示的地址仍然是：www.liuht.cn。


2. DNS解析中一些问题

2.1 A记录与CNAME记录

A记录是把一个域名解析到一个IP地址，而CNAME记录是把域名解析到另外一个域名，而这个域名最终会指向一个A记录，在功能实现在上A记录与CNAME记录没有区别。

CNAME记录在做IP地址变更时要比A记录方便。CNAME记录允许将多个名字映射到同一台计算机，当有多个域名需要指向同一服务器IP，此时可以将一个域名做A记录指向服务器IP，然后将其他的域名做别名(即：CNAME)到A记录的域名上。当服务器IP地址变更时，只需要更改A记录的那个域名到新IP上，其它做别名的域名会自动更改到新的IP地址上，而不必对每个域名做更改。


2.2 A记录与AAAA记录

二者都是指向一个IP地址，但对应的IP版本不同。A记录指向IPv4地址，AAAA记录指向IPv6地址。AAAA记录是A记录的升级版本。


2.3 IPv4与IPv6

IPv4，是互联网协议（Internet Protocol，IP）的第四版，也是第一个被广泛使用的版本，是构成现今互联网技术的基础协议。IPv4 的下一个版本就是IPv6，在将来将取代目前被广泛使用的IPv4。

IPv4中规定IP地址长度为32位（按TCP/IP参考模型划分) ，即有2^32-1个地址。IPv6的提出最早是为了解决，随着互联网的迅速发展IPv4地址空间将被耗尽的问题。为了扩大地址空间，IPv6将IP地址的长度由32位增加到了128位。在IPv6的设计过程中除了一劳永逸地解决了地址短缺问题以外，还解决了IPv4中的其它问题，如：端到端IP连接、服务质量（QoS）、安全性、多播、移动性、即插即用等。


2.4 TTL值

TTL－生存时间（Time To Live），表示解析记录在DNS服务器中的缓存时间，TTL的时间长度单位是秒，一般为3600秒。比如：在访问www.itbilu.com时，如果在DNS服务器的缓存中没有该记录，就会向某个NS服务器发出请求，获得该记录后，该记录会在DNS服务器上保存TTL的时间长度，在TTL有效期内访问www.itbilu.com，DNS服务器会直接缓存中返回刚才的记录。

### DNS轮询（不完善）
```python
#!/usr/bin/python
#coding:utf-8

import dns.resolver
import os
import httplib

iplist=[]    #定义域名IP列表变量
appdomain="fdl66.github.io"    #定义业务域名

def get_iplist(domain=""):    #域名解析函数，解析成功IP将追加到iplist
    try:
        cname = dns.resolver.query(domain, 'CNAME')
        domains = []
        for i in cname.response.answer:
            for j in i.items:
                print j.to_text()+"debug"
                domains.append(j)
        for dom in domains:
            A=dns.resolver.query(str(dom),'A')  # 解析A记录类型
            for i in A.response.answer:
                for j in i.items:
                    print j.address+"debug"
                    iplist.append(j.address)  # 追加到iplist
    except Exception,e:
        print "dns resolver error:"+str(e)
        return
    return True

def checkip(ip):
    checkurl=ip+":80"
    getcontent=""
    httplib.socket.setdefaulttimeout(5)    #定义http连接超时时间(5秒)
    conn=httplib.HTTPConnection(checkurl)    #创建http连接对象

    try:
        conn.request("GET", "/",headers = {"Host": appdomain})  #发起URL请求，添加host主机头
        r=conn.getresponse()
        getcontent =r.read(15)   #获取URL页面前15个字符，以便做可用性校验
    finally:
        print getcontent+"debug"
        if getcontent=="<!doctype html>":  #监控URL页的内容一般是事先定义好，比如“HTTP200”等
            print ip+" [OK]"
        else:
            print ip+" [Error]"    #此处可放告警程序，可以是邮件、短信通知

if __name__=="__main__":
    if get_iplist(appdomain) and len(iplist)>0:    #条件：域名解析正确且至少要返回一个IP
        for ip in iplist:
            checkip(ip)
    else:
        print "dns resolver error."

```
