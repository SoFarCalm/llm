import os
import sys
from dotenv import load_dotenv
from google import genai

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)


def main():

    verbose = False
    
    if len(sys.argv) < 2:
        print('Please provide a prompt...')
        sys.exit(1)
    
    if "--verbose" in sys.argv:
        verbose = True
    
    user_prompt = sys.argv[1]
    
    messages = [genai.types.Content(role="user", parts=[genai.types.Part(text=user_prompt)]),]

    response = client.models.generate_content(model='gemini-2.0-flash-001', contents=messages)

    print(f"\n{response.text}")

    if verbose:
        print(f"User prompt: {user_prompt}")
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")


if __name__ == "__main__":
    main()
