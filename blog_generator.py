import requests
import pandas as pd

# Together.ai API key"-
api_key = "[[YOUR API KEY]]"  # Replace this with actual key

def generate_blog(topic):
    url = "https://api.together.xyz/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "mistralai/Mixtral-8x7B-Instruct-v0.1",
        "messages": [
            {"role": "system", "content": "You are a blog writer for a building materials website. Write in a friendly and engaging tone."},
            {"role": "user", "content": f"Write a blog post about: {topic}"}
        ],
        "max_tokens": 500,
        "temperature": 0.7
    }

    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 200:
        result = response.json()
        return result['choices'][0]['message']['content']
    else:
        return f"❌ Error {response.status_code}: {response.text}"

def main():
    input_file = "blog_topics.xlsx"
    output_file = "blog_with_content.xlsx"

    try:
        df = pd.read_excel(input_file)
        df.rename(columns={df.columns[0]: "Topic"}, inplace=True)

        print(f"🔍 Found {len(df)} blog topics. Generating content...")

        df["Content"] = df["Topic"].apply(generate_blog)

        df.to_excel(output_file, index=False)
        print(f"✅ Done! Blog content saved to {output_file}")

    except FileNotFoundError:
        print("❌ blog_topics.xlsx not found in this folder.")
    except Exception as e:
        print(f"❌ Unexpected error: {e}")

if __name__ == "__main__":
    main()
