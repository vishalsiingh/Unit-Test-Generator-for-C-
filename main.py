import os
import yaml
import subprocess
from dotenv import load_dotenv
from openai import OpenAI

# Load API key
load_dotenv()
client = OpenAI()  # Uses OPENAI_API_KEY from .env

def load_prompt(path):
    with open(path, 'r') as f:
        return yaml.safe_load(f)['instruction']

def call_gpt(prompt, model="gpt-3.5-turbo"):
    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": "You are a helpful assistant that writes C++ unit tests using Google Test."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.4
    )
    return response.choices[0].message.content

def build_and_run_tests(test_path, output_exec="test_exec"):
    print(f"🔧 Building test: {test_path}")

    build_cmd = [
        "g++",
        test_path,
        "googletest/googletest/src/gtest-all.cc",
        "-Igoogletest/googletest/include",
        "-Igoogletest/googletest",
        "-pthread",
        "-o",
        output_exec
    ]

    result = subprocess.run(build_cmd, capture_output=True, text=True)

    if result.returncode != 0:
        print("❌ Build failed.")
        print(result.stderr)

        with open("build_error.txt", "w") as f:
            f.write(result.stderr)

        return False
    else:
        print("✅ Build succeeded. Running tests...\n")
        subprocess.run([f"./{output_exec}"])  # Run compiled test binary
        return True

def main():
    input_path = "cpp_project/EmployeeManager.cpp"
    output_path = "tests/test_EmployeeManager.cpp"
    prompt_path = "prompts/generate_tests.yaml"

    # Load source and prompt
    with open(input_path, 'r') as f:
        cpp_code = f.read()

    prompt_instruction = load_prompt(prompt_path)
    full_prompt = f"{prompt_instruction}\n\n```cpp\n{cpp_code}\n```"

    # Generate test
    test_code = call_gpt(full_prompt)

    # Save generated test
    os.makedirs("tests", exist_ok=True)
    with open(output_path, 'w') as f:
        f.write(test_code)

    print(f"✅ Test file generated: {output_path}")

    # Build and run test
    build_success = build_and_run_tests(output_path)

    if not build_success:
        print("\n🧠 Next step: You could send `build_error.txt` + test file back to GPT to auto-fix.")
    else:
        print("🚀 Test execution complete.")

if __name__ == "__main__":
    main()
