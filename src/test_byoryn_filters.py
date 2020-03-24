from jinja2 import Environment, FileSystemLoader
import pandas as pd
 

data1 = pd.read_excel('/home/troyee/byoryn/jinja/src/Full_Panel_v1.xlsx', dtype=str)
# data = [['H1', 'FFFFFF'],['H2', 'DDDD'],['H3','KKKKK'],['H4','OOOO'],['H5','UUUU']]
env = Environment(loader=FileSystemLoader('./'))
jinja_template = env.get_template('test.html')
with open('o.html', 'w+', encoding='utf-8') as fout:
    html_content = jinja_template.render(data=data1)
    fout.write(html_content)