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
    swap：狡猾分区使用数
    
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

