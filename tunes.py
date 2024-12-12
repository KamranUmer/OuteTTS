from enum import Enum

# Tune types 
class Tune_e_Type(str, Enum):
    male_1 = "male_1"
    male_2 = "male_2"
    male_3 = "male_2"
    male_4 = "male_3"
    female_1 = "female_1"
    female_2 = "female_2"

class Tune_ko_Type(str, Enum):
    male_1 = "male_1"
    male_2 = "male_2"
    female_1 = "female_1"
    female_2 = "female_2"

class Tune_jp_Type(str, Enum):
    male_1 = "male_1"
    female_1 = "female_1"
    female_2 = "female_2"
    female_3 = "female_3"

class Tune_chi_Type(str, Enum):
    male_1 = "male_1"
    male_2 = "male_2"
    female_1 = "female_1"
    female_2 = "female_2"