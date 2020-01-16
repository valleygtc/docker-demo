# 简介
使用 Docker 容器化 Flask Web App 的演示程序。


# 手动部署
```bash
$ git clone <repo>
$ cd docker-demo

$ python -m venv .venv
$ source .venv/bin/activate
$ pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple # 清华pypi镜像。

$ touch env.sh # 并在文件中填写好程序所需环境变量，参考文件：env.sh.example。
$ source env.sh # 读入环境变量。

$ flask create_tables # 创建数据库表。

$ python run.py
```

# Docker
## 构建镜像：
```bash
$ docker image build --tag=docker-demo:3 .
```

## 运行：
首先，将程序运行需要的环境变量写入 `docker.env` 文件，内容可参考：`docker.env.example`。

然后使用以下命令运行容器：
```bash
$ docker run \
  --name='docker-demo' \
  --network=host \
  --env-file='docker.env' \
  -v "$PWD/log":/docker-demo/log \
  -d docker-demo:3
```


# 依赖：
- Flask框架
- DB：
  - ORM: Flask-SQLAlchemy
  - MySQL + mysql-connector-python
- 部署： waitress


# api
## url
```
Endpoint                      Methods  Rule
----------------------------  -------  -----------------------
bp_main.hanlde_add_student    GET      /student/add
bp_main.hanlde_hello          GET      /
bp_main.hanlde_show_students  GET      /student/
static                        GET      /static/<path:filename>
```

## request格式：
见app/views.py中各视图函数的docstring。


# 开发说明：
- flask debug server: `$ flask run [--host=0.0.0.0]`
- unittest: `python -m unittest test.py`
