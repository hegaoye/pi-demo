from flasgger import Swagger
from flask import Flask
from flask_restful import Api

from src.resource.button_resource import ButtonResource
from src.resource.relay_resource import RelayResource
from src.resource.servo_resource import ServoResource

# 声明 flask 实例
app = Flask(__name__)
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

# 集成 swagger
Swagger(app)

# 注册接口
api = Api(app)
api.add_resource(ServoResource, '/servo/<int:gpio>/<int:angle>/<int:total_angle>', endpoint='servo')
api.add_resource(RelayResource, '/relay/<int:gpio>/<string:onoff>', endpoint='relay')
api.add_resource(ButtonResource, '/button/<int:gpio>', endpoint='button')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)