# UAF漏洞测试GDB脚本
set pagination off
set confirm off

# 设置断点
break main
break *0x469100  # 创建笔记函数
break *0x469760  # 删除笔记函数
break *0x469420  # 显示笔记内容函数

# 运行程序
run

# 创建第一个笔记
echo "创建第一个笔记...\n"
continue

# 创建第二个笔记
echo "创建第二个笔记...\n"
continue

# 删除第一个笔记
echo "删除第一个笔记...\n"
continue

# 尝试访问已删除的笔记
echo "尝试访问已删除的笔记...\n"
continue

# 检查内存状态
echo "检查内存状态...\n"
info registers
echo "\n"
x/20x $rsp
echo "\n"
bt
echo "\n"

# 退出
quit
