from db.run_sql import run_sql

from models.campaign_tag import CampaignTag
import repositories.campaign_repository as campaign_repository
import repositories.tag_repository as tag_repository


def save(campaign_tag):
    sql = "INSERT INTO campaigns_tags (campaign_id, tag_id) VALUES (%s, %s) RETURNING *"
    values = [campaign_tag.campaign.id, campaign_tag.tag.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    campaign_tag.id = id
    return campaign_tag


def select_all():
    campaigns_tags = []

    sql = "SELECT * FROM campaigns_tags"
    results = run_sql(sql)

    for row in results:
        campaign = campaign_repository.select(row['campaign_id'])
        tag = tag_repository.select(row['tag_id'])
        campaign_tag = CampaignTag(campaign, tag, row['id'])
        campaigns_tags.append(campaign_tag)
    return campaigns_tags


def select(id):
    campaign_tag = None
    sql = "SELECT * FROM campaigns_tags WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        campaign = campaign_repository.select(result['campaign_id'])
        tag = tag_repository.select(result['tag_id'])
        campaign_tag = CampaignTag(campaign, tag, result['id'])
    return campaign_tag


def delete_all():
    sql = "DELETE FROM campaigns_tags"
    run_sql(sql)


def delete(id):
    sql = "DELETE FROM campaigns_tags WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def update(campaign_tag):
    sql = "UPDATE campaigns_tags SET (campaign_id, tag_id) = (%s, %s) WHERE id = %s"
    values = [campaign_tag.campaign.id, campaign_tag.tag.id, campaign_tag.id]
    run_sql(sql, values)


def select_all_campaigns_by_tag(tag):
    campaigns = []

    sql = "SELECT campaign_id FROM campaigns_tags WHERE tag_id = %s"
    values = [tag.id]
    results = run_sql(sql, values)

    for result in results:
        campaign = campaign_repository.select(result["campaign_id"])
        campaigns.append(campaign)
    
    return campaigns


def select_all_campaign_ids_by_tag(tag):
    campaign_ids = []

    sql = "SELECT campaign_id FROM campaigns_tags WHERE tag_id = %s"
    values = [tag.id]
    results = run_sql(sql, values)

    for result in results:
        campaign_ids.append(result["campaign_id"])
    
    return campaign_ids


def select_by_tag_and_campaign(tag, campaign):
    campaign_tag = None
    sql = "SELECT * FROM campaigns_tags WHERE tag_id = %s AND campaign_id = %s"
    values = [tag.id, campaign.id]
    result = run_sql(sql, values)[0]

    if result is not None:
        campaign = campaign_repository.select(result['campaign_id'])
        tag = tag_repository.select(result['tag_id'])
        campaign_tag = CampaignTag(campaign, tag, result['id'])
    return campaign_tag
