<div align="center">
  <a href="https://v2.nonebot.dev/store"><img src="https://github.com/A-kirami/nonebot-plugin-template/blob/resources/nbp_logo.png" width="180" height="180" alt="NoneBotPluginLogo"></a>
  <br>
  <p><img src="https://github.com/A-kirami/nonebot-plugin-template/blob/resources/NoneBotPlugin.svg" width="240" alt="NoneBotPluginText"></p>
</div>

<div align="center">

# nonebot-plugin-llm-plugins-call
</div>

# 介绍
- 通过LLM结合语境调用已安装的nonebot插件,实现更拟人和自然机器人聊天风格
- 参考LLM中的function_call的实现思路，借助LLM分析用户自然语言和已导入的nonebot插件的metadata，分析自然语言中是否含有插件调用需求，决定是否调用和应该调用哪个插件，根据自然语言构造参数触发对应插件
- 希望能解决的问题:插件装多之后或者某些插件触发命令过于繁琐增加普通用户的使用难度
- 本插件仍在开发测试中,prompt还有很大的优化空间
- **根据语境调用插件的准确性和成功调用受该插件的metadata中的description和usage编写质量影响(详细程度和易于理解度),没有metadata的插件无法通过本插件调用**
- **支持对已安装插件的metadata进行添加或修改，解决插件描述和用法文档不详细或缺失导致根据语境调用该插件的准确率**


# 效果
<img src="demo1.jpg" width="40%">
<img src="demo2.jpg" width="40%">
<img src="demo3.jpg" width="40%">
<img src="demo4.jpg" width="40%">


# 安装

* 手动安装
  ```
  git clone https://github.com/Alpaca4610/nonebot_plugin_llm_plugins_call.git
  ```

  下载完成后在bot项目的pyproject.toml文件手动添加插件：

  ```
  plugin_dirs = ["xxxxxx","xxxxxx",......,"下载完成的插件路径/nonebot-plugin-llm-plugins-call]
  ```

* 使用 pip
  ```
  pip install nonebot-plugin-llm-plugins-call
  ```

* nonebot商店自动安装
  ```
  nb plugin install nonebot-plugin-llm-plugins-call
  ```

# 配置文件

在Bot根目录下的.env文件中追加如下内容：
## 必填内容：
```
plugins_call_key = ""  # API的KEY
plugins_call_api_url = ""  # LLM的API地址
plugins_call_llm: = "Qwen/QwQ-32B" # 用于选择调用插件的LLM,需要支持tools_call

```

## 可选内容（嫌麻烦可以不看）：
```
plugins_call_blacklist = ["nonebot_plugin_xxxx","plugins.xxx"]  # 不想使用plugins_call调用的插件黑名单,填入插件模块名,"plugins.xxx"代表手动安装在机器人目录/plugins/xxx目录的插件
```

## 修改插件metadata为自定义内容

```
plugins_call_metadata_file = ""  # 自定义metadata的文件的绝对路径
```

- 有些插件的功能不错，但metadata写的不是很全易理解或者缺失metadata。可以自己为指定插件编写metadata中的description和usage部分，提高根据语境调用插件的准确性和成功率。
- 本插件会优先读取自定义文件中的metadata，自定义文件中没有指定的插件则读取开发者编写的默认metadata
- 自定义metadata的文件格式为yaml，[示例](example.yaml)如下：

```yaml

# 多行自定义内容格式示例
- module_name: "plugins.pgsh"  # 填写插件的module name，这个范例代表Bot文件夹下plugins目录中手动安装的文件夹名字为pgsh的插件
  description: |
    北京邮电大学本部和沙河校区空闲洗衣机查询
  usage: |
    本部洗衣————查看本部空闲洗衣机
    本部洗衣机 学X楼X层—————查看本部指定楼层洗衣机状态
    本部洗衣机提醒 学X楼X层————设置洗衣机空闲提醒
    雁北洗衣机————查看沙河雁北空闲洗衣机
    雁南洗衣机————查看沙河雁南空闲洗衣机


# 单行自定义内容格式示例
- module_name: "nonebot_plugin_xxxx" # 填写插件的module name，通过nb安装的直接填入module name即可
  description: 北京邮电大学本部和沙河校区空闲洗衣机查询
  usage: 本部洗衣————查看本部空闲洗衣机，本部洗衣机 学X楼X层—————查看本部指定楼层洗衣机状态，本部洗衣机提醒 学X楼X层————设置洗衣机空闲提醒，雁北洗衣机————查看沙河雁北空闲洗衣机，雁南洗衣机————查看沙河雁南空闲洗衣机

```

# 使用方法
- @机器人使用

