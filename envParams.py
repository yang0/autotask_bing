try:
    from autotask.pluginEnvParams import EnvParam, register_env_params
except:
    from .stub import EnvParam, register_env_params



@register_env_params
class ENV_PARAMS:
    """环境参数"""
    BING_API_KEY = EnvParam(
        value="",  # 环境变量名
        description="Bing Search API Key"  # 描述
    )