import json
from langchain_community.llms import Ollama


message_template = """Hi! Here's a task for you.
Below are two jsons.
One contains reviews for some app.
The second contains the processed result of the reviews as a list of specific tasks to improve the app.
You have to read all the reviews and add the missing tasks to the resulting json and print it here.

Reviews:
{{reviews}}

Result:
{{result}}
"""


def load_json(fiile):
    with open(fiile, encoding='utf8') as f:
        d = json.load(f)
        return d


def main():
    message = (message_template
               .replace("{{reviews}}", json.dumps(load_json("reviews.json"), ensure_ascii=False, indent=4))
               .replace("{{result}}", json.dumps(load_json("results.json"), ensure_ascii=False, indent=4)))

    print(message)

    llm = Ollama(model="deepseek-r1:32b")
    response = llm.invoke(message)
    print(response)


if __name__ == "__main__":
    main()
