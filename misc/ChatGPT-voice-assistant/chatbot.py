import os
import datetime
import openai

# setup the API key
home_dir = os.path.expanduser("~")
openai.api_key_path = os.path.join(home_dir, 'OPENAI_API_KEY')

today_date = datetime.date.today()


def get_response(prompt):
    response = openai.ChatCompletion.create(
      model="gpt-3.5-turbo",
      messages=[
            {
                "role": "system",
                "content": (
                    f'You are ChatGPT, a large language model trained by OpenAI. '
                    f'Answer as concisely as possible. Current date: {today_date}.'
                )
            },
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response