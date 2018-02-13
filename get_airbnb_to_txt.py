import requests

def get_page(_offset):
	url = "https://www.airbnb.com/api/v2/explore_tabs?version=1.3.3&_format=for_explore_search_web&experiences_per_grid=20&items_per_grid=18&guidebooks_per_grid=20&auto_ib=true&fetch_filters=true&is_guided_search=true&is_new_cards_experiment=true&luxury_pre_launch=false&query_understanding_enabled=false&show_groupings=true&supports_for_you_v3=true&timezone_offset=-300&metadata_only=false&is_standard_search=true&tab_id=experience_tab&section_offset=3&items_offset=" + str(_offset) + "&recommendation_item_cursor=&refinement_paths[]=/experiences&query=&last_search_session_id=&federated_search_session_id=320016fd-d09c-48c0-b7ed-2786432d35fb&screen_size=large&_intents=p1&key=d306zoyjsyarp7ifhu67rjxn52tv0t20&currency=USD&locale=en"
	responses = requests.get(url).json()
	return responses

offset = 0
while offset <= 280: #280

	#add all results from this json pull to results var
	results = get_page(offset)
	items = results['explore_tabs'][0]['sections'][0]['trip_templates']
	for item in items:
		print '{'
		print '\"title\":' + '\"' + item['title'].encode('utf-8') + '\",'
		print '\"kicker_text\":' + '\"' + item['kicker_text'].encode('utf-8') + '\",'
		print '\"country\":' + '\"' + item['country'].encode('utf-8') + '\",'
		print '\"picture\":' + '\"' + item['picture']['large_ro'] + '\",'
		print '\"star_rating\":' + str(item['star_rating']) + ','
		print '\"lat\":' + str(item['lat']) + ','
		print '\"lng\":' + str(item['lng'])
		print '},'

	#update offset
	offset = offset + 40



#for airbnb:

#https://www.airbnb.com/api/v2/explore_tabs?version=1.3.3&_format=for_explore_search_web&experiences_per_grid=20&items_per_grid=18&guidebooks_per_grid=20&auto_ib=true&fetch_filters=true&is_guided_search=true&is_new_cards_experiment=true&luxury_pre_launch=false&query_understanding_enabled=false&show_groupings=true&supports_for_you_v3=true&timezone_offset=-300&metadata_only=false&is_standard_search=true&tab_id=experience_tab&section_offset=3&items_offset=40&recommendation_item_cursor=&refinement_paths[]=/experiences&query=&last_search_session_id=&federated_search_session_id=320016fd-d09c-48c0-b7ed-2786432d35fb&screen_size=large&_intents=p1&key=d306zoyjsyarp7ifhu67rjxn52tv0t20&currency=USD&locale=en

# https://www.airbnb.com/api/v2/explore_tabs?version=1.3.3&_format=for_explore_search_web&experiences_per_grid=20&items_per_grid=18&guidebooks_per_grid=20&auto_ib=true&fetch_filters=true&is_guided_search=true&is_new_cards_experiment=true&luxury_pre_launch=false&query_understanding_enabled=false&show_groupings=true&supports_for_you_v3=true&timezone_offset=-300&metadata_only=false&is_standard_search=true&tab_id=experience_tab&section_offset=5&items_offset=800&recommendation_item_cursor=&refinement_paths[]=/experiences&query=&last_search_session_id=&federated_search_session_id=320016fd-d09c-48c0-b7ed-2786432d35fb&screen_size=large&_intents=p1&key=d306zoyjsyarp7ifhu67rjxn52tv0t20&currency=USD&locale=en

# items_offset= increments by 40