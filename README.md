# Live Captions Web

一个实时字幕显示系统，支持从Luna Python脚本获取字幕数据并在网页中实时显示。

## 🌟 功能特性

### 核心功能
- **实时字幕显示** - 从Luna脚本获取字幕数据并实时显示
- **单词级更新** - 支持单词级别的动态刷新，避免整句重新渲染
- **增量显示** - 新内容增量添加，已完成内容保持不变

### 插件兼容
- **Lingkuma单词高亮兼容** - 超级完美支持Lingkuma，高亮生词，熟词，解析，小窗，侧栏等
- **沉浸式翻译兼容** - 完美支持沉浸式翻译插件

### 分享功能
- **Telegraph分享** - 一键分享原文到Telegraph平台
- **翻译内容分享** - 支持包含沉浸式翻译内容的分享

### 统计功能
- **监听时间** - 实时显示总监听时长
- **单词统计** - 统计总单词数和完成句子数
- **最后更新** - 显示最后更新时间

## 📁 项目结构

```
LiveCaptionsWeb/
├── README.md                 # 项目说明文档
├── live_captions.html        # 主界面HTML文件
└── LunaCaptionsListener.py   # Luna Python脚本
```

## 🚀 快速开始

### 环境要求
- Python 3.6+
- 现代浏览器（Chrome、Firefox、Safari、Edge）
- Luna脚本环境（用于字幕数据源）

### 安装步骤

1. **克隆项目**
   ```bash
   git clone <repository-url>
   cd LiveCaptionsWeb
   ```

2. **配置Luna脚本**
   - 将 `LunaCaptionsListener.py` 内容复制到LunaTranslator中
   - 确保Luna脚本调用 `POSTSOLVE(line)` 函数传递字幕数据

3. **启动服务**
   - Python服务会在Luna脚本首次调用时自动启动
   - 默认端口：8765（如果占用会自动尝试8766）

4. **打开界面**
   - 在浏览器中打开 `live_captions.html`
   - 点击"开始连接"按钮连接到后端服务


## 📄 许可证

本项目采用MIT许可证，详见LICENSE文件。

## 🙏 致谢

- Luna脚本平台提供数据源支持
- Telegraph平台提供分享服务
