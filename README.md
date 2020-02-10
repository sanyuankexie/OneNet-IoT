# OneNet-IoT
**Note:** 基于OneNet平台okHttp协议的远程环境监控App开发

 OneNET平台作为连接和数据的中心，能适应各种传感网络和通信网络，将面向智能家居、可穿戴设备、车联网、移动健康、智能创客等多个领域开放。 

借助OneNet平台，我们可以快速开发IoT环境，多协议接入提供了多种网络通信方式，这为IoT开发者提供了便利。

OneNet平台提供http协议，创建产品后，可以通过api接口上传数据，可在平台上的数据流显示需要显示的数据。通过api接口可以上传数据，也可以访问数据，官方也提供了详细的api技术文档，开发者可以自行查看。

## 项目介绍

本项目为基于onenet平台http协议的监控APP开发，硬件端采用的是python语言编写的模拟上传数据demo，当然在树莓派下可以运行，若是arduino、stm32或者esp8266单片机，需要重新设计代码。

<img src="C:\Users\yDarkin\AppData\Roaming\Typora\typora-user-images\image-20200210225012517.png" alt="image-20200210225012517"  />

客户端则是Android App开发，通过okhttp协议+json数据的方式，实现手机端显示环境数据。效果如下图：

<img src="C:\Users\yDarkin\Desktop\Screenshot_1581346119.png" alt="Screenshot_1581346119" style="zoom:50%;" />

