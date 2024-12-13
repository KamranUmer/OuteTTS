from fastapi import FastAPI
# from model import model_config_setting
from languages import Language_Type
from tunes import TuneType
from model_config import model_config_setting


app = FastAPI()


def select_tune(languagetype):
    if languagetype == Language_Type["english"]:
        return TuneType.get_tune_e()

    elif languagetype == Language_Type["chaines"]:
        return TuneType.get_tune_chi()

    elif languagetype == Language_Type["japnies"]:
        return TuneType.get_tune_jp()

    elif languagetype == Language_Type["korean"]:
        return TuneType.get_tune_ko()



@app.get("/languages/{language}")
async def language_fnc(languagetype:Language_Type, inputtext : str):
    if languagetype == Language_Type["english"]:
        tune = select_tune("english")
        output = model_config_setting("en", tune[0], inputtext)
        return output
    
    elif languagetype == Language_Type["chaines"]:
        tune = select_tune("chaines")
        output = model_config_setting("zh", tune[0], inputtext)
        return output
    
    elif languagetype == Language_Type["japnies"]:
        tune = select_tune("japnies")
        output = model_config_setting("ja", tune[0], inputtext)
        return output
        
    elif languagetype == Language_Type["korean"]:
        tune = select_tune("korean")
        output = model_config_setting("ko", tune[0], inputtext)
        return output
    
    else:
        return{"error ": "Tune type is not supported"}



# @app.get("/oute_model/{model}")
# async def model_fnc():
#         model = model_config_setting()

#         return 