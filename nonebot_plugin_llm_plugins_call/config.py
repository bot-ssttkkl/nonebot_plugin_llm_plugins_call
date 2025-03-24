from pydantic import BaseModel
from typing import Optional, List

class Config(BaseModel):
    plugins_call_key: Optional[str] = ""  # API的KEY
    plugins_call_api_url: Optional[str] = ""  # LLM的API地址
    plugins_call_llm: Optional[str] = "Qwen/QwQ-32B" # 用于选择调用插件的LLM,需要支持tools_call
    plugins_call_blacklist: List[str] = [""]  # 不想使用plugins_call调用的插件黑名单,填入插件模块名
    plugins_call_metadata_file: str = "" # 自定义metadata文件绝对路径
    
class ConfigError(Exception):
    pass