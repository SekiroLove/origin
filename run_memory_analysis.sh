#!/bin/bash
# GDB内存分析脚本

echo "启动GDB内存分析..."

# 创建GDB命令文件
cat > memory_analysis.gdb << 'EOF'
# 内存分析GDB脚本
set pagination off
set confirm off

# 设置断点
break main
break *0x469100  # 创建笔记函数
break *0x469760  # 删除笔记函数
break *0x469420  # 显示笔记内容函数
break malloc
break free

# 运行程序
run

# 显示程序启动时的内存布局
echo "程序启动时的内存布局:\n"
info proc mappings
echo "\n"

# 创建第一个笔记
echo "创建第一个笔记...\n"
continue

# 显示创建笔记后的内存状态
echo "创建笔记后的内存状态:\n"
info registers
echo "\n"
x/20x $rsp
echo "\n"

# 创建第二个笔记
echo "创建第二个笔记...\n"
continue

# 显示创建第二个笔记后的内存状态
echo "创建第二个笔记后的内存状态:\n"
info registers
echo "\n"
x/20x $rsp
echo "\n"

# 删除第一个笔记
echo "删除第一个笔记...\n"
continue

# 显示删除笔记后的内存状态
echo "删除笔记后的内存状态:\n"
info registers
echo "\n"
x/20x $rsp
echo "\n"

# 尝试访问已删除的笔记
echo "尝试访问已删除的笔记...\n"
continue

# 显示访问时的内存状态
echo "访问时的内存状态:\n"
info registers
echo "\n"
x/20x $rsp
echo "\n"
bt
echo "\n"

# 退出
quit
EOF

# 运行GDB
gdb -x memory_analysis.gdb ./all-pwn-red-book/pwn

echo "内存分析完成"
