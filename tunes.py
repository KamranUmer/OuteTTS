from enum import Enum

# Tune types 
class TuneType(str, Enum):
    male_1 = "male_1"
    male_2 = "male_2"
    male_3 = "male_3"
    male_4 = "male_4"
    female_1 = "female_1"
    female_2 = "female_2"
    female_3 = "female_3"

    @classmethod
    def get_tune_e(cls):
        return [cls.male_1, cls.male_2, cls.male_3, cls.male_4, cls.female_1, cls.female_2]

    @classmethod
    def get_tune_chi(cls):
        return [cls.male_1, cls.male_2, cls.female_1, cls.female_2]

    @classmethod
    def get_tune_jp(cls):
        return [cls.male_1, cls.female_1, cls.female_2, cls.female_3]

    @classmethod
    def get_tune_ko(cls):
        return [cls.male_1, cls.male_2, cls.female_1, cls.female_2]
