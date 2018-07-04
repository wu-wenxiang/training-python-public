## 01-CType
- 编写一个新的C程序：01-CType / add.c
- 编译
	
		#For Linux
		$  gcc -shared -Wl,-soname,adder -o adder.so -fPIC add.c
			
		#For Mac
		$ gcc -shared -Wl,-install_name,adder.so -o adder.so -fPIC add.c
- 用Python调用：01-CType / add.py
- 输出
	
		Sum of 4 and 5 = 9
		Sum of 5.5 and 4.1 =  9.600000381469727

## 02-CModule
- 编译

		python setup.py build_ext --inplace
- import模块

		$ python
		>>> import sample
		>>> sample.add_float(2.3, 2.4)
		4.699999999999999

## 03-CModule-CType
- 先编译C-Type

		gcc -shared -Wl,-install_name,libsample.so -o libsample.so -fPIC sample.c
- 调用：sample.py

		$ python
		>>> import sample
		>>> sample.gcd(35,42)
		7
		>>> sample.in_mandel(0,0,500)
		1
		>>> sample.in_mandel(2.0,1.0,500)
		0
		>>> sample.divide(42,8)
		(5, 2)
		>>> sample.avg([1,2,3])
		2.0
		>>> p1 = sample.Point(1,2)
		>>> p2 = sample.Point(4,5)
		>>> sample.distance(p1,p2)
		4.242640687119285
		
		>>> from ctypes.util import find_library
		>>> find_library('m')
		'/usr/lib/libm.dylib'
		>>> find_library('pthread')
		'/usr/lib/libpthread.dylib'
		>>> find_library('sample')
		'/usr/local/lib/libsample.so'
		>>>
- Build CModule

		python buildlib.py build_ext --inplace
- 调用，可以先把sample.py重命名称sample2.py，避免和新编译出的so文件冲突
