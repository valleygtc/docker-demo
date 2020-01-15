# 简介
使用 Docker 容器化 Flask Web App 的演示程序。


# 手动部署
```bash
$ git clone <repo>
$ cd docker-demo

$ python -m venv .venv
$ source .venv/bin/activate
$ pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple # 清华pypi镜像。

$ python run.py
```


# Docker
```bash
# build image
$ docker image build --tag=docker-demo:1 .

# run
$ docker run -p 5000:5000 -d docker-demo
```


# 依赖包：
- Flask框架
- Server：waitress


# api
## url
```
Endpoint      Methods  Rule
------------  -------  -----------------------
handle_hello  GET      /
static        GET      /static/<path:filename>
```

## request格式：
见app/views.py中各视图函数的docstring。


# 开发说明：
- flask debug server: `$ flask run [--host=0.0.0.0]`
- unittest: `python -m unittest test.py`
