from .models.game_models import Item

# 普通物品列表（quality=0）
common_items = [
    Item(id="item_bread", name="军事情报", value=32 , quality=0, weight=20),
    Item(id="item_water", name="单筒望远镜", value=22 , quality=0, weight=20),
    Item(id="item_apple", name="苹果", value=32 , quality=0, weight=15),
    Item(id="item_bandage", name="银币", value=22 , quality=0, weight=25),
    Item(id="item_stone", name="跳舞的女郎", value=22 , quality=0, weight=10),
    Item(id="item_wood", name="香喷喷烤面", value=42 , quality=0, weight=10),
    Item(id="item_pilot_glasses", name="飞行员眼镜", value=26 , quality=0, weight=18),
    Item(id="item_seafood_canned_porridge", name="海鲜粥罐头", value=38 , quality=0, weight=12),
    Item(id="item_nutrition_canned_porridge", name="营养粥罐头", value=34 , quality=0, weight=14),
    Item(id="item_hunting_matches", name="狩猎火柴", value=24 , quality=0, weight=22),
    Item(id="item_sugar_triangle", name="糖三角", value=28 , quality=0, weight=16),
    Item(id="item_gunpowder", name="火药", value=36 , quality=0, weight=13)
]

# 稀有物品列表（quality=1）
rare_items = [
    Item(id="item_iron_sword", name="仪式匕首", value=150 , quality=1, weight=15),
    Item(id="item_iron_armor", name="后妈耳环", value=60 , quality=1, weight=100),
    Item(id="item_leather_boot", name="黄金饰章", value=60 , quality=1, weight=100),
    Item(id="item_silver_ring", name="电动车电池", value=150 , quality=1, weight=15),
    Item(id="item_hunting_knife", name="完整牛角", value=60 , quality=1, weight=100),
    Item(id="item_elegant_coffee_cup", name="典雅咖啡杯", value=120 , quality=1, weight=30),
    Item(id="item_gingerbread_man", name="小糖人姜饼人", value=90 , quality=1, weight=50),
    Item(id="item_totem_arrow", name="图腾箭矢", value=110 , quality=1, weight=40),
    Item(id="item_bio_incubator", name="生化培养箱", value=180 , quality=1, weight=20),
    Item(id="item_mosaic_lamp", name="马赛克灯台", value=140 , quality=1, weight=25),
    Item(id="item_hydraulic_wrench", name="便携液压扳手", value=170 , quality=1, weight=22),
    Item(id="item_wide_angle_lens", name="广角镜头", value=200 , quality=1, weight=18)
]

# 史诗物品列表（quality=2）
epic_items = [
    Item(id="item_steel_sword", name="本地特色首饰", value=1000, quality=2, weight=5),
    Item(id="item_steel_armor", name="大型电台", value=1300, quality=2, weight=5),
    Item(id="item_magic_amulet", name="珠宝王冠", value=600 , quality=2, weight=30),
    Item(id="item_elf_bow", name="金杯", value=300, quality=2, weight=40),
    Item(id="item_dragon_scale", name="金图纸", value=300, quality=2, weight=40),
    Item(id="item_golden_laurel", name="金枝桂冠", value=1200, quality=2, weight=8),
    Item(id="item_raven_pendant", name="渡鸦项坠", value=1100, quality=2, weight=10),
    Item(id="item_music_box", name="发条八音盒", value=900, quality=2, weight=12),
    Item(id="item_ghthroth_judgment", name="格赫罗斯的审判", value=1400, quality=2, weight=5),
    Item(id="item_pearl", name="三角蚌小珍珠", value=500, quality=2, weight=35),
    Item(id="item_golden_pen", name="金笔", value=700, quality=2, weight=25),
    Item(id="item_satellite_phone", name="卫星电话", value=800, quality=2, weight=20),
    Item(id="item_military_module", name="军用网路模块", value=850, quality=2, weight=18),
    Item(id="item_army_multimeter", name="陆军万用表", value=650, quality=2, weight=30),
    Item(id="item_heart_stent_epic", name="心脏支架", value=950, quality=2, weight=15)
]

# 传说物品列表（quality=3）
legendary_items = [
    Item(id="item_excalibur", name="军用炮弹", value=2200 , quality=3, weight=30),
    Item(id="item_holy_armor", name="笔记本电脑", value=2100 , quality=3, weight=20),
    Item(id="item_philosophers_stone", name="非洲之心", value=20000 , quality=3, weight=1),
    Item(id="item_dragon_slayer", name="量子存储", value=1500 , quality=3, weight=50),
    Item(id="item_amulet_of_immortality", name="复苏呼吸机", value=10000 , quality=3, weight=5),
    Item(id="item_holy_armor", name="光盘", value=1000 , quality=3, weight=50),
    Item(id="item_holy_armor", name="劳力士", value=1200 , quality=3, weight=50),
    Item(id="item_gilded_card", name="鎏金卡牌", value=1100 , quality=3, weight=50),  # 调整为与劳力士相同
    Item(id="item_impressionist_painting", name="印象派名画", value=2000 , quality=3, weight=10),  # 调整为合理值
    Item(id="item_white_porcelain_vase", name="白瓷净瓶", value=1800 , quality=3, weight=12),  # 调整为合理值
    Item(id="item_golden_gazelle", name="黄金瞪羚", value=2200 , quality=3, weight=30),  # 调整为与军用炮弹相同
    Item(id="item_ecmo", name="ECMO", value=2300 , quality=3, weight=13),  # 调整为合理值
    Item(id="item_mandel_supercomputer", name="曼德尔超算单元", value=1500 , quality=3, weight=15),  # 调整为合理值
    Item(id="item_portable_radar", name="便携军用雷达", value=3000 , quality=3, weight=18),  # 调整为合理值
    Item(id="item_military_terminal", name="军用信息终端", value=1300 , quality=3, weight=50),  # 调整为合理值
    Item(id="item_main_battle_tank", name="主战坦克模型", value=2000 , quality=3, weight=15),  # 调整为合理值
    Item(id="item_infantry_fighting_vehicle", name="步战车模型", value=1300 , quality=3, weight=20),  # 调整为合理值
]

# 所有物品合并列表，用于搜索时随机获取物品
all_items = common_items + rare_items + epic_items + legendary_items

# 按品质分类的物品字典，便于按品质获取
items_by_quality = {
    0: common_items,
    1: rare_items,
    2: epic_items,
    3: legendary_items
}