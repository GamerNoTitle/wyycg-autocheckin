# wyycg-autosignin

本脚本通过使用Github Action来进行[网易云游戏](https://cg.163.com/)签到操作，让你能够天天白嫖网易云游戏时长和云电脑！

喜欢就给我点个STAR吧！

## 使用方法

### 变量添加

1、Fork本仓库，按右上角的分支按钮（如图）

![](https://upimage.alexhchu.com/2020/11/22/e9b4bcf8e6a1d.png)

2、进入设置，设置变量`cookie`和`teleid` `teletoken`（这两个可选）

[如何获取变量内容？请点这里](#变量内容获取)

![](https://upimage.alexhchu.com/2020/11/22/988724b77ca62.png)

![](https://upimage.alexhchu.com/2020/11/22/a7958e9f5582f.png)

![](https://upimage.alexhchu.com/2020/11/22/7213627d41fc1.png)

### 测试脚本

**请在当天没有签到的情况下测试！！！**

我们先进入Action界面，启用Action

![](https://upimage.alexhchu.com/2020/11/22/70dd262ae54f0.png)

然后我们进入对应的脚本，启用脚本，并进行测试

![](https://upimage.alexhchu.com/2020/11/22/457403bb7d3bb.png)

**只要测试通过就是没问题，如果你配置了TELEGRAM还会收到你的BOT给你发送的消息**

测试通过后，你就可以放着它不用管了，它会自己运行的~

## 变量内容获取

### cookie获取

首先我们进入[官网](https://cg.163.com)，进行登录，然后用<kbd>F12</kbd>打开开发者工具后使用<kbd>Ctrl</kbd>+<kbd>F5</kbd>进行刷新，会刷出很多结果

我们在里面找到`@me`这一项，然后在右边找到`Authorization`将冒号后面的内容复制下来就是我们所需要的Cookie

![](https://upimage.alexhchu.com/2020/11/22/bfb0e2dbd347a.png)

### teleid获取

用你的Telegram找到@userinfobot，点个Start，会直接给你回复你的ID，复制下id后面的数字就是teleid了

![](https://upimage.alexhchu.com/2020/11/22/e4c50250626a6.png)

### teletoken获取

找@BotFather进行机器人的创建，按照提示创建即可，会给你一个API TOKEN，如果一不小心点过去了可以用命令`/mybots`管理自己的bot，找到自己想要使用的bot并获取API就可以了

![](https://upimage.alexhchu.com/2020/11/22/0428751a3925e.png)