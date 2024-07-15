def spa_banner():
    width = 50
    space = ' '*48
    text = "Stores Pricing Analytics (SPA)".upper()
    text_padding = " " * ((width - len(text)) // 2 - 1)
    return f"""
{'╔' + '═' * (width - 2) + '╗'}
║{space}║\n║{text_padding}{text}{text_padding}║\n║{space}║
{'╚' + '═' * (width - 2) + '╝'}
    """
