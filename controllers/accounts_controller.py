from flask import Blueprint, redirect, render_template, request, session

import repositories.account_repository as account_repository
import repositories.platform_repository as platform_repository
import repositories.tag_repository as tag_repository
import repositories.currency_repository as currency_repository
import repositories.budget_repository as budget_repository
from models.account import Account
from models.budget import Budget

accounts_blueprint = Blueprint("accounts", __name__)


@accounts_blueprint.route("/account/")
def account():
    session.clear()
    session["account_id"] = 1
    account = account_repository.select(session["account_id"])
    platform_budgets = budget_repository.combine_platforms(account)
    return render_template("accounts/index.html", account=account, platform_budgets=platform_budgets)


@accounts_blueprint.route("/account/new")
def new_campaign():
    return render_template("accounts/new.html")


@accounts_blueprint.route("/accounts/new", methods=["POST"])
def create_campaign():
    return redirect("/account/")


@accounts_blueprint.route("/account/edit")
def edit_account():
    account = account_repository.select(session["account_id"])
    currencies = currency_repository.select_all()
    return render_template('accounts/edit.html', account=account, currencies=currencies)


@accounts_blueprint.route("/account/edit", methods=["POST"])
def update_account():
    currency_id = request.form["currency_id"]
    monthly_budget = request.form["monthly_budget"]
    amount_spent = request.form["amount_spent"]

    updated_currency = currency_repository.select(currency_id)
    account = account_repository.select(session["account_id"])
    updated_budget = Budget(monthly_budget, amount_spent, account.budget.id) # type: ignore
    budget_repository.update(updated_budget)
    updated_account = Account(updated_budget, updated_currency)
    account_repository.update(updated_account)
    return redirect("/account/")


@accounts_blueprint.route("/account/delete", methods=["POST"])
def delete_account():
    account_repository.delete(session["account_id"])
    return redirect("/")