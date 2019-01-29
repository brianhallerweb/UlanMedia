from functions.misc.get_campaign_sets import get_campaign_sets
import json

campaigns = get_campaign_sets()
print(json.dumps(campaigns))


