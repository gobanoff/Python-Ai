import os
from openai import OpenAI
from dotenv import load_dotenv
from rich import print

load_dotenv()
# To authenticate with the model you will need to generate a personal access token (PAT) in your GitHub settings.
# Create your PAT token by following instructions here: https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens
client = OpenAI(
    base_url="https://models.inference.ai.azure.com",
    api_key=os.environ["GITHUB_TOKEN"],
)

response = client.chat.completions.create(
    messages=[
        {
            "role": "system",
            "content": "",
        },
        {
            "role": "user",
            "content": "What is the capital of Lithuania,Australia,Russia,France,Germany,England,UK,Great Britain and who is the winner of UEFA champions league?",
        },
    ],
    model="gpt-4o",
    temperature=1,
    max_tokens=4096,
    top_p=1,
)

print(response.choices[0].message.content)

"""
Here is the list of countries and their respective capitals:

1. **Lithuania** - Vilnius
2. **Australia** - Canberra
3. **Russia** - Moscow
4. **France** - Paris
5. **Germany** - Berlin
6. **England** - London
7. **United Kingdom (UK)** - London
8. **Great Britain** - London

**Note:** England, Scotland, and Wales together form Great Britain. The United Kingdom includes 
Great Britain and Northern Ireland, but the capital remains London.


### **UEFA Champions League Winner:**
who defeated Inter Milan in the final.

For information beyond 2023, let me know so I can help clarify further!



"""
