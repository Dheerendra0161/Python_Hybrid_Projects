from faker import Faker
import random


def generate_age_data(relation):
    fake = Faker()

    if relation == "self":
        # Generate age between 21 and 99
        # age = fake.random_int(min=21, max=99)
        self_age_list = [21, 22, 23, 24, 25, 26, 28, 30, 31, 33, 32, 35, 38, 40]
        return random.choice(self_age_list)

    elif relation == "spouse":
        # Generate age between 18 and 99
        # age = fake.random_int(min=18, max=99)
        spouse_age_list = [23, 24, 27, 29, 31, 34, 36, 39]
        return random.choice(spouse_age_list)

    elif relation == "son":
        # Generate age in months from below 3 months to 11 months
        age_range_months = ["3 months", "4 months", "5 months", "6 months",
                            "7 months", "8 months", "9 months", "10 months", "11 months"]  # "Below 3 months",
        age_in_months = random.choice(age_range_months)

        # Son age limit 1 year to 30 years
        age_in_years = fake.random_int(min=1, max=30)

        # Return son age as a list with age in months and years
        age_s_list = [age_in_months]  # age_in_years, ]
        age_son = random.choice(age_s_list)
        return age_son

    elif relation == "daughter":
        # Generate age in months from below 3 months to 11 months
        age_range_months = ["3 months", "4 months", "5 months", "6 months",
                            "7 months", "8 months", "9 months", "10 months", "11 months"]  # "Below 3 months",
        age_in_months = random.choice(age_range_months)

        # Daughter age limit 1 year to 30 years
        age_in_years = fake.random_int(min=1, max=30)

        # Return daughter age as a list with age in months and years
        age_d_list = [age_in_months]  # age_in_years, ]
        age_daughter = random.choice(age_d_list)
        return age_daughter

    elif relation == "father" or relation == "mother":
        # Generate age between 36 and 99
        # age = fake.random_int(min=36, max=99)
        father_age_list = [58, 60, 65, 68, 62, 59, 78, 87, 79, 80, 81, 82, 83, 84, 85, 86, 90, 95, 99, 96]
        return random.choice(father_age_list)

    else:
        raise ValueError("Invalid relation specified.")


# Usage:
self_age = generate_age_data("self")
print("Self Age:", self_age)

spouse_age = generate_age_data("spouse")
print("Spouse Age:", spouse_age)

son_age_list = generate_age_data("son")
print("Son Age:", son_age_list)

daughter_age_list = generate_age_data("daughter")
print("Daughter Age:", daughter_age_list)

father_age = generate_age_data("father")
print("Father Age:", father_age)

mother_age = generate_age_data("mother")
print("Mother Age:", mother_age)
