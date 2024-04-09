from selenium_dolphin import DolphinAPI
from selenium_dolphin import DolphinAPI

api = DolphinAPI(api_key='Your_API_Key')
fingerprint = api.generate_fingerprint(platform='windows', browser_version='160')
profile_name = 'Facebook'
data = api.fingerprint_to_profile(name=profile_name, fingerprint=fingerprint)
response = api.create_profile(data)
if 'browserProfileId' in response:
    profile_id = response['browserProfileId']
    print("Profile ID:", profile_id)
else:
    print("Failed to create profile.")

api = DolphinAPI(
    api_key='eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiIxIiwianRpIjoiZjRkYzY2M2FmZTllZjE1MWRkMzBmY2NlMjQwNzNlZmQ4ZmNjMGMxMDNiMDQ2MWQ0ZDlkMDE4NDU0MTY4NWZmOWQyZmQ0MGUwMmUzYjlmYjEiLCJpYXQiOjE3MTIxNDAxODAuMzA0NDY5LCJuYmYiOjE3MTIxNDAxODAuMzA0NDcyLCJleHAiOjE3MTQ3MzIxODAuMjkwNTUsInN1YiI6IjMyNTYzNDAiLCJzY29wZXMiOltdfQ.CmrvkvS5-oL8Jh2dfkeVHHNDlIAY23ZhkoW067ZAzSlkCp18dnRQMYNMQW0j3FOmy6ED-NJ5Kt776wpoZbYdG0Cbcr948BDJ72-ZmxFCchueenjxkHhg4Xxudk3Kycx8opTHONK-mbCRmGsbWgoHtrkD3DvPu-Z3mLP2hbVnUQRBzXMqMIjUDMZZKRI4VHCvzbsP8QQxkQdz8M6m0ilTtVeMUVIikEPogzjqrIK9NQwfzWCFsUcOxDpqpp8ca8xjMkv68d9szxGNe2d65iqzweL_EHsdL4cLBOz9bf3nX8NhvHwPrN6zg93KZo8pYh1t6lWiGsfAHI_ohdX3J4g3IfaXSbUsEvLV9pYm752AAgKQk6RRNe6N18FeVKAue4L5OYHxNNr0M80AQxnJq5R_UZhBq7QNdR5os2Cs3dlWu4YNbHxKQkUBYv6gLTKh4Q6FleeRcm7goNEfanmPmjYybtDJsoYKlAZd9Y-9DgqgXhyL21f4my6TwCn8lxDZZPWw_BuYVy4IYmLNP0WVvA4BYa-sZS4ZkTw_wEftAbu2Uen80cKexaNU4BUEjhlGqjdNw6ROYupSy72ovxB4D6qZGUnLamij0b8UNsTbSFEZYLmtfIcSshjVnPnzHa-VBdB7B_6sGytss_7W_vWnSqmGlHSk2mpSu4HedpWHmMhIK8U')
# Generate a fingerprint
fingerprint = api.generate_fingerprint(platform='windows', browser_version='160')

# Create a new profile with the generated fingerprint
profile_name = 'Facebook'
data = api.fingerprint_to_profile(name=profile_name, fingerprint=fingerprint)
response = api.create_profile(data)

# Get the profile ID if creation was successful
if 'browserProfileId' in response:
    profile_id = response['browserProfileId']
    print("Profile ID:", profile_id)
else:
    print("Failed to create profile.")
