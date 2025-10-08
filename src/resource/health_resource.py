from flask_restful import Resource


class HealthResource(Resource):
    """
    监控检查控制
    """

    def get(self, status):
        """
        监控检查控制 API
        ---
        tags:
          - 监控检查控制 API
        parameters:
          - name: direction
            in: path
            type:  string
            required: true
            status: 状态 ping
        responses:
          500:
            description: 参数错误
          200:
            description: 正确执行
            schema:
              id: R
              properties:
                code:
                  type: string
                  description: 状态码
                  default: "0000"
        """

        return {"code": "0000", "info": "pong"}
