# 菜单题漏洞分析工具集

本工具集包含多个脚本，用于对MCP中打开的二进制程序进行fuzz测试和漏洞分析。

## 文件说明

### 1. test_binary.py
简单的二进制程序测试脚本，用于验证程序是否能正常启动。

**用法:**
```bash
python3 test_binary.py <binary_path>
```

### 2. fuzz_script.py
模糊测试脚本，对菜单选项进行随机输入测试，寻找崩溃点。

**用法:**
```bash
python3 fuzz_script.py <binary_path>
```

**功能:**
- 随机生成菜单选择和数据
- 测试边界情况（负数、超大数字、特殊字符）
- 自动保存崩溃信息到文件
- 统计崩溃率和测试次数

### 3. exploit_script.py
Pwntools交互脚本，提供完整的菜单交互功能。

**用法:**
```bash
# 本地测试
python3 exploit_script.py <binary_path>

# 远程测试
python3 exploit_script.py <binary_path> remote <host> <port>
```

**功能:**
- 完整的菜单交互功能
- 基本功能测试
- 边界情况测试
- 格式字符串漏洞测试
- 堆操作测试
- 整数溢出测试
- 交互模式

### 4. advanced_exploit.py
高级漏洞分析脚本，结合多种攻击技术。

**用法:**
```bash
python3 advanced_exploit.py <binary_path>
```

**功能:**
- Use After Free (UAF) 漏洞测试
- 堆喷射测试
- 格式字符串漏洞测试
- 缓冲区溢出测试
- 整数溢出测试
- 类型混淆测试
- 竞态条件测试

## 程序分析结果

基于静态分析，该二进制程序具有以下特点：

### 程序结构
- **语言**: C++
- **架构**: x86_64
- **保护机制**: 
  - 栈保护 (Stack Canary)
  - seccomp沙箱
  - 操作次数限制

### 菜单系统
1. **Daily Grind | #CheckInChallenge** - 创建笔记
2. **Spill the Tea | #HonestReviews** - 显示笔记
3. **显示笔记内容** - 显示特定笔记内容
4. **设置笔记内容** - 修改笔记内容
5. **Delete the Evidence** - 删除笔记
6. **Exit the Chat** - 退出程序

### 潜在漏洞点
1. **Use After Free**: 删除笔记后仍可能访问
2. **堆管理**: 笔记的创建和删除可能存在问题
3. **整数溢出**: 笔记编号和内容长度检查
4. **类型混淆**: 不同类型的笔记处理
5. **格式字符串**: 用户输入直接输出

## 使用建议

### 1. 基础测试
```bash
# 首先测试程序是否能正常运行
python3 test_binary.py ./pwn

# 进行模糊测试
python3 fuzz_script.py ./pwn
```

### 2. 深入分析
```bash
# 使用交互脚本进行手动测试
python3 exploit_script.py ./pwn

# 运行高级漏洞分析
python3 advanced_exploit.py ./pwn
```

### 3. 漏洞利用
根据测试结果，重点关注：
- 崩溃日志文件 (`crash_*.txt`)
- UAF漏洞的利用
- 堆喷射的可能性
- 格式字符串漏洞

## 注意事项

1. **权限**: 确保有执行二进制程序的权限
2. **依赖**: 需要安装pwntools: `pip install pwntools`
3. **环境**: 建议在Linux环境下运行
4. **安全**: 这些脚本仅用于安全研究和漏洞分析

## 预期结果

通过运行这些脚本，应该能够：
1. 识别程序的崩溃点
2. 发现潜在的漏洞类型
3. 验证漏洞的可利用性
4. 为后续的漏洞利用提供基础

## 后续步骤

1. 分析崩溃日志，确定漏洞类型
2. 针对特定漏洞编写利用脚本
3. 绕过安全机制（如seccomp）
4. 实现代码执行或信息泄露

