from flask import Blueprint, redirect, render_template, request
import repositories.platform_repository as platform_repository
import repositories.campaign_repository as campaign_repository
import repositories.account_repository as account_repository
import repositories.budget_repository as budget_repository
from models.platform import Platform
from models.budget import Budget


platforms_blueprint = Blueprint("platforms", __name__)


@platforms_blueprint.route("/platforms")
def platforms():
    account = account_repository.select(1)
    platforms = platform_repository.select_all_by_account(account)
    return render_template("platforms/index.html", platforms=platforms)


@platforms_blueprint.route("/platforms/new")
def new_platform():
    return render_template("platforms/new.html")


@platforms_blueprint.route("/platforms/new", methods=["POST"])
def create_platform():
    platform_name = request.form["platform_name"]
    monthly_budget = request.form["monthly_budget"]
    amount_spent = request.form["amount_spent"]
    
    budget = Budget(monthly_budget, amount_spent)
    account = account_repository.select(1)
    new_platform = Platform(platform_name, budget, account)
    platform_repository.save(new_platform)
    return redirect("/platforms")


@platforms_blueprint.route("/platforms/<id>")
def tag_details(id):
    platform = platform_repository.select(id)
    campaigns = campaign_repository.select_all_by_platform(platform)

    return render_template("platforms/index.html", platform=platform, campaigns=campaigns)


@platforms_blueprint.route("/platforms/<id>/edit")
def edit_platform(id):
    platform = platform_repository.select(id)
    return render_template('platforms/edit.html', platform=platform)


@platforms_blueprint.route("/platforms/<id>", methods=["POST"])
def update_platform(id):
    platform_name = request.form["platform_name"]
    monthly_budget = request.form["monthly_budget"]
    amount_spent = request.form["amount_spent"]

    platform = platform_repository.select(id)
    updated_budget = Budget(monthly_budget, amount_spent, platform.budget.id) # type: ignore
    budget_repository.update(updated_budget)
    updated_platform = Platform(platform_name, updated_budget, id)
    platform_repository.update(updated_platform)

    return redirect("/platforms")


@platforms_blueprint.route("/platforms/<id>/delete", methods=["POST"])
def delete_platform(id):
    platform_repository.delete(id)
    return redirect("/platforms")