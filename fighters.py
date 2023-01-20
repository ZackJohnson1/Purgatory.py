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
    """This function creates a dictionary to store list of ages"""
    ages_list = []
    for i in fighters:
        ages_list.append(i.get_age())
    mean = statistics.mean(ages_list)
    median = statistics.median(ages_list)
    mode = statistics.mode(ages_list)
    mmm = (mean, median, mode)
    return mmm

#Testing

p1 = Fighter("Kamaru Usman", 34, "Welterweight", "Nigeria")
p2 = Fighter("Conor McGregor", 32, "Lightweight", "Ireland")
p3 = Fighter("Khabib Nurmagomedov", 35, "Lightweight", "Russia")
p4 = Fighter("Sean O'Malley", 25, "Bantamweight", "United States")

fighter_list = [p1, p2, p3, p4]
print(age_stats(fighter_list)) # should print a tuple of three values