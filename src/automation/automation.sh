#!/bin/bash

# Tip_001 字符串处理：
  # 判断当前主机的CPU生产商，其信息在/proc/cpuinfo文件中vendor id一行中。
  # 如果其生产商为AuthenticAMD，就显示其为AMD公司；
  # 如果其生产商为GenuineIntel，就显示其为Intel公司；
  # 否则，就说其为非主流公司；

mycpu=`cat /proc/cpuinfo | grep vendor | awk '{print $3}' | head -1 | sed 's/^\s*//g' | sed 's/\s*$//g'`
if [ "x${mycpu}" = "xGenuineIntel" ]; then
  echo "INTEL chip inside"
elif [ "x${mycpu}" = "xAuthenticAMD" ]; then
  echo "AMD chip inside"
else
  echo "unkown cpu type: ${mycpu}"
fi

# Tip_002 流程控制
  # 设定变量FILE的值为/etc/passwd
  # 依次向/etc/passwd中的每个用户问好，并显示对方的shell
  # 形如：Hello, root, your shell: /bin/bash
  # 扩展：只向默认shell为bash的用户问好
  # 统计一共有多少个用户

SUM=0
FILE=/etc/passwd
LINES=`wc -l /etc/passwd| cut -d' ' -f1`
for I in `seq 1 $LINES`;do
  USER=`cat /etc/passwd | head -n $I | tail -1 | cut -d: -f1 `
  USHELL=`cat /etc/passwd| head -n $I | tail -1 | cut -d: -f7`
  # if $USHELL is null, then you will get error with the sinlge[]
  # so please use double[[]] when judge the string equation
  if [[ $USHELL == '/bin/bash' ]]; then
  echo "Hello, $USER , Your shell is $USHELL"
  SUM=$[$SUM+1]
  fi
done
echo "Total user is $SUM"

# Tip_003 数值计算
  # 计算100以内所有能被3整除的正整数的和

SUM=0
for I in `seq 1 100`;do
  if [ $[$I%3] = 0 ];then
    SUM=$[$SUM+$I]
  fi
done
echo "The sum is $SUM"
