class Settings:
    """存储游戏《外星人入侵》中所有的设置"""

    def __init__(self):
        """初始化游戏设置"""
        # 屏幕设置
        self.screen_width = 1120
        self.screen_height = 630
        self.bg_color = (230, 230, 230)
        # 飞船设置
        self.ship_speed = 1.5
        self.ship_limit = 3
        # 子弹设置
        self.bullet_speed = 0.5
        self.bullet_width = 1300
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 5
        # 外星人设置
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        # fleet_direction 为 1 表示向右移动， 为 -1 表示向左移动
        self.fleet_direction = 1