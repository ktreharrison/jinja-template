from jinja2 import Environment, FileSystemLoader

max_score = 100
test_name = "Python Challenge"
students = [
    {"name": "Kenneth", 'score':100},
    {"name": 'Travis', 'score': 87},
    {"name": "Eugenio", 'score':99},
    {'name': 'Jess', 'score': 45},
    {'name': "David", 'score': 40},
    ]
# A Jinja environment with FileSystemLoader points to the folder of your templates.
env = Environment(loader=FileSystemLoader('templates/'))
template = env.get_template('message.txt')

for student in students:
    filename = f"output/message_{student['name'].lower()}.txt"
    content = template.render(student,
                              max_score=max_score,
                              test_name=test_name
    )
    with open(filename, mode='w') as message:
        message.write(content)
        print(f"... wrote {filename}")
        
print("Template rendering complete!")