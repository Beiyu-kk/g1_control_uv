import os

def print_tree(root="."):
    """
    优雅地打印项目目录结构。
    - 忽略以 . 或 _ 开头的文件夹。
    - 先打印文件夹，再打印文件。
    - 使用树状缩进表示结构。
    """
    root = os.path.abspath(root)
    print(os.path.basename(root) + "/")  # 打印根目录名
    _print_tree(root, "", True)

def _print_tree(dirpath, prefix, is_last):
    items = os.listdir(dirpath)
    
    # 只收集不以 . 或 _ 开头的文件夹
    dirs = [
        item for item in items
        if os.path.isdir(os.path.join(dirpath, item)) and not (item.startswith('.') or item.startswith('_'))
    ]
    
    # 收集所有文件（不忽略以 . 或 _ 开头的文件）
    files = [
        item for item in items
        if os.path.isfile(os.path.join(dirpath, item))
    ]
    
    # 按字母顺序排序
    dirs.sort()
    files.sort()
    
    # 先文件夹，后文件
    all_items = dirs + files
    total = len(all_items)
    
    for i, item in enumerate(all_items):
        is_last_item = (i == total - 1)
        connector = "└── " if is_last_item else "├── "
        
        if item in dirs:
            # 打印文件夹
            print(prefix + connector + item + "/")
            new_prefix = prefix + ("    " if is_last_item else "│   ")
            _print_tree(os.path.join(dirpath, item), new_prefix, is_last_item)
        else:
            # 打印文件
            print(prefix + connector + item)

# 使用示例
if __name__ == "__main__":
    print_tree()  # 从当前目录开始打印