import os
def get_files_info(working_directory, directory="."):
    abs_working = os.path.abspath(working_directory)
    abs_target = os.path.abspath(os.path.join(working_directory, directory))

    allowed = (abs_target == abs_working) or abs_target.startswith(abs_working + os.sep)
    if not allowed:
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    elif not os.path.isdir(abs_target):
        return f'Error: "{directory}" is not a directory'
    
# python
    lines = []
    try:
        for name in os.listdir(abs_target):
            full = os.path.join(abs_target, name)
            size = os.path.getsize(full)
            is_dir = os.path.isdir(full)
            lines.append(f"- {name}: file_size={size} bytes, is_dir={is_dir}")
        return "\n".join(lines)
    except Exception as e:
       return f"Error: {e}"
    
