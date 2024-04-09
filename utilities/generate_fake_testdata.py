from faker import Faker


def generate_fake_data(gender):
    fake = Faker()

    # Generate a 10-digit mobile number starting with 98, 79, or 87
    mobile_number = fake.numerify(text="9#########")

    # Ensure it starts with 98, 79, or 87
    while not (mobile_number.startswith("98") or mobile_number.startswith("79") or mobile_number.startswith("87")):
        mobile_number = fake.numerify(text="9#########")

    # Generate an age between 18 and 80
    age = fake.random_int(min=18, max=80)

    # Generate a fake email
    email = fake.email()

    # Generate a gender-specific name
    if gender == "male":
        first_name = fake.first_name_male()
        last_name = fake.last_name_male()
    elif gender == "female":
        first_name = fake.first_name_female()
        last_name = fake.last_name_female()
    else:
        raise ValueError("Invalid gender specified. Use 'male' or 'female'.")

    # Combine first name and last name
    full_name = f"{first_name} {last_name}"

    return {
        "mobile_number": mobile_number,
        "age": age,
        "email": email,
        "full_name": full_name,
        "gender": gender
    }

# male data:
# male_fake_data = generate_fake_data(gender="male")
# print("Generated Male Fake Data:")
# print("Mobile Number:", male_fake_data["mobile_number"])
# print("Age:", male_fake_data["age"])
# print("Email:", male_fake_data["email"])
# print("Full Name:", male_fake_data["full_name"])
# print("Gender:", male_fake_data["gender"])
# print()

# female data:
# female_fake_data = generate_fake_data(gender="female")
# print("Generated Female Fake Data:")
# print("Mobile Number:", female_fake_data["mobile_number"])
# print("Age:", female_fake_data["age"])
# print("Email:", female_fake_data["email"])
# print("Full Name:", female_fake_data["full_name"])
# print("Gender:", female_fake_data["gender"])
