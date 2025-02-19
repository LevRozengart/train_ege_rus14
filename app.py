from fastapi import FastAPI
from pydantic import BaseModel
from enum import Enum
import random
import json


app = FastAPI()

class SDrop(str, Enum):
    slitno = "Слитно"
    razdelno = "Раздельно"


@app.get("/word")
async def get_word():
    with open("bd.json", encoding="utf-8") as file:
        json_lst = json.load(file)
    n = random.randint(0, 1)
    n_word = random.randint(0, len(json_lst[n][str(n)]) - 1)
    current_word = json_lst[n][str(n)][n_word]
    with open("temp.json", "w", encoding="utf-8") as file:
        json.dump({"word": current_word, "right_var": n}, file, indent=2, ensure_ascii=False)
    return {"word": current_word}

@app.get("/task")
async def main_task(answer: SDrop):
    model_ans = {"Слитно": 0, "Раздельно": 1}
    naob = {0: "Слитно", 1: "Раздельно"}
    with open("temp.json", encoding="utf-8") as file:
        data_word = json.load(file)
    right_var = data_word["right_var"]
    word = data_word["word"]
    user_ans = model_ans[answer]
    if user_ans == right_var:
        return {"message": "Верно!"}
    else:
        return {"message": f"Неверно, слово пишется {naob[right_var]}"}