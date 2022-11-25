from flask import Blueprint, redirect, render_template, request
import repositories.campaign_repository as campaign_repository
import repositories.platform_repository as platform_repository
import repositories.account_repository as account_repository
import repositories.budget_repository as budget_repository
import repositories.tag_repository as tag_repository
import repositories.campaign_tag_repository as campaign_tag_repository
from models.campaign import Campaign
from models.budget import Budget
from models.campaign_tag import CampaignTag


campaigns_blueprint = Blueprint("campaigns", __name__)


@campaigns_blueprint.route("/accounts/<account_id>/platforms/<platform_id>/campaigns/new")
def new_campaign(account_id, platform_id):
    account = account_repository.select(account_id)

    platform = platform_repository.select(platform_id)
    categories = tag_repository.get_tag_categories_and_names(account)

    return render_template("platforms/campaigns/new.html", platform=platform, categories=categories, account=account)
        

@campaigns_blueprint.route("/accounts/<account_id>/platforms/<platform_id>/campaigns/new", methods=["POST"])
def create_campaign(account_id, platform_id):
    account = account_repository.select(account_id)

    campaign_name = request.form["campaign_name"]
    monthly_budget = float(request.form["monthly_budget"])
    categories = tag_repository.get_tag_categories_and_names(account)
    
    budget = Budget(monthly_budget)
    budget_repository.save(budget)
    platform = platform_repository.select(platform_id)
    new_campaign = Campaign(campaign_name, budget, platform)
    campaign = campaign_repository.save(new_campaign)

    for tag_category, tag_names_ids in categories.items():
        try:
            tag_id = request.form[f"category_input_{tag_category}"]
            tag = tag_repository.select(tag_id)
            campaign_tag = CampaignTag(campaign, tag)
            campaign_tag_repository.save(campaign_tag)
        except KeyError:
            continue

    return redirect(f"/accounts/{account_id}/platforms/{platform_id}")


@campaigns_blueprint.route("/accounts/<account_id>/platforms/<platform_id>/campaigns/edit")
def edit_all_campaigns(account_id, platform_id):
    account = account_repository.select(account_id)
    platform = platform_repository.select(platform_id)
    campaigns = campaign_repository.select_all_by_platform(platform)

    return render_template("platforms/campaigns/edit.html", account=account, platform=platform, campaigns=campaigns)


@campaigns_blueprint.route("/accounts/<account_id>/platforms/<platform_id>/campaigns/edit", methods=["POST"])
def edit_campaign(account_id, platform_id):
    platform = platform_repository.select(platform_id)
    campaigns = campaign_repository.select_all_by_platform(platform)

    if request.form["action"] == "Apply Changes":
        for campaign in campaigns:
            campaign_name = request.form[f"campaign_name_{campaign.id}"]
            monthly_budget = float(request.form[f"monthly_budget_{campaign.id}"])
            amount_spent = float(request.form[f"amount_spent_{campaign.id}"]) if request.form[f"amount_spent_{campaign.id}"] else None

            campaign = campaign_repository.select(campaign.id)
            updated_budget = Budget(monthly_budget, amount_spent, campaign.budget.id) # type: ignore
            budget_repository.update(updated_budget)

            updated_campaign = Campaign(campaign_name, updated_budget, campaign.platform, campaign.id) # type: ignore
                    
            campaign_repository.update(updated_campaign)
    
    elif request.form["action"] == "Delete Selected":
        for campaign in campaigns:
            if request.form.get(f"campaign_{campaign.id}"):
                campaign_repository.delete(campaign.id)
    
    return redirect(f"/accounts/{account_id}/platforms/{platform_id}")