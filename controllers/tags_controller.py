from flask import Blueprint, redirect, render_template, request, session
import repositories.tag_repository as tag_repository
import repositories.campaign_repository as campaign_repository
import repositories.campaign_tag_repository as campaign_tag_repository
import repositories.account_repository as account_repository
import repositories.budget_repository as budget_repository
import repositories.tag_category_repository as tag_category_repository
from models.tag import Tag
from models.campaign_tag import CampaignTag
from models.tag_category import TagCategory
from models.budget import Budget


tags_blueprint = Blueprint("tags", __name__)


@tags_blueprint.route("/tags")
def tags():
    account = account_repository.select(session["account_id"])
    tag_categories = tag_repository.get_tags_by_categories(account)

    return render_template("tags/index.html", tag_categories=tag_categories, account=account)


@tags_blueprint.route("/tags/new")
def new_tag():
    tag_type = request.args.get("tag_type")
    checked = "tag_category"

    if tag_type:
        if tag_type == "tag":
            checked = "tag"
            account = account_repository.select(session["account_id"])
            tag_categories = tag_category_repository.select_all_by_account(account)

            return render_template("tags/new_tag.html", checked=checked, tag_categories=tag_categories)
    else:
        return render_template("tags/new_category.html", checked=checked)

    return render_template("tags/new_category.html", checked=checked)


@tags_blueprint.route("/tags/new", methods=["POST"])
def create_tag():
    try:
        if request.form["tag_type"] == "Tag Category" or request.form["tag_type"] == "Tag":
            return redirect("/tags/new")
        
    except KeyError:
        if request.form["action"] == "Create Category":
            tag_category_name = request.form["category_name"]
            account = account_repository.select(session["account_id"])
            tag_category = TagCategory(tag_category_name, account)
            tag_category_repository.save(tag_category)
            return redirect("/tags")

        elif request.form["action"] == "Create Tag":
            tag_category_id = request.form["category_input"]
            tag_category = tag_category_repository.select(tag_category_id)
            tag_name = request.form["tag_name"]
            monthly_budget = float(request.form["monthly_budget"])
            budget_object = Budget(monthly_budget)
            budget = budget_repository.save(budget_object)
            account = account_repository.select(session["account_id"])
            tag = Tag(tag_name, tag_category, budget, account)

            tag_repository.save(tag)
            return redirect("/tags")
    
    return redirect("/tags/new")


@tags_blueprint.route("/tags/<tag_id>")
def tag_details(tag_id):
    if account_repository.request_allowed(session["account_id"], "tag_id", tag_id):
        account = account_repository.select(session["account_id"])
        tag = tag_repository.select(tag_id)
        platforms_campaigns = campaign_repository.get_platforms_campaigns_by_tag(tag)

        return render_template('tags/details.html', platforms_campaigns=platforms_campaigns, tag=tag, account=account)
        
    else: 
        return render_template("access_denied.html")


@tags_blueprint.route("/tags/edit")
def edit_all_tags():
    account = account_repository.select(session["account_id"])
    tag_categories = tag_repository.get_tags_by_categories(account)

    return render_template("tags/edit.html", tag_categories=tag_categories, account=account)


@tags_blueprint.route("/tags/edit", methods=["POST"])
def update_all_tags():
    account = account_repository.select(session["account_id"])
    tags = tag_repository.select_all_by_account(account)
    tag_categories = tag_category_repository.select_all_by_account(account)

    if request.form["action"] == "Apply Changes":
        for tag in tags:
            tag_name = request.form[f"tag_name_{tag.id}"]
            monthly_budget = float(request.form[f"monthly_budget_{tag.id}"])
            amount_spent = float(request.form[f"amount_spent_{tag.id}"]) if request.form[f"amount_spent_{tag.id}"] else None

            tag = tag_repository.select(tag.id)
            updated_budget = Budget(monthly_budget, amount_spent, tag.budget.id) # type: ignore
            budget_repository.update(updated_budget)
            updated_tag = Tag(tag_name, tag.category, updated_budget, tag.account, tag.id) # type: ignore
            tag_repository.update(updated_tag)
        
        for category in tag_categories:
            category_name = request.form[f"tag_category_{category.id}"]
            tag_category = tag_category_repository.select(category.id)
            updated_category = TagCategory(category_name, account, tag_category.id) # type: ignore
            tag_category_repository.update(updated_category)                    

    elif request.form["action"] == "Delete Selected":
        for tag in tags:
            if request.form[f"tag_{tag.id}"]:
                tag_repository.delete(tag.id)
            
        for category in tag_categories:
            if request.form[f"category_{category.id}"]:
                tag_category_repository.delete(category.id)

    return redirect("/tags")


@tags_blueprint.route("/tags/<tag_id>/edit")
def edit_tag(tag_id):
    if account_repository.request_allowed(session["account_id"], "tag_id", tag_id):
        tag = tag_repository.select(tag_id)
        return render_template('tags/edit.html', tag=tag)

    else: 
        return render_template("access_denied.html")


@tags_blueprint.route("/tags/<tag_id>/delete", methods=["POST"])
def delete_tag(tag_id):
    if account_repository.request_allowed(session["account_id"], "tag_id", tag_id):
        tag_repository.delete(tag_id)
        return redirect("/tags")
        
    else: 
        return render_template("access_denied.html")


@tags_blueprint.route("/tags/<tag_id>/campaigns/add")
def add_tag_to_campaigns(tag_id):
    if account_repository.request_allowed(session["account_id"], "tag_id", tag_id):
        account = account_repository.select(session["account_id"])
        tag = tag_repository.select(tag_id)
        platforms_campaigns = campaign_repository.get_platforms_campaigns_not_with_tag(tag)

        return render_template('tags/campaigns/add.html', platforms_campaigns=platforms_campaigns, tag=tag, account=account)
        
    else: 
        return render_template("access_denied.html")


@tags_blueprint.route("/tags/<tag_id>/campaigns/add", methods=["POST"])
def add_tag_to_campaigns_post(tag_id):
    account = account_repository.select(session["account_id"])
    tag = tag_repository.select(tag_id)
    campaigns = campaign_repository.select_all_by_account(account)
                
    for campaign in campaigns:
        try:
            if request.form[f"campaign_{campaign.id}"]:
                campaign_tag = CampaignTag(campaign, tag)
                campaign_tag_repository.save(campaign_tag)
        except KeyError:
            continue

    return redirect(f"/tags/{tag_id}")


@tags_blueprint.route("/tags/<tag_id>/campaigns/remove")
def remove_tag_to_campaigns(tag_id):
    if account_repository.request_allowed(session["account_id"], "tag_id", tag_id):
        account = account_repository.select(session["account_id"])
        tag = tag_repository.select(tag_id)
        platforms_campaigns = campaign_repository.get_platforms_campaigns_by_tag(tag)

        return render_template('tags/campaigns/remove.html', platforms_campaigns=platforms_campaigns, tag=tag, account=account)
        
    else: 
        return render_template("access_denied.html")


@tags_blueprint.route("/tags/<tag_id>/campaigns/remove", methods=["POST"])
def remove_tag_to_campaigns_post(tag_id):
    account = account_repository.select(session["account_id"])
    tag = tag_repository.select(tag_id)
    campaigns = campaign_repository.select_all_by_account(account)
                
    for campaign in campaigns:
        try:
            if request.form[f"campaign_{campaign.id}"]:
                campaign_tag = campaign_tag_repository.select_by_tag_and_campaign(tag, campaign)
                campaign_tag_repository.delete(campaign_tag.id) # type: ignore
        except KeyError:
            continue

    return redirect(f"/tags/{tag_id}")