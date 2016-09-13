本项目是使用PyOpenGL编写的3D魔方游戏（制作人：Mr.Ye）
1. 环境搭建
（1）Windows
    a)下载python
	URL：https://www.python.org/downloads/windows/
	点击安装
    b)下载pyopengl
	URL：https://pypi.python.org/pypi/PyOpenGL
	点击安装
    c)下载pyopengl-accelerate
	URL：https://pypi.python.org/pypi/PyOpenGL-accelerate
	点击安装
    d)下载pyglut
	URL：https://github.com/mrcyberfighter/pyglut/
	进入freeGLUT根目录，调用python setup.py install安装
    e)下载freeGLUT
	URL：http://www.transmissionzero.co.uk/software/freeglut-devel/
	解压压缩包，将freeglut\bin下的freeglut.dll放到编写的python脚本同级目录下即可
（2）Ubuntu
    a) sudo apt-get install pyopengl
2.程序框架
程序采用面向对象的思想编写
（1）类
    a)Cube类
	此类为魔方中的小正方体的类
    b)MagicCube类
	此类为魔方的类，包含27个Cube类
（2）Cube类的属性和方法
    a)属性：坐标位置，每个面的贴图
（3）MagicCube类的属性和方法