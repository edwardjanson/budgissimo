import unittest
from models.tag import Tag
from models.campaign_tag import CampaignTag
from models.campaign import Campaign
from models.budget import Budget


class TestCampaignTag(unittest.TestCase):
    
    def setUp(self):
        self.budget_1 = Budget(500.00, 17.00, 30.00)
        self.budget_2 = Budget(400.00, 10.00, 20.00)
        self.tag_1 = Tag("Test tag", self.budget_1)
        self.campaign_1 = Campaign("Test campaign", self.budget_2)
        self.campaign_tag_1 = CampaignTag(self.campaign_1, self.tag_1)
    
    def test_campaign_tag_has_tag(self):
        self.assertEqual("Test tag", self.campaign_tag_1.tag.name)

    def test_campaign_tag_has_campaign(self):
        self.assertEqual("Test campaign", self.campaign_tag_1.campaign.name)