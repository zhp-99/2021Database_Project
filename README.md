# 这是整个项目的运行教程：

首先请安装django和vue，具体怎么安装自己上网找教程。

然后进入PkuWenWenbackend文件夹运行命令：python manage.py runserver

再进入pkuwenwenfrontend文件夹，先运行命令yarn install，这会自动安装依赖包，安装成功后运行命令yarn serve

然后整个项目就运行起来了，前端运行在localhost:8080，后端运行在localhost:8000.


# 这是本项目的开发规范
本项目在以下这些约束下进行开发：
* 每一个页面只能有一个mounted函数用来加载本页面需要的数据
* 这也就意味着后端的每一个url挂接的函数要满足对应的前端页面的所有需求
* 每一个页面可以有多个按钮，但是每一个按钮只能发送一次http请求并接受一次对应的答复

基于上面这些约束后端采用以下文件结构:
* url.py, 进行view函数与url的绑定，前端需求先行，后端来满足
* view.py, 用来和前端对接的函数写在这里，返回值一律写成JsonResponse（尽可能用function.py 里面定义的功能进行组合，不要重复造轮子）
* function.py：这里面是各种轮子，返回值一律做成dict形式
