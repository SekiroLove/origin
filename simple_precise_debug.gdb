set pagination off
set confirm off

# 设置断点
break main
break malloc
break free

# 运行程序
run

# 显示程序启动信息
echo "程序已启动，开始调试...\n"

# 创建第一个笔记
echo "=== 创建第一个笔记 ===\n"
continue

# 检查malloc调用
echo "检查malloc调用:\n"
info registers
echo "\n"
x/10x $rsp
echo "\n"

# 创建第二个笔记
echo "=== 创建第二个笔记 ===\n"
continue

# 检查第二个malloc调用
echo "检查第二个malloc调用:\n"
info registers
echo "\n"
x/10x $rsp
echo "\n"

# 删除第一个笔记
echo "=== 删除第一个笔记 ===\n"
continue

# 检查free调用
echo "检查free调用:\n"
info registers
echo "\n"
x/10x $rsp
echo "\n"

# 尝试访问已删除的笔记
echo "=== 尝试访问已删除的笔记 ===\n"
continue

# 检查访问时的状态
echo "检查访问时的状态:\n"
info registers
echo "\n"
x/10x $rsp
echo "\n"
bt
echo "\n"

# 退出
quit
