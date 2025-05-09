from flask import Flask

from src.ctrl.openapi_ctrl import openapi

# 声明 flask 实例
app = Flask(__name__)
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
# 注册 openapi 控制机器
app.register_blueprint(openapi)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
