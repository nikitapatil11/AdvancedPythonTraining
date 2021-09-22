from jinja2 import Environment, FileSystemLoader

persons = [
    {"name": "andre", "age": 21},
    {"name": "joe", "age": 23},
    {"name": "alex", "age": 21},
    {"name": "cindrella", "age": 16},
    {"name": "tom", "age": 13},
]


file_loader = FileSystemLoader("templates")
env = Environment(loader=file_loader)
template = env.get_template("minors.txt")

output = template.render(persons=persons)
print(output)
