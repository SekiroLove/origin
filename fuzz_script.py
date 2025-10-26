#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
菜单题Fuzz脚本
针对二进制程序的菜单选项进行模糊测试
"""

import subprocess
import random
import string
import time
import os
import signal
import sys

class MenuFuzzer:
    def __init__(self, binary_path):
        self.binary_path = binary_path
        self.crash_count = 0
        self.test_count = 0
        self.max_tests = 1000
        
    def generate_random_input(self):
        """生成随机输入"""
        inputs = []
        
        # 生成菜单选择 (1-6)
        menu_choice = random.randint(1, 6)
        inputs.append(str(menu_choice))
        
        # 根据菜单选择生成相应的输入
        if menu_choice == 1:  # Daily Grind - 创建笔记
            # 笔记类型选择 (1-3)
            note_type = random.randint(1, 3)
            inputs.append(str(note_type))
            
            # 随机内容
            content_length = random.randint(1, 1000)
            content = ''.join(random.choices(string.ascii_letters + string.digits + ' ', k=content_length))
            inputs.append(content)
            
        elif menu_choice == 2:  # Spill the Tea - 显示笔记
            # 笔记编号
            note_num = random.randint(0, 20)
            inputs.append(str(note_num))
            
        elif menu_choice == 3:  # 显示笔记内容
            note_num = random.randint(0, 20)
            inputs.append(str(note_num))
            
        elif menu_choice == 4:  # 设置笔记内容
            note_num = random.randint(0, 20)
            inputs.append(str(note_num))
            
            # 随机内容
            content_length = random.randint(1, 2000)
            content = ''.join(random.choices(string.ascii_letters + string.digits + ' ', k=content_length))
            inputs.append(content)
            
        elif menu_choice == 5:  # Delete the Evidence
            note_num = random.randint(0, 20)
            inputs.append(str(note_num))
            
        return inputs
    
    def generate_edge_case_inputs(self):
        """生成边界情况输入"""
        edge_cases = [
            # 负数
            ["1", "-1", "test"],
            ["2", "-1"],
            ["3", "-1"],
            ["4", "-1", "test"],
            ["5", "-1"],
            
            # 超大数字
            ["1", "999999999", "test"],
            ["2", "999999999"],
            ["3", "999999999"],
            ["4", "999999999", "test"],
            ["5", "999999999"],
            
            # 特殊字符
            ["1", "1", "A" * 10000],
            ["4", "1", "A" * 10000],
            
            # 空输入
            ["1", "", ""],
            ["2", ""],
            ["3", ""],
            ["4", "", ""],
            ["5", ""],
            
            # 格式字符串
            ["1", "1", "%x%x%x%x%x%x%x%x"],
            ["4", "1", "%x%x%x%x%x%x%x%x"],
            
            # 缓冲区溢出尝试
            ["1", "1", "A" * 0x1000],
            ["4", "1", "A" * 0x1000],
        ]
        
        return random.choice(edge_cases)
    
    def run_binary_with_input(self, inputs):
        """运行二进制程序并输入测试数据"""
        try:
            # 启动进程
            process = subprocess.Popen(
                [self.binary_path],
                stdin=subprocess.PIPE,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True
            )
            
            # 发送输入
            input_data = '\n'.join(inputs) + '\n'
            stdout, stderr = process.communicate(input=input_data, timeout=10)
            
            return process.returncode, stdout, stderr
            
        except subprocess.TimeoutExpired:
            process.kill()
            return -1, "", "Timeout"
        except Exception as e:
            return -1, "", str(e)
    
    def analyze_crash(self, returncode, stdout, stderr, inputs):
        """分析崩溃情况"""
        if returncode != 0:
            self.crash_count += 1
            print(f"[CRASH #{self.crash_count}] Return code: {returncode}")
            print(f"Input: {inputs}")
            print(f"STDOUT: {stdout}")
            print(f"STDERR: {stderr}")
            print("-" * 50)
            
            # 保存崩溃信息到文件
            with open(f"crash_{self.crash_count}.txt", "w") as f:
                f.write(f"Return code: {returncode}\n")
                f.write(f"Input: {inputs}\n")
                f.write(f"STDOUT: {stdout}\n")
                f.write(f"STDERR: {stderr}\n")
    
    def fuzz(self):
        """开始模糊测试"""
        print(f"开始对 {self.binary_path} 进行模糊测试...")
        print(f"最大测试次数: {self.max_tests}")
        print("-" * 50)
        
        while self.test_count < self.max_tests:
            self.test_count += 1
            
            # 随机选择测试类型
            if random.random() < 0.7:  # 70% 随机输入
                inputs = self.generate_random_input()
            else:  # 30% 边界情况
                inputs = self.generate_edge_case_inputs()
            
            print(f"[TEST #{self.test_count}] Input: {inputs}")
            
            # 运行测试
            returncode, stdout, stderr = self.run_binary_with_input(inputs)
            
            # 分析结果
            self.analyze_crash(returncode, stdout, stderr, inputs)
            
            # 短暂延迟
            time.sleep(0.1)
        
        print(f"\n模糊测试完成!")
        print(f"总测试次数: {self.test_count}")
        print(f"崩溃次数: {self.crash_count}")
        print(f"崩溃率: {self.crash_count/self.test_count*100:.2f}%")

def main():
    if len(sys.argv) != 2:
        print("用法: python3 fuzz_script.py <binary_path>")
        sys.exit(1)
    
    binary_path = sys.argv[1]
    if not os.path.exists(binary_path):
        print(f"错误: 文件 {binary_path} 不存在")
        sys.exit(1)
    
    fuzzer = MenuFuzzer(binary_path)
    fuzzer.fuzz()

if __name__ == "__main__":
    main()
