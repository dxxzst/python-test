import requests
from plotly.graph_objs import Bar
from plotly import offline

# 获取github python相关的数据
url = "https://api.github.com/search/repositories?q=language:python&sort=stars"
headers = {"accept": "application/json;v=b3;q=0.9"}
r = requests.get(url, headers=headers)
response_dict = r.json()

# 项目列表
repo_dicts = response_dict["items"]

repo_names, stars, labels, repo_links = [], [], [], []
for repo_dict in repo_dicts:
    repo_names.append(repo_dict['name'])
    stars.append(repo_dict['stargazers_count'])
    owner = repo_dict['owner']['login']
    desc = repo_dict['description']
    labels.append(f"<div>{owner} <br /> {desc}</div>")
    repo_links.append(f"<a href='{repo_dict['html_url']}'>{repo_dict['name']}<a>")

# 可视化
data = [{'type': 'bar', 'x': repo_links, 'y': stars, 'hovertext': labels, 'marker': {
    'color': 'rgb(60,100,150)', 'line': {'width': 1.5, 'color': 'rgb(25,25,25)'}
}, 'opacity': 0.6}]

my_layout = {'title': "GitHub上最受欢迎的python项目", "xaxis": {"title": '项目'}, "yaxis": {"title": 'stars'}}
fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='github_python.html')
