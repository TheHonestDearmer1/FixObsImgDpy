# 修复Obsidian img标签无法显示的工具

将<img>全部替换成“![]()”的形式解决掉<img>标签在Obs中需要绝对路径才能访问的问题。

安装FixObsImgDpy：

```
pip install FixObsImgDpy
```

安装完成后在需要修复的md文件的父目录下运行命令:

```
FixObsImgDpy
```

就会自动修复父目录以下的全部md文件
