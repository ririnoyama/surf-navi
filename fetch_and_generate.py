from datetime import datetime

# 仮データ（本来はAPIやスクレイピングで取得）
spot1 = "波高1.2m、南南西風5m/s、うねり東南東、満潮4:24/16:50"
spot2 = "波高1.1m、風は南、ピーク間隔11秒、干潮9:09/21:01"
spot3 = "波高0.8m、風は南南西、ピーク間隔8秒、満潮4:23/18:59"

with open("index_template.html", "r", encoding="utf-8") as f:
    template = f.read()

html = template.replace("{{spot1}}", spot1)\
               .replace("{{spot2}}", spot2)\
               .replace("{{spot3}}", spot3)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)
