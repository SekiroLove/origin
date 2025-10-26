#!/bin/bash
# 交互式GDB调试脚本

echo "启动交互式GDB调试..."

# 创建GDB命令文件
cat > interactive_debug.gdb << 'EOF'
# 交互式GDB调试脚本
set pagination off
set confirm off

# 设置断点
break main
break *0x469100  # 创建笔记函数
break *0x4692f0  # 显示笔记函数
break *0x469420  # 显示笔记内容函数
break *0x4695c0  # 设置笔记内容函数
break *0x469760  # 删除笔记函数

# 设置关键函数断点
break *0x469bc0  # 删除笔记关键函数
break *0x469c20  # 笔记数组操作
break *0x469c50  # 笔记删除清理

# 设置堆断点
break malloc
break free

# 运行程序
run

# 显示当前状态
echo "程序已启动，可以开始调试\n"
echo "可用命令:\n"
echo "  1. 创建笔记\n"
echo "  2. 显示笔记\n"
echo "  3. 显示笔记内容\n"
echo "  4. 设置笔记内容\n"
echo "  5. 删除笔记\n"
echo "  6. 退出\n"
echo "使用 'continue' 继续执行\n"
echo "使用 'info registers' 查看寄存器\n"
echo "使用 'x/10x $rsp' 查看栈\n"
echo "使用 'x/10x $rax' 查看返回值\n"
echo "使用 'bt' 查看调用栈\n"
echo "使用 'info breakpoints' 查看断点\n"
echo "使用 'delete breakpoints' 删除所有断点\n"
echo "使用 'quit' 退出GDB\n"
EOF

# 运行GDB
gdb -x interactive_debug.gdb ./all-pwn-red-book/pwn

echo "交互式调试完成"
