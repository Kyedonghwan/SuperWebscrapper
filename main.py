from flask import Flask, render_template, request


app = Flask("SuperScrapper")


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/report")
def report():
    word = request.args.get('word')
    return render_template("report.html", searching_by=word)


app.run()


"""
from indeed import get_jobs as get_indeed_jobs
from stackoverflow import get_jobs as get_stackoverflow_jobs
from save import save_to_file

stackoverflow_jobs = get_stackoverflow_jobs()
indeed_jobs = get_indeed_jobs()


jobs = indeed_jobs + stackoverflow_jobs
save_to_file(jobs)
"""
