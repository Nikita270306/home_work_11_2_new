from flask import Flask, render_template
from utils import *

app = Flask(__name__)


@app.route('/')
def main_page():
    full_candidates = load_candidates_from_json('candidates.json')
    return render_template('list.html', full_candidates=full_candidates)


@app.route('/candidate/<int:x>')
def personal_page(x):
    candidate_info = get_candidate(x)
    return render_template('single.html', candidate_info=candidate_info)


@app.route('/search/<candidate_name>')
def name_page(candidate_name):
    name_info = get_candidates_by_name(candidate_name)
    lenght = len(name_info)
    return render_template('search.html', name_info=name_info, lenght=lenght)


@app.route('/skill/<skill_name>')
def skill_page(skill_name):
    skill_info = get_candidates_by_skill(skill_name)
    skill_name_ = skill_name
    skill_name_l = len(get_candidates_by_skill(skill_name))
    return render_template('skill.html', skill_info=skill_info, skill_name_=skill_name_, skill_name_l=skill_name_l)


app.run()
