#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Sodache Game Plugin for NoneBot2
A text-based adventure game with search, attack, and retreat mechanics
"""

from . import command_routes

__plugin_name__ = "sodache_game"
__plugin_usage__ = """
Sodache游戏命令：
- @机器人 搜索: 开始搜索物品    
- @机器人 攻击 <目标QQ>: 攻击指定玩家
- @机器人 撤离: 撤离当前搜索区域
"""