# Holosimulation 测试说明

## 1.安装holoocean链接：

[Installation — HoloOcean 0.5.0 documentation](https://holoocean.readthedocs.io/en/master/usage/installation.html)

## 2.UE4的源代码链接：

[Getting Started — HoloOcean 0.5.0 documentation](https://holoocean.readthedocs.io/en/master/develop/start.html)

按照链接clone下来UE4的开发的源代码，然后用`UE4.27`打开，然后开发，把导出的包放到holoocean的安装路径中

## 3.从链接

[https://github.com/hwgao1101/Holosimulation](https://github.com/hwgao1101/Holosimulation)

中把测试代码下载下来

代码结构：

- 其中 `myTankSimulator.py` 用来测试`myTank-HoveringImagingSonar.json`文件是否成功

`Test`文件夹下面的`manulControl.py`文件用来测试`myTank-Hovering.json`是否成功

- 其中`OpenWaterSimulator.py`和`SimpleUnderwaterSimulator.py`是测试下载包的代码，应该都是能正常运行的
