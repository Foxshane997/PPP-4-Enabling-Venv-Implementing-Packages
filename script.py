import pprint
import requests
import matplotlib.pyplot as plt
from tabulate import tabulate

# Fetch Pokémon data from API
API_URL = 'https://pokeapi.co/api/v2/pokemon/35'
r = requests.get(API_URL)
response = r.json()

# Fetch basic Pokémon information
pokemon_basic_info = {
    'name': response['name'],
    'id': response['id'],
    'types': [t['type']['name'] for t in response['types']],
    'stats': {stat['stat']['name']: stat['base_stat'] for stat in response['stats']}
}

# Display basic information as text
pokemon_info = (
    f"Name: {pokemon_basic_info['name'].capitalize()}\n"
    f"ID: {pokemon_basic_info['id']}\n"
    f"Types: {', '.join(pokemon_basic_info['types'])}\n"
    f"Stats:\n" + "\n".join(f"  {key.capitalize()}: {value}" for key, value in pokemon_basic_info['stats'].items())
)
print("Basic Information (Text):\n")
print(pokemon_info)

# Display basic information as a table
table = [
    ["Name", pokemon_basic_info['name'].capitalize()],
    ["ID", pokemon_basic_info['id']],
    ["Types", ', '.join(pokemon_basic_info['types'])],
]

stats_table = [[key.capitalize(), value] for key, value in pokemon_basic_info['stats'].items()]
table.extend(stats_table)

print("\nBasic Information (Table):\n")
print(tabulate(table, headers=["Attribute", "Value"]))

# Display Pokémon stats as a bar chart
stats = pokemon_basic_info['stats']
names = list(stats.keys())
values = list(stats.values())

plt.figure(figsize=(10, 6))
plt.bar(names, values, color='skyblue')
plt.xlabel('Stats')
plt.ylabel('Base Value')
plt.title(f"{pokemon_basic_info['name'].capitalize()} Stats")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

html_content = f"""
<!DOCTYPE html>
<html>
<head>
    <title>{pokemon_basic_info['name'].capitalize()}</title>
    <style>
        body {{ font-family: Arial, sans-serif; }}
        .container {{ max-width: 600px; margin: auto; padding: 20px; }}
        h1 {{ text-align: center; }}
        .stats {{ list-style-type: none; padding: 0; }}
        .stats li {{ margin: 5px 0; }}
    </style>
</head>
<body>
    <div class="container">
        <h1>{pokemon_basic_info['name'].capitalize()}</h1>
        <p><strong>ID:</strong> {pokemon_basic_info['id']}</p>
        <p><strong>Types:</strong> {', '.join(pokemon_basic_info['types'])}</p>
        <ul class="stats">
            {''.join(f'<li><strong>{key.capitalize()}:</strong> {value}</li>' for key, value in pokemon_basic_info['stats'].items())}
        </ul>
    </div>
</body>
</html>
"""

with open("pokemon_info.html", "w") as file:
    file.write(html_content)

print("\nHTML file 'pokemon_info.html' has been created.")
