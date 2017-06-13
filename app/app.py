from flask import Flask
from app import config
from app.views import UserReg, GetCusView, FilterNameView, FilterEtcView, AwesomeView

app = Flask(__name__)
app.config.update(config.dev_config)


from app.views import hello, gen_password

app.add_url_rule('/index', view_func=hello)
app.add_url_rule('/', view_func=hello)

app.add_url_rule(
    '/gen-pass', 
    view_func=gen_password,
    methods=["GET", "POST"]
    )

app.add_url_rule(
    '/reg-user', 
    view_func=UserReg.as_view("registration")
    )

app.add_url_rule(
    "/get-cust",
    view_func=GetCusView.as_view("get-cust")
    )

app.add_url_rule(
    "/filter_by_name",
    view_func=FilterNameView.as_view("filer_by_name")
    )

app.add_url_rule(
    "/filter",
    view_func=FilterEtcView.as_view("filer")
    )

app.add_url_rule(
    "/awe_filter",
    view_func=AwesomeView.as_view("awe_filter")
    )