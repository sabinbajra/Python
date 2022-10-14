
users = {
    'Ram': {'first': 'Ram', 'mid': 'Muni', 'last': 'Shakya', 'age': 35},
    'Sabin': {'first': 'Sabin', 'mid': '', 'last': 'Napit', 'age': 37},
    'Chudamani': {'first': 'Chudamani', 'mid': 'Harsa', 'last': 'Maharjan', 'age': 25},
         }

for user, info in users.items():
    print(f"Username :: {user}")
    print(f"Details\nFirstname :: {info['first'].title()}"
          f"\nMiddle name :: {info['mid'].title()}"
          f"\nLastname :: {info['last'].title()}\n")
