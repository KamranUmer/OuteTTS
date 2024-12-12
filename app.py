from fastapi import FastAPI
# from model import model_config_setting
from languages import Language_Type
from tunes import Tune_chi_Type, Tune_e_Type, Tune_jp_Type, Tune_ko_Type
from model_config import model_config_setting


app = FastAPI()

@app.get("/model/{model_name}")
async def model_1(languagetype:Language_Type):
    if languagetype == Language_Type["english"]:
        return "english language"
    
    elif languagetype == Language_Type["chaines"]:
        return "chaines language"
    
    if languagetype == Language_Type["japnies"]:
        return "japnies language"
    
    elif languagetype == Language_Type["korean"]:
        return "korean language"