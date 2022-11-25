from flask import Blueprint, redirect, render_template, request

import repositories.account_repository as account_repository
import repositories.budget_repository as budget_repository
import repositories.currency_repository as currency_repository
from models.account import Account
from models.budget import Budget

accounts_blueprint = Blueprint("accounts", __name__)


@accounts_blueprint.route("/accounts")
def account():
    accounts = account_repository.select_all()
    # platform_budgets = budget_repository.combine_platforms(account)
    return render_template("accounts/index.html", accounts=accounts)


@accounts_blueprint.route("/accounts/new")
def new_campaign():
    currencies = currency_repository.select_all()
    return render_template("accounts/new.html", currencies=currencies)


@accounts_blueprint.route("/accounts/new", methods=["POST"])
def create_campaign():
    account_name = request.form["account_name"]
    currency_id = request.form["currency_id"]
    monthly_budget = float(request.form["monthly_budget"])
    amount_spent = float(request.form["amount_spent"]) if request.form["amount_spent"] else None

    currency = currency_repository.select(currency_id)
    budget = Budget(monthly_budget, amount_spent)
    new_budget = budget_repository.save(budget)
    new_account = Account(account_name, new_budget, currency)
    account_repository.save(new_account)
    return redirect("/accounts")


@accounts_blueprint.route("/accounts/edit")
def edit_account():
    accounts = account_repository.select_all()
    currencies = currency_repository.select_all()
    return render_template('accounts/edit.html', accounts=accounts, currencies=currencies)


@accounts_blueprint.route("/accounts/edit", methods=["POST"])
def update_account():
    accounts = account_repository.select_all()

    if request.form["action"] == "Apply Changes":
        for account in accounts:
            account_name = request.form[f"account_name_{account.id}"]
            monthly_budget = float(request.form[f"monthly_budget_{account.id}"])
            amount_spent = float(request.form[f"amount_spent_{account.id}"]) if request.form[f"amount_spent_{account.id}"] else None
            currency_id = request.form["currency_id"]

            account = account_repository.select(account.id)
            updated_budget = Budget(monthly_budget, amount_spent, account.budget.id) # type: ignore
            budget_repository.update(updated_budget)
            updated_currency = currency_repository.select(currency_id)

            updated_account = Account(account_name, updated_budget, updated_currency, account.id) # type: ignore
                    
            account_repository.update(updated_account)
    
    elif request.form["action"] == "Delete Selected":
        for account in accounts:
            if request.form.get(f"account_{account.id}"):
                account_repository.delete(account.id)

    return redirect("/accounts")