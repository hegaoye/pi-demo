import logging

from flask import Flask
from flask_socketio import SocketIO, emit

from src.driver.ws2412d_driver import get_motor_instance
from src.resource.chassis_resource import ChassisResource

# 配置日志
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# 创建 Flask 应用
app = Flask(__name__)
app.config['SECRET_KEY'] = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

# 初始化 SocketIO
socketio = SocketIO(app, cors_allowed_origins="*", async_mode='threading')


class ChassisWebSocketController:
    """WebSocket 底盘控制器"""

    def __init__(self):
        self.robot = ChassisResource()
        self.current_status = {
            'direction': 'stop',
            'speed': 0,
            'is_running': False
        }

    def execute_command(self, direction, speed=0):
        """执行底盘控制命令，逻辑参考 ChassisResource"""
        try:
            print(f"执行命令: {direction}, 速度: {speed}")

            self.robot.get(direction, speed)
            if direction == 'forward':
                self.current_status.update({
                    'direction': direction,
                    'speed': speed,
                    'is_running': True
                })
            elif direction == 'reverse':
                self.current_status.update({
                    'direction': direction,
                    'speed': speed,
                    'is_running': True
                })
            elif direction == 'turn_left':
                self.current_status.update({
                    'direction': direction,
                    'speed': speed,
                    'is_running': True
                })
            elif direction == 'turn_right':
                self.current_status.update({
                    'direction': direction,
                    'speed': speed,
                    'is_running': True
                })
            elif direction == 'start':
                self.current_status.update({
                    'direction': direction,
                    'speed': 0,
                    'is_running': True
                })
            elif direction == 'pause':
                self.current_status.update({
                    'direction': direction,
                    'speed': 0,
                    'is_running': False
                })
            elif direction == 'stop':
                self.current_status.update({
                    'direction': direction,
                    'speed': 0,
                    'is_running': False
                })
            else:
                return {'code': '9999', 'message': f'未知的方向指令: {direction}'}

            logger.info(f"执行命令: {direction}, 速度: {speed}")
            return {'code': '0000', 'message': '执行成功', 'status': self.current_status}

        except Exception as e:
            logger.error(f"执行底盘命令时出错: {e}")
            return {'code': '9999', 'message': f'执行失败: {str(e)}'}


# 创建控制器实例
chassis_controller = ChassisWebSocketController()


@socketio.on('connect')
def handle_connect():
    """客户端连接事件"""
    logger.info("客户端已连接")
    emit('connected', {
        'code': '0000',
        'message': '连接成功',
        'status': chassis_controller.current_status
    })


@socketio.on('disconnect')
def handle_disconnect():
    """客户端断开连接事件"""
    logger.info("客户端已断开连接")
    # 安全起见，断开连接时停止底盘
    try:
        chassis_controller.execute_command('stop')
    except Exception as e:
        logger.error(f"断开连接时停止底盘失败: {e}")


@socketio.on('chassis_control')
def handle_chassis_control(data):
    """处理底盘控制命令"""
    try:
        direction = data.get('direction', 'stop')
        speed = int(data.get('speed', 0))
        print(data)
        logger.info(f"执行命令: {direction}, 速度: {speed}")

        # 验证速度范围
        if not 0 <= speed <= 100:
            emit('chassis_response', {
                'code': '9999',
                'message': '速度必须在 0-100 范围内'
            })
            return

        # 验证方向参数
        valid_directions = ['forward', 'reverse', 'turn_left', 'turn_right', 'start', 'pause', 'stop']
        if direction not in valid_directions:
            emit('chassis_response', {
                'code': '9999',
                'message': f'无效的方向参数: {direction}，有效值: {valid_directions}'
            })
            return

        logger.info(f"收到底盘控制命令: direction={direction}, speed={speed}")

        # 执行命令
        result = chassis_controller.execute_command(direction, speed)

        # 发送结果给客户端
        emit('chassis_response', result)

        # 如果执行成功，广播状态更新给所有连接的客户端
        if result.get('code') == '0000':
            socketio.emit('status_update', result.get('status', chassis_controller.current_status))

    except ValueError as e:
        logger.error(f"参数类型错误: {e}")
        emit('chassis_response', {
            'code': '9999',
            'message': f'参数类型错误: {str(e)}'
        })
    except Exception as e:
        logger.error(f"处理底盘控制命令时出错: {e}")
        emit('chassis_response', {
            'code': '9999',
            'message': f'处理命令失败: {str(e)}'
        })


@socketio.on('get_status')
def handle_get_status():
    """获取当前底盘状态"""
    emit('status_response', {
        'code': '0000',
        'status': chassis_controller.current_status
    })


@socketio.on('emergency_stop')
def handle_emergency_stop():
    """紧急停止"""
    logger.warning("收到紧急停止命令")
    result = chassis_controller.execute_command('stop')
    emit('emergency_stop_response', result)
    # 广播紧急停止状态
    socketio.emit('status_update', chassis_controller.current_status)


@socketio.on('ping')
def handle_ping():
    """心跳检测"""
    emit('pong', {'timestamp': int(time.time() * 1000)})


if __name__ == '__main__':
    import time

    logger.info("启动 WebSocket 服务器...")
    logger.info("支持的事件:")
    logger.info(
        "- chassis_control: 底盘控制 {direction: 'forward|reverse|turn_left|turn_right|start|pause|stop', speed: 0-100}")
    logger.info("- get_status: 获取状态")
    logger.info("- emergency_stop: 紧急停止")
    logger.info("- ping: 心跳检测")
    socketio.run(app, host='0.0.0.0', port=8081, debug=True, allow_unsafe_werkzeug=True)
