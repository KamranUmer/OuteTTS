from fastapi import FastAPI
# from model import model_config_setting
from languages import Language_Type
from tunes import TuneType
from model_config import model_config_setting


app = FastAPI()


def select_tune(languagetype):
    if languagetype == Language_Type["english"]:
        return {"Available tunes for english ": TuneType.get_tune_e()}

    elif languagetype == Language_Type["chaines"]:
        return {"Available tunes for chaines ": TuneType.get_tune_chi()}

    elif languagetype == Language_Type["japnies"]:
        return {"Available tunes for Japnies " : TuneType.get_tune_jp()}

    elif languagetype == Language_Type["korean"]:
        return {"Available tunes for korean " : TuneType.get_tune_ko()}



@app.get("/languages/{language}")
async def language_fnc(languagetype:Language_Type):
    if languagetype == Language_Type["english"]:
        tune = select_tune("english")
        return tune
    
    elif languagetype == Language_Type["chaines"]:
        tune = select_tune("chaines")
        return tune

    elif languagetype == Language_Type["japnies"]:
        tune = select_tune("japnies")
        return tune
    
    elif languagetype == Language_Type["korean"]:
        tune = select_tune("korean")
        return tune

    else:
        return{"error ": "Tune type is not supported"}



# @app.get("/oute_model/{model}")
# async def model_fnc():
#         model = model_config_setting()

#         return 