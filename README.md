# Python-Homework-Open-Source-Project

![Homework-Open-Source.jpg](https://repository-images.githubusercontent.com/531410247/c87eee78-e33b-48c5-938d-33340f8415ce)

## 最新消息

### [2022.11.9] 完结撒花!!!

***

#### [1] 今后有关"Python程序设计"的所有作业都会在此开源.

#### [2] 任何人都能够随意的浏览和下载这里的代码.

#### [3] 任何人都可以创建新的分支并提交自己的代码.

#### [4] 让我们一起维护好开源生态吧!

#### ~~[本人从C++那里来的,接触Python没几天]~~

***

# MountPenglai

## 简介

&emsp;&emsp;MountPenglai 是一个 turtle 库功能增强包, 并且向下兼容 turtle 的所有函数, 意在改变 turtle 的绘图逻辑, 使之参数化. 当然我也增加了很多turtle本身内置函数无法实现的功能,
在参数化绘图、旋转、色彩变换上非常方便.

&emsp;&emsp;如果在学习 C/C++ 时使用过 EasyX Graphics Library 的话, 就会发现 MountPenglai 与 EasyX 非常相似, 没错 EasyX 可以帮助 C/C++ 初学者快速上手图形和游戏编程,
因此也比 turtle 更加适合 Python初学者(这里的初学者指的是正在受高等教育的人, 而不是九年义务教育), 因此我借鉴了 EasyX 的函数名与部分绘图逻辑, 就得到了 Python
这方便的开发平台和 EasyX 简单但适合计算机图形学的绘图功能. 同时这也使得 C/C++ 中使用 EasyX 编写的代码能够较轻松的移植进 Python.

> MountPenglai 0.0.3 - Powered by RMSHE

- [MountPenglai Pipy Link](https://pypi.org/project/MountPenglai/)
- [MountPenglai GitHub Link](https://github.com/RMSHE-MSH/MountPenglai)
- [EasyX Graphics Library](https://easyx.cn)
- [Python Turtle](https://docs.python.org/3/library/turtle.html)
- [PythonHomeworkOpenSourceProject](https://github.com/RMSHE-MSH/Python-Homework-Open-Source-Project)

***

## 目前支持的图形绘制函数

|    函数名称    | 函数名解释                       | 参数                                                                                               | 参数解释                                                                                                                                        |
| :------------: | :------------------------------- | :------------------------------------------------------------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------- |
|    teleport    | 将画笔传送到指定位置             | x, y                                                                                               | 点的坐标                                                                                                                                        |
|    putpixel    | 画点                             | x, y, radius=2                                                                                     | 点的坐标, 点的视觉半径(默认值为2)                                                                                                               |
|      line      | 画一条线段                       | x0, y0, x1, y1                                                                                     | 两点确定一条线段                                                                                                                                |
|    polyline    | 画连续的多条线段                 | POINTs=()                                                                                          | 控制点列表(x0, y0, x1, y1, x2, y2, ......)                                                                                                      |
|   rectangle    | 画无填充矩形                     | left, top, right, bottom, angle=0, xbase=Center, ybase=Center                                      | 矩形左上角顶点与右下角顶点的坐标, 旋转角度(默认为0), 旋转基点(默认为矩形几何中心)                                                               |
| solidrectangle | 画无边框的填充矩形               | 同上                                                                                               | 同上                                                                                                                                            |
| fillrectangle  | 画有边框的填充矩形               | 同上                                                                                               | 同上                                                                                                                                            |
|   roundrect    | 画无填充的圆角矩形               | 同上                                                                                               | 同上                                                                                                                                            |
| solidroundrect | 画无边框的填充圆角矩形           | 同上                                                                                               | 同上                                                                                                                                            |
| fillroundrect  | 画有边框的填充圆角矩形           | 同上                                                                                               | 同上                                                                                                                                            |
|    polygon     | 画无填充的规则多边形             | x, y, radius, steps=72, angle=0, xbase=Center, ybase=Center                                        | 指定外切圆圆心坐标, 指定外切圆半径, 指定多边形边数(默认为72-画圆), 图形旋转角度(默认为0), 旋转基点坐标(默认为多边形几何中心)                    |
|  solidpolygon  | 画无边框的规则填充多边形         | 同上                                                                                               | 同上                                                                                                                                            |
|  fillpolygon   | 画有边框的规则填充多边形         | 同上                                                                                               | 同上                                                                                                                                            |
|    ellipse     | 画无填充的椭圆                   | left, top, right, bottom, angle=0, xbase=Center, ybase=Center, stangle=0, endangle=360, steps=DECP | 椭圆外切矩形,旋转角度(默认为0),旋转基点(默认为几何中心),圆弧起始角角度(默认为0), 圆弧终止角角度(默认为360), 绘图计算精度(值越小越精细, 默认为1) |
|  solidellipse  | 画无边框的填充椭圆               | 同上                                                                                               | 同上                                                                                                                                            |
|  fillellipse   | 画有边框的填充椭圆               | 同上                                                                                               | 同上                                                                                                                                            |
|      arc       | 画椭圆弧                         | left, top, right, bottom, stangle=0, endangle=360                                                  | 扇形外切矩形, 扇形的起始角的角度(默认为0), 扇形的终止角的角度(默认为360)                                                                        |
|      pie       | 画无填充的扇形                   | left, top, right, bottom, stangle=0, endangle=360, angle=0, xbase=Center, ybase=Center             | 扇形外切矩形,扇形的起始角的角度(默认为0),扇形的终止角的角度(默认为360),旋转角度(默认为0),旋转基点(默认为外切矩形几何中心)                       |
|    solidpie    | 画无边框的填充扇形               | 同上                                                                                               | 同上                                                                                                                                            |
|    fillpie     | 画有边框的填充扇形               | 同上                                                                                               | 同上                                                                                                                                            |
|     Circle     | 画无填充的圆                     | x, y, radius                                                                                       | 圆心 x 坐标, 圆心 y 坐标, 圆的半径                                                                                                              |
|  solidcircle   | 画无边框的填充圆                 | 同上                                                                                               | 同上                                                                                                                                            |
|   fillcircle   | 画有边框的填充圆                 | 同上                                                                                               | 同上                                                                                                                                            |
|    getpixel    | 获取点的颜色(目前存在BUG)        | x, y                                                                                               | 点的坐标                                                                                                                                        |
|    drawtext    | 在指定区域内以指定格式输出字符串 | x, y, TextStr="", fontname="微软雅黑", fontsize=12, fonttype="normal", align="left"                | 指定输出坐标, 文本内容, 字体(默认微软雅黑), 字号(默认为12), 字形(默认为普通), 文本对齐方式(默认左对齐)                                          |
|   saveimage    | 将画布导出为矢量图               | fileName                                                                                           | 指定文件名                                                                                                                                      |

***

## 目前支持的色彩处理函数

&emsp;&emsp;色彩的表达有很多形式,目前主流有HEX, RGB, HSV, HSL, CMYK, HSI, CIE-LAB 这几种, 在MountPenglai中我们只使用 HEX, RGB, HSV 三种. 其中 HEX(
颜色的十六进制值) 为函数与函数间的通用色彩传参形式.

|       函数名称       | 函数名解释                        | 参数                                                                                       | 参数解释                                                                                                  | 返回值                                           |
| :------------------: | :-------------------------------- | :----------------------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------- | :----------------------------------------------- |
|         RGB          | RGB to HEX                        | R, G, B                                                                                    | 指定RGB颜色的三个通道(红, 绿, 蓝)的分量                                                                   | HEX字符串                                        |
|         HSV          | HSV to HEX                        | H, S, V                                                                                    | 指定HSV颜色的三个通道(色相, 饱和度, 明度)的分量                                                           | HEX字符串                                        |
|     GetRGBValue      | HEX to RGB                        | HEX                                                                                        | 指定颜色的十六进制值(例: "#5c2d91")                                                                       | RGB三分量元组                                    |
|      GetRValue       | 返回指定HEX颜色值中的红色分量     | HEX                                                                                        | 同上                                                                                                      | RGB的红色分量                                    |
|      GetGValue       | 返回指定HEX颜色值中的绿色分量     | HEX                                                                                        | 同上                                                                                                      | RGB的绿色分量                                    |
|      GetBValue       | 返回指定HEX颜色值中的蓝色分量     | HEX                                                                                        | 同上                                                                                                      | RGB的蓝色分量                                    |
|     GetHSVValue      | HEX to HSV                        | HEX                                                                                        | 同上                                                                                                      | HSV三分量元组                                    |
|      GetHValue       | 返回指定HEX颜色值中的色相分量     | HEX                                                                                        | 同上                                                                                                      | HSV的色相分量                                    |
|      GetSValue       | 返回指定HEX颜色值中的饱和度分量   | HEX                                                                                        | 同上                                                                                                      | HSV的饱和度分量                                  |
|      GetVValue       | 返回指定HEX颜色值中的明度分量     | HEX                                                                                        | 同上                                                                                                      | HSV的明度分量                                    |
|       HSVtoRGB       | HSV色彩空间转RGB色彩空间          | H, S, V                                                                                    | 指定HSV颜色的三个通道(色相, 饱和度, 明度)的分量                                                           | RGB三分量元组                                    |
|       RGBtoHSV       | RGB色彩空间转HSV色彩空间          | R, G, B                                                                                    | 指定RGB颜色的三个通道(红, 绿, 蓝)的分量                                                                   | HSV三分量元组                                    |
|      RGBtoGRAY       | 返回与指定RGB颜色对应的灰度值颜色 | R, G, B                                                                                    | 同上                                                                                                      | 灰度值                                           |
| RGBChannelExtraction | RGB色彩通道提取                   | ColorGroupHex=(), Channel="R", MIN=0, MAX=255, Fill=(0, 0, 0)                              | 像素组颜色的十六进制值列表, 提取通道[R, G, B], 提取范围[0, 255], 其余通道填充值                           | 返回被提取出来的像素组颜色的十六进制值列表       |
|    RGBChannelEdit    | RGB色彩通道编辑(值替换)           | ColorGroupHex=(), Channel="R", AlternateValue=None, MIN=0, MAX=255                         | 像素组颜色的十六进制值列表, 需要编辑的通道[R, G, B], 替换值[0, 255], 编辑范围[0, 255]                     | 返回对目标通道替换后的像素组颜色的十六进制值列表 |
|   RGBChannelDrift    | RGB色彩通道线性偏移               | ColorGroupHex=(), Channel="R", DriftValue=None, MIN=0, MAX=255                             | 像素组颜色的十六进制值列表, 需要编辑的通道[R, G, B], 偏移量, 编辑范围[0, 255]                             | 返回对目标通道偏移后的像素组颜色的十六进制值列表 |
| HSVChannelExtraction | HSV色彩通道提取                   | ColorGroupHex=(), Channel="H", MIN=0.0, MAX=360.0, Fill=(0.0, 1.0, 1.0)                    | 像素组颜色的十六进制值列表, 提取通道[H, S, V], 提取范围{ H:[0, 360], S:[0, 1], V:[0, 1] }, 其余通道填充值 | 返回被提取出来的像素组颜色的十六进制值列表       |
|    HSVChannelEdit    | HSV色彩通道编辑(值替换)           | ColorGroupHex=(), EditChannel="H", AlternateValue=0.0, BaseChannel="H", MIN=0.0, MAX=360.0 | 像素组颜色的十六进制值列表, 编辑通道[H/S/V], 替换值, 基通道[H/S/V], 基通道范围                            | 返回对目标通道替换后的像素组颜色的十六进制值列表 |
|   HSVChannelDrift    | HSV色彩通道偏移                   | ColorGroupHex=(), EditChannel="H", DriftValue=0.0, BaseChannel="H", MIN=0.0, MAX=360.0     | 像素组颜色的十六进制值列表, 编辑通道[H/S/V], 偏移量, 基通道[H/S/V], 基通道范围                            | 返回对目标通道偏移后的像素组颜色的十六进制值列表 |

***

## 绘图画布相关函数

|    函数名称    | 函数名解释                                                                                                               | 参数                                                                                               | 参数解释                                                                                                                                        |
| :------------: | :----------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------- |
|   initgraph    | 初始化型表观海龟灭绝处理器(初始化绘图窗口和画布)                                                                         | width, height, BGcolor="#282c34"                                                                   | 画布宽度, 画布高度, 画布颜色(默认#282c34)                                                                                                       |
| BeginBatchDraw | 开始批量绘图. 执行后, 任何绘图操作都将暂时不输出到绘图窗口上, 直到执行 FlushBatchDraw 或 EndBatchDraw 才将之前的绘图输出 | 无                                                                                                 | 无                                                                                                                                              |
| FlushBatchDraw | 执行未完成的绘制任务; 执行一次 TurtleScreen 刷新. 在禁用追踪时使用                                                       | 无                                                                                                 | 无                                                                                                                                              |
|  EndBatchDraw  | 结束批量绘制，并执行未完成的绘制任务                                                                                     | 无                                                                                                 | 无                                                                                                                                              |
| clearrectangle | 清空矩形区域                                                                                                             | left, top, right, bottom, angle=0, xbase=Center, ybase=Center                                      | 矩形左上角顶点与右下角顶点的坐标, 旋转角度(默认为0), 旋转基点(默认为矩形几何中心)                                                               |
| clearroundrect | 清空圆角矩形区域                                                                                                         | left, top, right, bottom, radius, angle=0, xbase=Center, ybase=Center                              | 矩形左上角顶点与右下角顶点的坐标, 圆角半径, 旋转角度(默认为0), 旋转基点(默认为矩形几何中心)                                                     |
|  clearcircle   | 清空圆形区域                                                                                                             | x, y, radius                                                                                       | 圆心坐标,圆的半径                                                                                                                               |
|  clearellipse  | 清空椭圆区域                                                                                                             | left, top, right, bottom, angle=0, xbase=Center, ybase=Center, stangle=0, endangle=360, steps=DECP | 椭圆外切矩形,旋转角度(默认为0),旋转基点(默认为几何中心),圆弧起始角角度(默认为0), 圆弧终止角角度(默认为360), 绘图计算精度(值越小越精细, 默认为1) |
|    clearpie    | 清空扇形区域                                                                                                             | left, top, right, bottom, stangle=0, endangle=360, angle=0, xbase=Center, ybase=Center             | 扇形外切矩形,扇形的起始角的角度(默认为0),扇形的终止角的角度(默认为360),旋转角度(默认为0),旋转基点(默认为外切矩形几何中心)                       |
|  clearpolygon  | 清空规则的多边形区域                                                                                                     | x, y, radius, steps=72, angle=0, xbase=Center, ybase=Center                                        | 指定外切圆圆心坐标, 指定外切圆半径, 指定多边形边数(默认为72-画圆), 图形旋转角度(默认为0), 旋转基点坐标(默认为多边形几何中心)                    |
|  clearcanvas   | 使用当前背景色清空(填充)画布                                                                                             | 无                                                                                                 | 无                                                                                                                                              |
| RotationMatrix | 指定点绕基点旋转                                                                                                         | x, y, xbase, ybase, angle                                                                          | 待旋转的点的坐标,基点坐标,旋转角度                                                                                                              |

***

## 示例效果图

![时钟.jpg](https://raw.githubusercontent.com/RMSHE-MSH/Python-Homework-Open-Source-Project/master/Coursework%20Diagram%20Tool%20-%20MountPenglai%20(%E5%A4%A7%E4%BD%9C%E4%B8%9A%E5%9B%BE%E5%BD%A2%E5%B7%A5%E5%85%B7%20-%20%E8%93%AC%E8%8E%B1%E5%B1%B1)/ExamplesEffect/%E6%97%B6%E9%92%9F.jpg)
![CircleLineLink.jpg](https://raw.githubusercontent.com/RMSHE-MSH/Python-Homework-Open-Source-Project/master/Coursework%20Diagram%20Tool%20-%20MountPenglai%20(%E5%A4%A7%E4%BD%9C%E4%B8%9A%E5%9B%BE%E5%BD%A2%E5%B7%A5%E5%85%B7%20-%20%E8%93%AC%E8%8E%B1%E5%B1%B1)/ExamplesEffect/CircleLineLink.jpg)

![Coursework1_Easy05(绘制漂亮的渐变螺旋).jpg](https://raw.githubusercontent.com/RMSHE-MSH/Python-Homework-Open-Source-Project/master/Coursework1_Easy%20(%E7%AE%80%E5%8D%95%E6%98%93%E6%87%82%E7%9A%84%E5%A4%A7%E4%BD%9C%E4%B8%9A%E6%A1%88%E4%BE%8B1)/Renderings(%E6%95%88%E6%9E%9C%E5%9B%BE)/Coursework1_Easy05(%E7%BB%98%E5%88%B6%E6%BC%82%E4%BA%AE%E7%9A%84%E6%B8%90%E5%8F%98%E8%9E%BA%E6%97%8B).jpg)
![Coursework1_Easy01(画椭圆的案例).jpg](https://raw.githubusercontent.com/RMSHE-MSH/Python-Homework-Open-Source-Project/master/Coursework1_Easy%20(%E7%AE%80%E5%8D%95%E6%98%93%E6%87%82%E7%9A%84%E5%A4%A7%E4%BD%9C%E4%B8%9A%E6%A1%88%E4%BE%8B1)/Renderings(%E6%95%88%E6%9E%9C%E5%9B%BE)/Coursework1_Easy01(%E7%94%BB%E6%A4%AD%E5%9C%86%E7%9A%84%E6%A1%88%E4%BE%8B).jpg)
![Coursework1_Easy04(画一束花).jpg](https://raw.githubusercontent.com/RMSHE-MSH/Python-Homework-Open-Source-Project/master/Coursework1_Easy%20(%E7%AE%80%E5%8D%95%E6%98%93%E6%87%82%E7%9A%84%E5%A4%A7%E4%BD%9C%E4%B8%9A%E6%A1%88%E4%BE%8B1)/Renderings(%E6%95%88%E6%9E%9C%E5%9B%BE)/Coursework1_Easy04(%E7%94%BB%E4%B8%80%E6%9D%9F%E8%8A%B1).jpg)
![Coursework1_Easy03(画心形图案)](https://raw.githubusercontent.com/RMSHE-MSH/Python-Homework-Open-Source-Project/master/Coursework1_Easy%20(%E7%AE%80%E5%8D%95%E6%98%93%E6%87%82%E7%9A%84%E5%A4%A7%E4%BD%9C%E4%B8%9A%E6%A1%88%E4%BE%8B1)/Renderings(%E6%95%88%E6%9E%9C%E5%9B%BE)/Coursework1_Easy03(%E7%94%BB%E5%BF%83%E5%BD%A2%E5%9B%BE%E6%A1%88).jpg)
![Coursework1_Easy02(画彩虹).jpg](https://raw.githubusercontent.com/RMSHE-MSH/Python-Homework-Open-Source-Project/master/Coursework1_Easy%20(%E7%AE%80%E5%8D%95%E6%98%93%E6%87%82%E7%9A%84%E5%A4%A7%E4%BD%9C%E4%B8%9A%E6%A1%88%E4%BE%8B1)/Renderings(%E6%95%88%E6%9E%9C%E5%9B%BE)/Coursework1_Easy02(%E7%94%BB%E5%BD%A9%E8%99%B9).jpg)
![Mandelbrot Set.jpg](https://raw.githubusercontent.com/RMSHE-MSH/Python-Homework-Open-Source-Project/master/Coursework%20Diagram%20Tool%20-%20MountPenglai%20(%E5%A4%A7%E4%BD%9C%E4%B8%9A%E5%9B%BE%E5%BD%A2%E5%B7%A5%E5%85%B7%20-%20%E8%93%AC%E8%8E%B1%E5%B1%B1)/ExamplesEffect/Mandelbrot%20Set.jpg)
![伪3D平面.jpg](https://raw.githubusercontent.com/RMSHE-MSH/Python-Homework-Open-Source-Project/master/Coursework%20Diagram%20Tool%20-%20MountPenglai%20(%E5%A4%A7%E4%BD%9C%E4%B8%9A%E5%9B%BE%E5%BD%A2%E5%B7%A5%E5%85%B7%20-%20%E8%93%AC%E8%8E%B1%E5%B1%B1)/ExamplesEffect/%E4%BC%AA3D%E5%B9%B3%E9%9D%A2.jpg)
***










