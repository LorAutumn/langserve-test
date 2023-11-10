# langserve-test

## Installation

Create an venv with

```bash
python3 -m venv {{venv_name}}
```

Install the LangChain CLI if you haven't yet

```bash
pip install -U langchain-cli
```

Activate the venv with

```bash
source {{venv_name}}/bin/activate
```

Install requirements in requirements.txt

```bash
pip install -r requirements.txt
```

## Environment Setup

Copy the .env.dev file and set the `OPENAI_API_KEY` environment variable to access the OpenAI models.

## Run the app

Run the backend (make shure to activate venv in terminal first):

```shell
langchain serve
```

This will start the FastAPI app with a server is running locally at
[http://localhost:8000](http://localhost:8000)

We can see all templates at [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
We can access the playground at [http://127.0.0.1:8000/pirate-speak/playground](http://127.0.0.1:8000/pirate-speak/playground)

Run the frontend

from folder frontend (make shure to activate venv in terminal first):

```shell
streamlit run remote-bot.py
```
