import jinja2

# The core component of Jinja
env = jinja2.Environment()
#  load the string "Hello, {{ name }}!" as a template
template = env.from_string("Hello, {{name}}!")

# can provide a dictionary or keyword arguments as context. 
template.render(name="Ken")








# old code
# env = Environment(loader=PackageLoader('app'), 
#                   auto_reload=select_autoescape())

# template = env.get_template('template.html')


# html = template.render(navigation=navigation, welcome="Hello", 
#                        first_name=input("What is your name?\n"))




# # Printing the html variable.
# print(html)