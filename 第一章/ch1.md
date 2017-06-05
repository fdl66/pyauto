第一章 系统基础信息模块详解
=========================
## 系统性能信息模块`psutil`

实例：https://github.com/giampaolo/psutil

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
>>> psutil.virtual_memory()
svmem(total=10367352832, available=6472179712, percent=37.6, used=8186245120, free=2181107712, active=4748992512, inactive=2758115328, buffers=790724608, cached=3500347392, shared=787554304)
>>> psutil.swap_memory()
sswap(total=2097147904, used=296128512, free=1801019392, percent=14.1, sin=304193536, sout=677842944)
>>>

```


3. 磁盘信息

4. 网络信息

5. 其他系统信息



## 实用的IP地址处理模块`IPy`


## DNS处理模块`dnspython`

