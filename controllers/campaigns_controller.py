from flask import Blueprint, redirect, render_template, request
import repositories.campaign_repository as campaign_repository
import repositories.platform_repository as platform_repository
import repositories.account_repository as account_repository
import repositories.budget_repository as budget_repository
from models.campaign import Campaign
from models.budget import Budget


campaigns_blueprint = Blueprint("campaigns", __name__)


@campaigns_blueprint.route("/platforms/<platform_id>/campaigns/new")
def new_campaign(platform_id):
    return render_template("campaigns/new.html")


@campaigns_blueprint.route("/platforms/<platform_id>/campaigns/new", methods=["POST"])
def create_campaign(platform_id):
    campaign_name = request.form["campaign_name"]
    monthly_budget = request.form["monthly_budget"]
    amount_spent = request.form["amount_spent"]
    
    budget = Budget(monthly_budget, amount_spent)
    platform = platform_repository.select(platform_id)
    new_campaign = Campaign(campaign_name, budget, platform)
    campaign_repository.save(new_campaign)
    return redirect("/platforms/<platform_id>")


@campaigns_blueprint.route("/platforms/<platform_id>/campaigns/<campaign_id>")
def tag_details(platform_id, campaign_id):
    campaign = campaign_repository.select(campaign_id)

    return render_template("campaigns/index.html", campaign=campaign)


@campaigns_blueprint.route("/campaigns/<platform_id>/campaigns/<campaign_id>/edit")
def edit_campaign(platform_id, campaign_id):
    campaign = campaign_repository.select(campaign_id)
    return render_template('campaigns/edit.html', campaign=campaign)


@campaigns_blueprint.route("/campaigns/<platform_id>/campaigns/<campaign_id>", methods=["POST"])
def update_campaign(platform_id, campaign_id):
    campaign_name = request.form["campaign_name"]
    monthly_budget = request.form["monthly_budget"]
    amount_spent = request.form["amount_spent"]

    campaign = campaign_repository.select(campaign_id)
    updated_budget = Budget(monthly_budget, amount_spent, campaign.budget.id) # type: ignore
    budget_repository.update(updated_budget)
    updated_campaign = Campaign(campaign_name, updated_budget, campaign_id)
    campaign_repository.update(updated_campaign)

    return redirect("/campaigns/<platform_id>/campaigns")


@campaigns_blueprint.route("/campaigns/<platform_id>/campaigns/<campaign_id>/delete", methods=["POST"])
def delete_campaign(platform_id, campaign_id):
    campaign_repository.delete(campaign_id)
    return redirect("/campaigns")