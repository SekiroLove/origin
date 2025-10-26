set pagination off
set confirm off

# 设置断点
break main
break malloc
break free

# 运行程序
run

# 显示内存布局
echo "显示内存布局:\n"
info proc mappings
echo "\n"

# 继续执行
continue

# 显示寄存器
echo "显示寄存器:\n"
info registers
echo "\n"

# 显示栈
echo "显示栈:\n"
x/20x $rsp
echo "\n"

# 退出
quit
