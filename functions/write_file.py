import os
from google.genai import types
def write_file(working_directory, file_path, content):
    abs_working_dir = os.path.abspath(working_directory)
    path = os.path.abspath(os.path.join(working_directory,file_path))
    
    if not path.startswith(abs_working_dir):
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
    
    try:
        with open(path,'w') as f:
            f.write(content)
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except Exception as e:
        return f'Error: {e}'
    
schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description=f"Create the file and append the content to it, if the files exisit it will get override by contect",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file_path is the path to the file, relative to the working directory. It is compulsory",
            ),
            "content":types.Schema(
                type=types.Type.STRING,
                description="The content is the data that is overridden or insert into the file"
            )
        },
        required=['file_path','content']
    ),
)  