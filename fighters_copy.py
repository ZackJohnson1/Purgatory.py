import statistics

class Fighter:
    def __init__(self, name, age, division, country):
        """Initializes the parameters for the fighter class as private
        data members; these parameters include simple attributes such as the fighter's
        name, age, weight division and their country of origin"""
        self._name = name
        self._age = age
        self._division = division
        self._country = country

    def get_name(self):
        return self._name
    def get_age(self):
        return self._age
    def get_division(self):
        return self._division
    def get_country(self):
        return self._country


def age_stats (fighters):
    """This function creates a list to store list of ages"""
    ages_list = []
    for i in fighters:
        ages_list.append(i.get_age())
    mean = statistics.mean(ages_list)
    median = statistics.median(ages_list)
    mode = statistics.mode(ages_list)
    mmm = (mean, median, mode)
    return mmm

def basic_stats (countries):
    """This function creates a dictionary to store list of countries"""
    country_of_birth = []
    for i in countries:
        country_of_birth.append(i.country())
    return mmm

print()