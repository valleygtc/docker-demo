FROM python:3.7
LABEL maintainer="gutianci@pwrd.com"

# 将文件复制到 image 中。
COPY . /docker-demo

# pip 安装程序依赖
WORKDIR /docker-demo
RUN python3 -m venv .venv
RUN . .venv/bin/activate && pip install --no-cache-dir -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

# 声明我们的程序运行需要的环境变量
ENV PORT=5000

EXPOSE 5000
CMD . .venv/bin/activate && python run.py