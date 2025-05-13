# 使用说明

### 安装依赖包

```shell
#安装依赖包, 加入：--break-system-packages 突破限制管理
pip install   --break-system-packages -r  requirements.txt
```

### 启动

```shell
#执行，启动后默认端口为 8080
python run.py
```

`端口：8080`

### 访问 swagger

```shell
#浏览器输入一下地址，访问 swagger页面
http://127.0.0.1:8080/apidocs
```

### 守护进程

#### 安装 `supervisor`

```shell
apt-get install supervisor
```

#### 配置 `supervisor`

```
文件位置：/etc/supervisor/conf.d/
命名规则：app_name.conf


[program:app] ; 程序名称，在 supervisorctl 中通过这个值来对程序进行一系列的操作
autorestart=True      ; 程序异常退出后自动重启
autostart=True        ; 在 supervisord 启动的时候也自动启动
redirect_stderr=True  ; 把 stderr 重定向到 stdout，默认 false
environment=PATH="/home/app_env/bin"  ; 可以通过 environment 来添加需要的环境变量，一种常见的用法是使用指定的 virtualenv 环境
command=python server.py  ; 启动命令，与手动在命令行启动的命令是一样的
user=ubuntu           ; 用哪个用户启动
directory=/home/app/  ; 程序的启动目录
stdout_logfile_maxbytes = 20MB  ; stdout 日志文件大小，默认 50MB
stdout_logfile_backups = 20     ; stdout 日志文件备份数
; stdout 日志文件，需要注意当指定目录不存在时无法正常启动，所以需要手动创建目录（supervisord 会自动创建日志文件）
stdout_logfile = /data/logs/usercenter_stdout.log
```

#### `supervisor` 操作指令

```
supervisorctl 操作
supervisorctl 是 supervisord 的命令行客户端工具，使用的配置和 supervisord 一样，这里就不再说了。下面，主要介绍 supervisorctl 操作的常用命令：
输入命令 supervisorctl 进入 supervisorctl 的 shell 交互界面：

help # 查看帮助
status # 查看程序状态
stop program_name # 关闭 指定的程序
start program_name # 启动 指定的程序
restart program_name # 重启 指定的程序
tail -f program_name # 查看 该程序的日志
update # 重启配置文件修改过的程序（修改了配置，通过这个命令加载新的配置)

也可以直接通过 shell 命令操作：
supervisorctl status
supervisorctl update
```