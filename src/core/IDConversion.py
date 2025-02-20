import pandas as pd
from pathlib import Path

github_url = "https://raw.githubusercontent.com/Seeridia/fzu-learning-center-api/main/source/seatIdConversionTool.csv"

def get_space_name_by_id(id: str | int) -> str:
    """根据id获取spaceName
    Args:
        id: 座位ID (可以是字符串或整数)
    Returns:
        str: 对应的空间名称，如果未找到返回空字符串
    """
    try:
        file_path = Path(__file__).parent / 'seatIdConversionTool.csv'
        if file_path.exists():
            df = pd.read_csv(file_path)
        else:
            df = pd.read_csv(github_url)
        
        id = int(id) if isinstance(id, str) else id
        
        result = df[df['id'] == id]['spaceName']
        return result.iloc[0] if not result.empty else ''
    except Exception as e:
        print(f"Error: {e}")
        return ''

def get_id_by_space_name(space_name: str) -> str | int:
    """根据spaceName获取id
    Args:
        space_name: 空间名称
    Returns:
        str: 对应的座位ID，如果未找到返回空字符串
    """
    try:
        file_path = Path(__file__).parent / 'seatIdConversionTool.csv'
        if file_path.exists():
            df = pd.read_csv(file_path)
        else:
            df = pd.read_csv(github_url)
        
        result = df[df['spaceName'] == space_name]['id']
        return result.iloc[0] if not result.empty else ''
    except Exception as e:
        print(f"Error: {e}")
        return ''
