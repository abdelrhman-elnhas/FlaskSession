from flask import Flask, render_template


master_code = Flask(__name__)

my_skills = [("HTML", 90), ("CSS", 70), ("Python", 30)]


@master_code.route("/")
def home():
    return render_template("home.html", pagetitle="Home", custom_css="home")


@master_code.route("/contact")
def contact():
    return render_template("contact.html", pagetitle="Contact")


@master_code.route("/skills")
def skills():
    return render_template("skill.html", pagetitle="skills", page_head="My Skills", skills=my_skills, custom_css="skills")


if __name__ == "__main__":
    master_code.run(debug=True, port=9000)
