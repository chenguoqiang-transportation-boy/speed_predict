# speed_predict
# 基于高德地图API，开发了一个能自动爬取、处理、分析、预测车速数据的软件，用的python编程语言，pyqt5

# 不足之处：
因为懒，有两部分代码没添加进去，大概如下：
  1.数据清洗部分
import pandas as pd
inputfile='D:\成都绕城高速.csv'
data = pd.read_csv(inputfile)
time=data[u'时间'].count()
speed=data[u'车速'].count()
rate_nan=1 - (speed/time)
print(‘时间总数为:’,time)
print(‘车速数据总数为:’,speed)
print(‘空值占比为:’,rate_nan)
if rate_nan > 0.2:
    print('车速数据空值占比超过20％，应该放弃该条路段的研究')
else:
print('车速数据空值未占比超过20％，本路段可研究')
  
  2.数据填充部分
import pandas as pd
inputfile='D:\成都绕城高速.csv'
data = pd.read_csv(inputfile)
data['车速'] = data['车速'].fillna(method='ffill')
data.to_csv('D:\成都绕城高速.csv',mode='w',encoding='utf-8-sig')

# 结果：
![image](https://github.com/chenguoqiang-transportation-boy/speed_predict/blob/master/images_demo/image1.jpg)
![image](https://github.com/chenguoqiang-transportation-boy/speed_predict/blob/master/images_demo/image2.jpg)
![image](https://github.com/chenguoqiang-transportation-boy/speed_predict/blob/master/images_demo/image3.jpg)
![image](https://github.com/chenguoqiang-transportation-boy/speed_predict/blob/master/images_demo/image4.jpg)
