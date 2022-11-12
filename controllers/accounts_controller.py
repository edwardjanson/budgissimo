from flask import Blueprint, Flask, redirect, render_template, request
import repositories.account_repository as account_repository
import repositories.currency_repository as currency_repository


accounts_blueprint = Blueprint("accounts", __name__)


@accounts_blueprint.route("/account/")
def account():
    account = account_repository.select(1)
    return render_template("accounts/index.html", account=account)


@accounts_blueprint.route("/account/edit")
def edit_account():
    account = account_repository.select(1)
    currencies = currency_repository.select_all()
    return render_template('accounts/edit.html', account=account, currencies=currencies)


@accounts_blueprint.route("/account/edit", methods=["POST"])
def update_account():
    currency_id = request.form["currency_id"]
    currency = currency_repository.select(currency_id)
    account = account_repository.select(1)
    account.update_currency(currency)
    account_repository.update(account)
    return redirect("/account/")


@accounts_blueprint.route("/account/delete", methods=["POST"])
def delete_account():
    account_repository.delete(1)
    return redirect("/")