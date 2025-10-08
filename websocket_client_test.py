import socketio
import time
import threading

class ChassisWebSocketClient:
    """底盘 WebSocket 客户端测试"""

    def __init__(self, server_url='http://localhost:8081'):
        self.sio = socketio.Client()
        self.server_url = server_url
        self.connected = False
        self.setup_event_handlers()

    def setup_event_handlers(self):
        """设置事件处理器"""

        @self.sio.event
        def connect():
            print("✅ 已连接到 WebSocket 服务器")
            self.connected = True

        @self.sio.event
        def disconnect():
            print("❌ 已断开与 WebSocket 服务器的连接")
            self.connected = False

        @self.sio.event
        def connected(data):
            print(f"🔗 服务器确认连接: {data}")

        @self.sio.event
        def chassis_response(data):
            print(f"🤖 底盘控制响应: {data}")

        @self.sio.event
        def status_update(data):
            print(f"📊 状态更新: {data}")

        @self.sio.event
        def emergency_stop_response(data):
            print(f"🛑 紧急停止响应: {data}")

        @self.sio.event
        def status_response(data):
            print(f"📋 状态查询响应: {data}")

        @self.sio.event
        def pong(data):
            print(f"🏓 心跳响应: {data}")

    def connect(self):
        """连接到服务器"""
        try:
            self.sio.connect(self.server_url)
            return True
        except Exception as e:
            print(f"❌ 连接失败: {e}")
            return False

    def disconnect(self):
        """断开连接"""
        if self.connected:
            self.sio.disconnect()

    def control_chassis(self, direction, speed=0):
        """控制底盘"""
        if not self.connected:
            print("❌ 未连接到服务器")
            return

        self.sio.emit('chassis_control', {
            'direction': direction,
            'speed': speed
        })
        print(f"📤 发送控制命令: {direction}, 速度: {speed}")

    def get_status(self):
        """获取状态"""
        if not self.connected:
            print("❌ 未连接到服务器")
            return

        self.sio.emit('get_status')
        print("📤 请求状态更新")

    def emergency_stop(self):
        """紧急停止"""
        if not self.connected:
            print("❌ 未连接到服务器")
            return

        self.sio.emit('emergency_stop')
        print("📤 发送紧急停止命令")

    def ping(self):
        """心跳检测"""
        if not self.connected:
            print("❌ 未连接到服务器")
            return

        self.sio.emit('ping')
        print("📤 发送心跳")

def test_basic_commands():
    """测试基本命令"""
    client = ChassisWebSocketClient()

    if not client.connect():
        return

    try:
        # 等待连接稳定
        time.sleep(1)

        print("\n=== 开始测试底盘控制命令 ===")

        # 获取初始状态
        client.get_status()
        time.sleep(1)

        # 测试各种命令
        commands = [
            ('forward', 50),
            ('pause', 0),
            ('reverse', 30),
            ('pause', 0),
            ('turn_left', 40),
            ('pause', 0),
            ('turn_right', 40),
            ('stop', 0)
        ]

        for direction, speed in commands:
            print(f"\n--- 测试: {direction}, 速度: {speed} ---")
            client.control_chassis(direction, speed)
            time.sleep(2)

        # 最终获取状态
        client.get_status()
        time.sleep(1)

        print("\n=== 测试完成 ===")

    except KeyboardInterrupt:
        print("\n⚠️ 用户中断测试")
    finally:
        client.disconnect()

def test_interactive_mode():
    """交互式测试模式"""
    client = ChassisWebSocketClient()

    if not client.connect():
        return

    print("\n=== 进入交互式控制模式 ===")
    print("命令格式: <direction> <speed>")
    print("可用方向: forward, reverse, turn_left, turn_right, start, pause, stop")
    print("速度范围: 0-100")
    print("其他命令: status (获取状态), ping (心跳), emergency (紧急停止), quit (退出)")

    try:
        while True:
            command = input("\n请输入命令: ").strip().lower()

            if command == 'quit':
                break
            elif command == 'status':
                client.get_status()
            elif command == 'ping':
                client.ping()
            elif command == 'emergency':
                client.emergency_stop()
            elif command:
                parts = command.split()
                if len(parts) >= 1:
                    direction = parts[0]
                    speed = int(parts[1]) if len(parts) > 1 and parts[1].isdigit() else 0
                    client.control_chassis(direction, speed)

            time.sleep(0.5)

    except KeyboardInterrupt:
        print("\n⚠️ 用户中断")
    except Exception as e:
        print(f"❌ 错误: {e}")
    finally:
        client.disconnect()

if __name__ == '__main__':
    import sys

    print("WebSocket 底盘控制客户端")
    print("选择测试模式:")
    print("1. 自动测试模式")
    print("2. 交互式控制模式")

    try:
        choice = input("请选择 (1/2): ").strip()

        if choice == '1':
            test_basic_commands()
        elif choice == '2':
            test_interactive_mode()
        else:
            print("❌ 无效选择")
    except KeyboardInterrupt:
        print("\n👋 再见!")
