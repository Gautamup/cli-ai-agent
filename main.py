import os,time
from config import CALL_LIMIT
from dotenv import load_dotenv
from google import genai
from google.genai import types
import sys
from call_functions import available_function , call_function
from prompts import SYSTEM_PROMPT

        
def main():
    load_dotenv()

    api_key = os.getenv("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)

    args_len = len(sys.argv)
    if len(sys.argv) < 2:
        print("Please enter you query")
        sys.exit(1)

    # check for verbose flag
    verboseCheck = "--verbose" in sys.argv
    
    user_prompt = ""
    for i in range(args_len) or sys.argv[i].startswith("--"):
        if i == 0 or sys.argv[i].startswith('--'):
            continue            
        user_prompt += sys.argv[i] + " "

    user_prompt.strip()
    
    
    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)]),
    ]
    for itr in range(CALL_LIMIT):
        time.sleep(1)
        res = generate_content(client,messages,verboseCheck)
        if res:
            print(res)
            if "DONE" in res:
                break
        
    
def generate_content(client,messages,verboseCheck):
    
    response = client.models.generate_content(
        model='gemini-2.0-flash-001',
        contents=messages,
        config=types.GenerateContentConfig(system_instruction=SYSTEM_PROMPT,tools=[available_function])
    )
    
    for candidate in response.candidates:
        messages.append(candidate.content)
        
    if verboseCheck:
        res = {}
        res['tokens tokens'] = response.usage_metadata.prompt_token_count
        res['Response tokens'] = response.usage_metadata.candidates_token_count
        print(res)

    if not response.function_calls:
        return response.text
    
    function_responses = []
    
    for function_call_part in response.function_calls:
        function_call_result = call_function(function_call_part, verboseCheck)
        
        if (
            not function_call_result.parts
            or not function_call_result.parts[0].function_response
        ):
            raise Exception("empty function call result")
        if verboseCheck:
            print(f"-> {function_call_result.parts[0].function_response.response}")
        function_responses.append(function_call_result.parts[0])
    
        tool_response = types.Content(
            role="tool",
            parts=[function_call_result.parts[0]],
        )
        
        messages.append(tool_response)
        
    if not function_responses:
        raise Exception("no function responses generated, exiting.")
    
    if response.text and len(response.text) > 0:
        return response.text
        
if __name__ == "__main__":
   a =  main()