from functions.classification_functions.get_offer_weight import get_offer_weight

# this is an example of how to get an offer weight
# I will use this on offers_for_all_flow_rules

weight = get_offer_weight("(bin: unitedKingdom - English)", "0343f17c-7539-4471-ad96-c09328ca0d88")

print(weight)


