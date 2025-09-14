import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types


def main():
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)

    verbose = "--verbose" in sys.argv
    args = []
    for arg in sys.argv[1:]:
        if not arg.startswith("--"):
            args.append(arg)

    if not args:
        print("Error: Prompt not provided. Please try again.")
        print('\nUsage: python main.py "your prompt here" [--verbose]')
        print(f"Usage: uv python {sys.argv[0]} <your prompt here>")
        sys.exit(1)

    prompt = " ".join(args)
    print(prompt + "\n" + len(prompt) * "-" + "\n")

    if verbose:
        print(f"User prompt: {prompt}")
    

    messages = [
    types.Content(role="user", parts=[types.Part(text=prompt)]),
    ]

    generate_content(client, messages, verbose)

    
def generate_content(client, messages, verbose):
    response = client.models.generate_content(
        model="gemini-2.0-flash-001",
        contents=messages,
    )

    prompt_tokens = response.usage_metadata.prompt_token_count
    response_tokens = response.usage_metadata.candidates_token_count

    if verbose:
        print(f"Prompt tokens: {prompt_tokens}")
        print(f"Response tokens: {response_tokens}")

    print("Response:")
    print(response.text)

if __name__ == "__main__":
    main()