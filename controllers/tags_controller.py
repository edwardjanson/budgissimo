from flask import Blueprint, redirect, render_template, request
import repositories.tag_repository as tag_repository
import repositories.account_repository as account_repository
import repositories.budget_repository as budget_repository
from models.tag import Tag
from models.budget import Budget


tags_blueprint = Blueprint("tags", __name__)


@tags_blueprint.route("/tags")
def tags():
    account = account_repository.select(1)
    tags = tag_repository.select_all_by_account(account)
    return render_template("tags/index.html", tags=tags)


@tags_blueprint.route("/tags/new")
def new_tag():
    return render_template("tags/new.html")


@tags_blueprint.route("/tags/new", methods=["POST"])
def create_tag():
    tag_name = request.form["tag_name"]
    monthly_budget = request.form["monthly_budget"]
    amount_spent = request.form["amount_spent"]
    
    budget = Budget(monthly_budget, amount_spent)
    account = account_repository.select(1)
    new_tag = Tag(tag_name, budget, account)
    tag_repository.save(new_tag)
    return redirect("/tags")


@tags_blueprint.route("/tags/<id>/edit")
def edit_tag(id):
    tag = tag_repository.select(id)
    return render_template('tags/edit.html', tag=tag)


@tags_blueprint.route("/tags/<id>", methods=["POST"])
def update_tag(id):
    tag_name = request.form["tag_name"]
    monthly_budget = request.form["monthly_budget"]
    amount_spent = request.form["amount_spent"]

    tag = tag_repository.select(id)
    updated_budget = Budget(monthly_budget, amount_spent, tag.budget.id) # type: ignore
    budget_repository.update(updated_budget)
    updated_tag = Tag(tag_name, updated_budget, id)
    tag_repository.update(updated_tag)

    return redirect("/tags")


@tags_blueprint.route("/tags/<id>/delete", methods=["POST"])
def delete_tag(id):
    tag_repository.delete(id)
    return redirect("/tags")