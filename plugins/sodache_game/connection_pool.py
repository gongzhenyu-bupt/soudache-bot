import sqlite3
from typing import List, Optional

class ConnectionPool:
    """A simple SQLite connection pool"""
    
    def __init__(self, db_path: str, pool_size: int = 5, timeout: int = 5):
        """
        初始化连接池
        
        参数:
        - db_path: 数据库文件路径
        - pool_size: 连接池大小，默认5
        - timeout: 数据库操作超时时间（秒），默认5
        """
        self.db_path = db_path
        self.pool_size = pool_size
        self.timeout = timeout
        self.connections: List[sqlite3.Connection] = []
    
    def get_conn(self) -> sqlite3.Connection:
        """从连接池获取一个数据库连接"""
        if self.connections:
            return self.connections.pop()
        # 如果连接池为空，创建新连接
        return sqlite3.connect(self.db_path, timeout=self.timeout)
    
    def put_conn(self, conn: sqlite3.Connection) -> None:
        """将连接放回连接池"""
        if len(self.connections) < self.pool_size:
            self.connections.append(conn)
        else:
            # 如果连接池已满，关闭该连接
            conn.close()
    
    def close_all(self) -> None:
        """关闭连接池中的所有连接"""
        for conn in self.connections:
            conn.close()
        self.connections.clear()