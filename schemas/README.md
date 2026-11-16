# 结构化协议 v1

JSON Schema使用draft2020-12。source要求固定40位Commit、64位SHA256和1-based行。动画参数中null表示未知；不要用required误解为该字段必须存在确定数值。

validate.py执行这些Schema所使用关键词的标准库子集校验（type/required/properties/items/enum/pattern/minimum/minItems/$ref），并独立检查路径、关联、源码哈希和参数证据。它不是通用JSON Schema实现；后续扩展Schema关键字时须同步校验器，或改用完整合规validator。

可信度词可组合，runtime范围另记录；源码确认、改编方式和实际运行是不同维度。不要把它们压成单一confidence分数。
