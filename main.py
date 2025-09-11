import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types


def main():
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)

    args = sys.argv[1:]

    if not args:
        print("Error: Prompt not provided. Please try again.")
        print(f"Usage: uv python {sys.argv[0]} <your prompt here>")
        sys.exit(1)

    prompt = " ".join(args)
    print(prompt + "\n" + len(prompt) * "-" + "\n")

    response = client.models.generate_content(
        model='gemini-2.0-flash-001', contents=prompt)


    print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
    print(f"Response tokens: {response.usage_metadata.candidates_token_count}\n")
    print("Response:")
    print(response.text)

if __name__ == "__main__":
    main()