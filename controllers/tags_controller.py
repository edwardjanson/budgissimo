from flask import Blueprint, redirect, render_template, request, session
import repositories.tag_repository as tag_repository
import repositories.campaign_repository as campaign_repository
import repositories.campaign_tag_repository as campaign_tag_repository
import repositories.account_repository as account_repository
import repositories.budget_repository as budget_repository
from models.tag import Tag
from models.budget import Budget


tags_blueprint = Blueprint("tags", __name__)


@tags_blueprint.route("/tags")
def tags():
    account = account_repository.select(session["account_id"])
    tags = tag_repository.select_all_by_account(account)
    return render_template("tags/index.html", tags=tags)


@tags_blueprint.route("/tags/new")
def new_tag():
    return render_template("tags/new.html")


@tags_blueprint.route("/tags/new", methods=["POST"])
def create_tag():
    tag_name = request.form["tag_name"]
    tag_type = request.form["tag_type"]
    monthly_budget = request.form["monthly_budget"]
    amount_spent = request.form["amount_spent"]
    
    budget = Budget(monthly_budget, amount_spent)
    account = account_repository.select(session["account_id"])
    new_tag = Tag(tag_name, tag_type, budget, account)
    tag_repository.save(new_tag)
    return redirect("/tags")


@tags_blueprint.route("/tags/<tag_id>")
def tag_details(tag_id):
    if account_repository.request_allowed(session["account_id"], "tag_id", tag_id):
        tag = tag_repository.select(tag_id)
        campaigns = campaign_tag_repository.select_all_campaigns_by_tag(tag)

        return render_template("tags/index.html", tag=tag, campaigns=campaigns)
    
    else: 
        return render_template("access_denied.")


@tags_blueprint.route("/tags/<tag_id>/edit")
def edit_tag(tag_id):
    if account_repository.request_allowed(session["account_id"], "tag_id", tag_id):
        tag = tag_repository.select(tag_id)
        return render_template('tags/edit.html', tag=tag)

    else: 
        return render_template("access_denied.html")


@tags_blueprint.route("/tags/<tag_id>", methods=["POST"])
def update_tag(tag_id):
    if account_repository.request_allowed(session["account_id"], "tag_id", tag_id):
        tag_name = request.form["tag_name"]
        tag_type = request.form["tag_type"]
        monthly_budget = request.form["monthly_budget"]
        amount_spent = request.form["amount_spent"]

        tag = tag_repository.select(tag_id)
        updated_budget = Budget(monthly_budget, amount_spent, tag.budget.id) # type: ignore
        budget_repository.update(updated_budget)
        updated_tag = Tag(tag_name, tag_type, updated_budget, tag_id)
        tag_repository.update(updated_tag)

        return redirect("/tags")
        
    else: 
        return render_template("access_denied.html")


@tags_blueprint.route("/tags/<tag_id>/delete", methods=["POST"])
def delete_tag(tag_id):
    if account_repository.request_allowed(session["account_id"], "tag_id", tag_id):
        tag_repository.delete(tag_id)
        return redirect("/tags")
    
    else: 
        return render_template("access_denied.html")