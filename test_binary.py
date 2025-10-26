#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
简单测试脚本
用于快速验证二进制程序的基本功能
"""

import subprocess
import time
import os
import sys

def test_binary(binary_path):
    """测试二进制程序的基本功能"""
    print(f"测试二进制程序: {binary_path}")
    
    if not os.path.exists(binary_path):
        print(f"错误: 文件 {binary_path} 不存在")
        return False
    
    try:
        # 启动程序
        process = subprocess.Popen(
            [binary_path],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        
        # 等待欢迎信息
        stdout, stderr = process.communicate(input="6\n", timeout=5)
        
        if "Welcome to the All-Pwn-Red-Book App!" in stdout:
            print("[+] 程序启动成功")
            print(f"[+] 输出: {stdout}")
            return True
        else:
            print("[-] 程序启动失败")
            print(f"STDOUT: {stdout}")
            print(f"STDERR: {stderr}")
            return False
            
    except subprocess.TimeoutExpired:
        process.kill()
        print("[-] 程序超时")
        return False
    except Exception as e:
        print(f"[-] 错误: {e}")
        return False

def main():
    if len(sys.argv) != 2:
        print("用法: python3 test_binary.py <binary_path>")
        sys.exit(1)
    
    binary_path = sys.argv[1]
    success = test_binary(binary_path)
    
    if success:
        print("\n[+] 二进制程序测试通过，可以开始fuzz和exploit")
    else:
        print("\n[-] 二进制程序测试失败")

if __name__ == "__main__":
    main()

