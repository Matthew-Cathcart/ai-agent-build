import sys
import os
from google import genai
from google.genai import types
from dotenv import load_dotenv


def main():
    load_dotenv()

    #This part is the users message (For now probably)
    args = sys.argv[1:]
    if len(args) == 1:
        print("No text input for the AI")
        exit(1)

    #user_prompt = " ".join(args)
    messages = [
        types.Content(role="user", parts=[types.Part(text=args[0])]),
    ]

    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)
    response = client.models.generate_content(
        model="gemini-2.0-flash-001",
        contents=messages ,
    )

    if "--verbose" in args[1:]:
        print("User prompt:", args[0])
        print("Prompt tokens:", response.usage_metadata.prompt_token_count)
        print("Response tokens:", response.usage_metadata.candidates_token_count)
    print("Response:")
    print(response.text)


if __name__ == "__main__":
    main()