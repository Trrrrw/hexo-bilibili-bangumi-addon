<<<<<<< Updated upstream
# hexo-bilibili-bangumi-addon
A python script for hexo-bilibili-bangumi  
自己的博客在用这个插件：[hexo-bilibili-bangumi](https://github.com/HCLonely/hexo-bilibili-bangumi)。但是用的bangumi源不能获取除标题和封面之外的信息。  
不会写Node.js，所以就写了个Python来补全番剧的信息。  
> 准备把每次获取到的数据存在本地，这样就不用每次都获取一样的数据了。
=======
# hexo-bilibili-bangumi-addon
A python script for hexo-bilibili-bangumi  
自己的博客在用这个插件：[hexo-bilibili-bangumi](https://github.com/HCLonely/hexo-bilibili-bangumi)。但是用的bangumi源不能获取除标题和封面之外的信息。  
不会写Node.js，所以就写了个Python来补全番剧的信息。  
22/10/22：随便写了点，现在运行之后会在`sourse/_data`下多出一个`bangumis-save.json`，这个文件内容和`bangumis.json`一样，每次更新的时候会先从这个文件里面找。如果想要重新从api获取的话把`bangumis-save.json`删掉就行了

# 使用
1. 给你的网站安装这个插件[hexo-bilibili-bangumi](https://github.com/HCLonely/hexo-bilibili-bangumi)，并根据其说明做好配置；
2. 在网页根目录运行一次`hexo bangumi -u`确保插件配置正常；
3. 安装[Python](https://www.python.org/)；
4. 安装`httpx`：`pip install httpx`；
5. 将`main.py`放到网页根目录，在终端中运行：`python main.py`
>>>>>>> Stashed changes
