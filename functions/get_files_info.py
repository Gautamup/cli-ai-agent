import os
from google.genai import types
def get_files_info(working_directory,directory="."):
    absPath = os.path.abspath(working_directory)
    path = os.path.abspath(os.path.join(working_directory, directory))
    
    if not path.startswith(absPath):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    
    if not os.path.isdir(path):
        return f'Error: "{directory}" is not a directory'
    
    try:
        res = ""
        for file in os.listdir(path=path):
                temp = f" - {file}: file_size={os.path.getsize(os.path.join(path,file))}, is_dir={os.path.isdir(file)} \n"
                res += temp
        return res
    except Exception as e:
        return f"Error: {e}"

schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
        },
    ),
)
    
    