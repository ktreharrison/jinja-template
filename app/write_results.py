from jinja2 import Environment, FileSystemLoader

from write_messages import max_score, students, test_name

env = Environment(loader=FileSystemLoader('templates/'))
results_template = env.get_template('results.html')
results_filename = 'output/students_results.html'


context = {
    "students": students, 
    "test_name":test_name,     
    "max_score":max_score,
}      

with open(results_filename, mode='w') as results:
    results.write(results_template.render(context))
    print(f"... wrote {results_filename}")          
    
print("Template rendering complete!")
