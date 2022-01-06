class GameStats:
    """跟踪游戏统计信息"""

    def __init__(self, ai_game):
        """初始化信息"""
        self.settings = ai_game.settings
        self.reset_stats()
        # 游戏刚开始时处于非活跃状态
        self.game_active = False

    def reset_stats(self):
        """初始化游戏统计信息"""
        self.ships_left = self.settings.ship_limit
