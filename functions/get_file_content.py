import os
from google.genai import types
from config import MAX_CHAR
def get_file_content(working_directory, file_path):
    abs_working_dir = os.path.abspath(working_directory)
    path = os.path.abspath(os.path.join(working_directory,file_path))
    
    if not path.startswith(abs_working_dir):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    
    if not os.path.isfile(path=path):
        return f'Error: File not found or is not a regular file: "{file_path}"'

    try:
        with open(path,'r') as f:
            file_content_string = f.read(MAX_CHAR)
            if len(file_content_string) == MAX_CHAR:
                file_content_string += f'\n[...File "{file_path}" truncated at 10000 characters]'
            return file_content_string
    except Exception as e:
        return f"Error: {e}"
    
schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description=f"Get the content of the specified file upto {MAX_CHAR}, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file_path is the path to the file, relative to the working directory. It is compulsory",
            ),
        },
        required=['file_path']
    ),
)