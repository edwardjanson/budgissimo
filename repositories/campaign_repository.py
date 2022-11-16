from db.run_sql import run_sql

from models.campaign import Campaign
import repositories.budget_repository as budget_repository
import repositories.platform_repository as platform_repository
import repositories.campaign_repository as campaign_repository
import repositories.campaign_tag_repository as campaign_tag_repository


def save(campaign):
    sql = "INSERT INTO campaigns (name, budget_id, platform_id) VALUES (%s, %s, %s) RETURNING *"
    values = [campaign.name, campaign.budget.id, campaign.platform.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    campaign.id = id
    return campaign


def select_all():
    campaigns = []

    sql = "SELECT * FROM campaigns"
    results = run_sql(sql)

    for row in results:
        budget = budget_repository.select(row['budget_id'])
        platform = platform_repository.select(row['platform_id'])
        campaign = Campaign(row['name'], budget, platform, row['id'])
        campaigns.append(campaign)
    return campaigns


def select(id):
    campaign = None
    sql = "SELECT * FROM campaigns WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        budget = budget_repository.select(result['budget_id'])
        platform = platform_repository.select(result['platform_id'])
        campaign = Campaign(result['name'], budget, platform, result['id'])
    return campaign


def delete_all():
    sql = "DELETE FROM campaigns"
    run_sql(sql)


def delete(id):
    sql = "DELETE FROM campaigns WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def update(campaign):
    sql = "UPDATE campaigns SET (name, budget_id, platform_id) = (%s, %s, %s) WHERE id = %s"
    values = [campaign.name, campaign.budget.id, campaign.platform.id, campaign.id]
    run_sql(sql, values)


def select_all_by_account(account):
    campaigns = []

    sql = """SELECT campaigns.id FROM campaigns
            INNER JOIN platforms
                ON campaigns.platform_id = platforms.id
            WHERE platforms.account_id = %s"""

    values = [account.id]
    results = run_sql(sql, values)

    for result in results:
        campaign = select(result["id"])
        campaigns.append(campaign)
    
    return campaigns


def select_all_by_platform(platform):
    campaigns = []

    sql = "SELECT id FROM campaigns WHERE platform_id = %s"
    values = [platform.id]
    results = run_sql(sql, values)

    for result in results:
        campaign = select(result["id"])
        campaigns.append(campaign)
    
    return campaigns


def get_platforms_campaigns_by_tag(tag):
    platforms = platform_repository.select_all_by_account(tag.account)

    platforms_with_campaigns = []

    for platform in platforms:
        campaign_objects = []

        sql = """SELECT campaigns.id as campaign_id, campaigns.platform_id as platform_id FROM campaigns
                INNER JOIN campaigns_tags
                    ON campaigns_tags.campaign_id = campaigns.id
                INNER JOIN tags
                    ON campaigns_tags.tag_id = tags.id
                WHERE tags.id = %s AND platform_id = %s"""
        values = [tag.id, platform.id] # type: ignore
        results = run_sql(sql, values)

        for row in results:
            campaign = campaign_repository.select(row["campaign_id"])
            campaign_objects.append(campaign)
        
        platform_dict = {}
        platform_dict[platform] = campaign_objects
        platforms_with_campaigns.append(platform_dict)

    return platforms_with_campaigns


def get_platforms_campaigns_not_with_tag(tag):
    platforms = platform_repository.select_all_by_account(tag.account)
    unwanted_campaign_ids = campaign_tag_repository.select_all_campaign_ids_by_tag(tag)

    platforms_with_campaigns = []

    for platform in platforms:
        campaign_objects = []

        sql = """SELECT DISTINCT campaigns.id as campaign_id, campaigns.platform_id as platform_id FROM campaigns
                INNER JOIN campaigns_tags
                    ON campaigns_tags.campaign_id = campaigns.id
                INNER JOIN tags
                    ON campaigns_tags.tag_id = tags.id
                WHERE platform_id = %s"""
        values = [platform.id] # type: ignore
        results = run_sql(sql, values)

        for row in results:
            campaign = campaign_repository.select(row["campaign_id"])
            if row["campaign_id"] not in unwanted_campaign_ids:
                campaign_objects.append(campaign)
                
        platform_dict = {}
        platform_dict[platform] = campaign_objects
        platforms_with_campaigns.append(platform_dict)

    return platforms_with_campaigns