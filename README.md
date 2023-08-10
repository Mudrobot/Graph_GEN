# 自动生成给定经纬度区间的路网图

将想要查询的路网经纬度信息写在query.json中。

5个参数分别代表：

`name`:社区名字

`lon`: 社区左上角的经度

`lat`: 社区左上角的维度

`lon_delta`: 右下角和左上角经度上的差异

`lat_delta`: 右下角和左上角纬度上的差异

参照例子填写完毕后就可以直接运行main.py了，最后会生成当前区域的一个街区图默认保存在img.json中。

其中中间会产生way，node两种类型的参数可以保存进入geopandas dataframe中去，但是polygon目前确实不知道该如何进行生成。**这也是目前最大的挑战！**

---

还有一种方法见`test.ipynb`文件，但是该方法感觉没有先前的方法灵活。