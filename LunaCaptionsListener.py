
import json
import threading
import time
import socket

_current_line = ""  # 当前行数据
_server_socket = None  # 服务器socket
_server_thread = None  # 服务器线程
_server_running = False  # 服务器运行状态

def handle_request(client_socket):
    """处理单个HTTP请求"""
    try:
        request = client_socket.recv(1024).decode('utf-8')

        if 'GET /captions' in request:
            # 构造响应数据
            data = {
                'current_line': _current_line,
                'timestamp': time.time()
            }

            response_body = json.dumps(data, ensure_ascii=False)
            response = f"""HTTP/1.1 200 OK\r
Content-Type: application/json; charset=utf-8\r
Access-Control-Allow-Origin: *\r
Content-Length: {len(response_body.encode('utf-8'))}\r
\r
{response_body}"""
        else:
            response = "HTTP/1.1 404 Not Found\r\n\r\n"

        client_socket.send(response.encode('utf-8'))
    except Exception as e:
        print(f"处理请求错误: {e}")
    finally:
        client_socket.close()

def server_loop():
    """服务器主循环"""
    global _server_socket, _server_running

    while _server_running:
        try:
            client_socket, addr = _server_socket.accept()
            # 在新线程中处理请求
            client_thread = threading.Thread(target=handle_request, args=(client_socket,), daemon=True)
            client_thread.start()
        except Exception as e:
            if _server_running:  # 只在服务器运行时打印错误
                print(f"接受连接错误: {e}")

def start_server():
    """启动HTTP服务器"""
    global _server_socket, _server_thread, _server_running

    if _server_socket is None:
        try:
            print("正在启动Caption服务器...")
            _server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            _server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            _server_socket.bind(('127.0.0.1', 8765))
            _server_socket.listen(5)
            _server_running = True

            _server_thread = threading.Thread(target=server_loop, daemon=True)
            _server_thread.start()
            print("Caption server started on http://127.0.0.1:8765")
        except Exception as e:
            print(f"Failed to start server: {e}")
            # 尝试其他端口
            try:
                print("尝试端口8766...")
                _server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                _server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
                _server_socket.bind(('127.0.0.1', 8766))
                _server_socket.listen(5)
                _server_running = True

                _server_thread = threading.Thread(target=server_loop, daemon=True)
                _server_thread.start()
                print("Caption server started on http://127.0.0.1:8766")
            except Exception as e2:
                print(f"端口8766也失败: {e2}")

def stop_server():
    """停止HTTP服务器"""
    global _server_socket, _server_thread, _server_running

    _server_running = False
    if _server_socket:
        _server_socket.close()
        _server_socket = None
        _server_thread = None

def POSTSOLVE(line):
    """
    Luna脚本接口函数
    - 不做任何缓存处理
    - 只是将当前line数据提供给网页端
    - Luna正常返回line内容
    """
    global _current_line

    print(f"POSTSOLVE被调用，line: '{line}'")  # 调试信息

    # 启动服务器（如果还没启动）
    start_server()

    # 更新当前行数据供网页端获取
    _current_line = line if line else ""
    print(f"更新_current_line: '{_current_line}'")  # 调试信息

    # Luna直接返回原始内容，不做任何处理
    return line if line else ""




