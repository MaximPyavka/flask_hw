from flask import render_template, request, abort, jsonify
from flask.views import MethodView
from app.db_utils.create_db import connect_db

from app.utils import randomword


def hello():
    return render_template("index.html")


def gen_password():
    n = request.args.get(n)
    print(n)
    if n and n.isdigit() and int(n) > 10:
        n = int(n)
    else:
        abort(400)

    context = {
        "password": randomword(n),
        "title": "Generate Password",
    }
    return render_template("/gen-pass.html",
                           data=context)


class UserReg(MethodView):
    def get(self):
        return render_template("/reg-user.html")

    def post(self):
        form = request.form

        data = {
            "login": form["login"],
            "password": form["password"]
        }

        # print(login, password)
        # print(form)
        return render_template('/reg-user.html', data=data)


class GetCusView(MethodView):
    def get(self):
        conn = connect_db()
        query = "SELECT * FROM Customers"
        # print(request.args)
        # print(request.args.get("argfjdkg","1"*7))
        limit = request.args.get("limit")
        if limit and limit.isdigit():
            tab = conn.execute("{} LIMIT {}".format(query, limit))
        else:
            tab = conn.execute(query)
        tab = [i for i in tab]
        conn.close()
        return render_template("customers.html", data=tab)


class FilterNameView(MethodView):
    def get(self):
        conn = connect_db()
        # req = request.args
        # print(req)
        query = "SELECT * FROM Customers WHERE FirstName LIKE '{start}%{temp}%{end}'"
        points = {"start": request.args.get("start", ""),
                  "end": request.args.get("end", ""),
                  "temp": request.args.get("temp", "")
                  }
        tab = conn.execute(query.format(**points))
        tabs = [i for i in tab]
        print(tabs)
        conn.close()
        return render_template("customers.html", data=tabs)


class FilterEtcView(MethodView):
    def get(self):
        return render_template("filter.html")

    def post(self):
        conn = connect_db()
        form = request.form
        print(form)
        query = "SELECT * FROM Customers WHERE Company LIKE '{company}'" \
                " AND City LIKE '{city}'" \
                " AND State LIKE '{state}'"
        tab = conn.execute(query.format(**form))
        tabs = [i for i in tab]
        conn.close()
        return render_template("filter.html", data=tabs)


class AwesomeView(MethodView):
    def get(self):
        return render_template("awesome_filter.html")

    def post(self):
        conn = connect_db()
        form = request.form
        order = [form["1st_field"], form["2nd_field"], form["3rd_field"]]
        print(form)
        query = "SELECT * FROM Customers ORDER BY {} {}"
        tab = conn.execute(query.format(",".join(order), form['ordering_way']))
        tabs = [i for i in tab]
        conn.close()
        return jsonify(tabs)
        # return render_template("awesome_filter.html", data=tabs)
