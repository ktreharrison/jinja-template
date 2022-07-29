import random

from faker import Faker
from jinja2 import Environment, FileSystemLoader

fake = Faker()

max_score = 100
test_name = "Python Challenge"
students = [{"name":fake.first_name(), "score": random.randint(0, 100)} for _ in range(25)]


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
        # print(f"... wrote {filename}")
        
print("Template rendering complete!")