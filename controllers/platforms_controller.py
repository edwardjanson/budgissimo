from flask import Blueprint, redirect, render_template, request, session
import repositories.platform_repository as platform_repository
import repositories.campaign_repository as campaign_repository
import repositories.account_repository as account_repository
import repositories.budget_repository as budget_repository
import repositories.tag_repository as tag_repository
from models.platform import Platform
from models.budget import Budget


platforms_blueprint = Blueprint("platforms", __name__)


@platforms_blueprint.route("/platforms")
def platforms():
    account = account_repository.select(session["account_id"])
    platforms = platform_repository.select_all_by_account(account)
    return render_template("platforms/index.html", platforms=platforms, account=account)


@platforms_blueprint.route("/platforms/new")
def new_platform():
    return render_template("platforms/new.html")


@platforms_blueprint.route("/platforms/new", methods=["POST"])
def create_platform():
    platform_name = request.form["platform_name"]
    monthly_budget = float(request.form["monthly_budget"])
    
    budget = Budget(monthly_budget)
    budget_repository.save(budget)
    account = account_repository.select(session["account_id"])
    new_platform = Platform(platform_name, budget, account)
    platform_repository.save(new_platform)

    return redirect("/platforms")


@platforms_blueprint.route("/platforms/<platform_id>")
def platform_details(platform_id):
    if account_repository.request_allowed(session["account_id"], "platform_id", platform_id):
        account = account_repository.select(session["account_id"])
        platform = platform_repository.select(platform_id)
        campaigns = campaign_repository.select_all_by_platform(platform)

        return render_template("platforms/details.html", platform=platform, campaigns=campaigns, account=account)

    else: 
        return redirect("/access-denied")


@platforms_blueprint.route("/platforms/edit")
def edit_all_platforms():
    account = account_repository.select(session["account_id"])
    platforms = platform_repository.select_all_by_account(account)

    return render_template("platforms/edit.html", platforms=platforms, account=account)


@platforms_blueprint.route("/platforms/edit", methods=["POST"])
def update_all_platforms():
    account = account_repository.select(session["account_id"])
    platforms = platform_repository.select_all_by_account(account)

    if request.form["action"] == "Apply Changes":
        for platform in platforms:
            platform_name = request.form[f"platform_name_{platform.id}"]
            monthly_budget = float(request.form[f"monthly_budget_{platform.id}"])
            amount_spent = float(request.form[f"amount_spent_{platform.id}"]) if request.form[f"amount_spent_{platform.id}"] else None

            platform = platform_repository.select(platform.id)
            updated_budget = Budget(monthly_budget, amount_spent, platform.budget.id) # type: ignore
            budget_repository.update(updated_budget)

            updated_platform = Platform(platform_name, updated_budget, platform.account, platform.id) # type: ignore
                    
            platform_repository.update(updated_platform)
    
    elif request.form["action"] == "Delete Selected":
        for platform in platforms:
            if request.form.get(f"platform_{platform.id}"):
                platform_repository.delete(platform.id)

    return redirect("/platforms")


@platforms_blueprint.route("/platforms/<platform_id>/edit")
def edit_platform(platform_id):
    if account_repository.request_allowed(session["account_id"], "platform_id", platform_id):
        platform = platform_repository.select(platform_id)
        return render_template('platforms/edit.html', platform=platform)

    else: 
        return redirect("/access-denied")


@platforms_blueprint.route("/platforms/<platform_id>", methods=["POST"])
def update_platform(platform_id):
    if account_repository.request_allowed(session["account_id"], "platform_id", platform_id):
        platform_name = request.form["platform_name"]
        monthly_budget = request.form["monthly_budget"]
        amount_spent = request.form["amount_spent"]

        platform = platform_repository.select(platform_id)
        updated_budget = Budget(monthly_budget, amount_spent, platform.budget.id) # type: ignore
        budget_repository.update(updated_budget)
        updated_platform = Platform(platform_name, updated_budget, platform_id)
        platform_repository.update(updated_platform)

        return redirect("/platforms")

    else: 
        return redirect("/access-denied")


@platforms_blueprint.route("/platforms/<platform_id>/delete", methods=["POST"])
def delete_platform(platform_id):
    if account_repository.request_allowed(session["account_id"], "platform_id", platform_id):
        platform_repository.delete(platform_id)
        return redirect("/platforms")

    else: 
        return redirect("/access-denied")