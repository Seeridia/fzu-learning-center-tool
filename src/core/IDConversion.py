import csv
from pathlib import Path
import urllib.request
import urllib.error

github_url = "https://raw.githubusercontent.com/Seeridia/fzu-learning-center-api/main/source/seatIdReferenceTable.csv"

def _load_data():
    """加载CSV数据
    Returns:
        list: CSV数据列表，每项包含id、spaceName和floor
    """
    try:
        file_path = Path(__file__).parent / 'seatIdReferenceTable.csv'
        if file_path.exists():
            with open(file_path, 'r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                return list(reader)
        else:
            with urllib.request.urlopen(github_url) as response:
                content = response.read().decode('utf-8').splitlines()
                reader = csv.DictReader(content)
                return list(reader)
    except urllib.error.URLError:
        return "network error"
    except Exception as e:
        print(f"Error: {e}")
        return []

def get_space_name_by_id(id: str | int) -> str:
    """根据id获取spaceName
    Args:
        id: 座位ID (可以是字符串或整数)
    Returns:
        str: 对应的空间名称，如果未找到返回空字符串
    """
    try:
        data = _load_data()
        if data == "network error":
            return "network error"
        
        id_str = str(int(id))
        for row in data:
            if row['id'] == id_str:
                return row['spaceName']
        return ''
    except Exception as e:
        print(f"Error: {e}")
        return ''

def get_id_by_space_name(space_name: str | int) -> str:
    """根据spaceName获取id
    Args:
        space_name: 空间名称，可以是字符串或整数
    Returns:
        str: 对应的座位ID，如果未找到返回空字符串
    """
    try:
        data = _load_data()
        if data == "network error":
            return "network error"
        
        space_name_str = str(space_name).lstrip('0')
        for row in data:
            if row['spaceName'].lstrip('0') == space_name_str:
                return row['id']
        return ''
    except Exception as e:
        print(f"Error: {e}")
        return ''

def get_floor_by_space_name(space_name: str | int) -> int:
    """根据spaceName获取楼层
    Args:
        space_name: 空间名称，可以是字符串或整数
    Returns:
        str: 对应的楼层，如果未找到返回空字符串
    """
    try:
        data = _load_data()
        if data == "network error":
            return "network error"
        
        space_name_str = str(space_name).lstrip('0')
        for row in data:
            if row['spaceName'].lstrip('0') == space_name_str:
                return row['floor']
        return ''
    except Exception as e:
        print(f"Error: {e}")
        return ''