# 2. DataFormatter Class
class DataFormatter:
    @staticmethod
    def format_monster_data(monsters):
        return [f"Monster {monster['monster_id']} at ({monster['lat']}, {monster['lon']})" for monster in monsters]

    @staticmethod
    def format_survivor_data(survivors):
        return [f"Survivor {survivor['survivor_id']} in {survivor['district']} ({survivor['lat']}, {survivor['lon']})" for survivor in survivors]

    @staticmethod
    def format_resource_data(resources):
        return [
            f"{props.get('dist_name', 'Unknown')}: Temp {props.get('temp', 'N/A')}°C, Food {props.get('food_rations', 'N/A')}kg"
            for resource in resources if (props := resource.get("properties"))
        ]