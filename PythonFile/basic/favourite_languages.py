favourite_languages = dict({'ram': ['C++'], 'sita': ['java'], 'hari': ['python'], 'rita': ['html']})
favourite_languages['sangamita'] = ['ASP', 'c++']
favourite_languages['sabin'] = ['JSP', 'Java', 'Html']

for name,languages in favourite_languages.items():
    print(f"Name:: {name} \nThe languages you like are:: ")
    for language in languages:
        print(f"== {language.lower()}")

'''
for key, value in favourite_languages.items():
    print(f"\n{key} like {value} language")


keywords = {'List': "[1,2,3,4,5]", 'if else': "if a<b: else: ", 'Dictionary': "{color: green, point:12}"}
for key, value in keywords.items():
    print(f"\n{key} means {value}")

for name in favourite_languages.keys():
    print(f"The name of person is {name}")

for name in favourite_languages.values():
    print(f"The favourites languages are {name}")

friends = ['sita','rita']
for name in favourite_languages.keys():
    print(f"Hello {name.title()}")

    if name in friends:
        language = favourite_languages[name].title()
        print(f"You are so special {name} as you like {language}")
'''