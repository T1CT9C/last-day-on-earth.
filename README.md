# last-day-on-earth.

Last Day on Earth is a text-based survival game set in a post-apocalyptic world. The world has been overrun by the undead, leaving only a few scattered survivors struggling to endure. As a player, you assume the role of a survivor and navigate this hostile landscape, scavenging for resources, battling zombies, and attempting to survive another day.

The game features a class-based system, allowing players to choose a unique survivor type, each with distinct abilities and attributes that affect gameplay. Strategy, resource management, and careful decision-making are key as you encounter various threats and challenges.

Game Features

	•	Class System: Choose from different survivor classes, each with special abilities and attributes.
	•	Combat System: Engage in intense battles with zombies and other enemies.
	•	Resource Management: Collect and manage critical resources necessary for survival, such as food, water, and ammunition.
	•	Exploration: Travel through different areas in search of supplies, allies, and safe zones.
	•	Dynamic Storyline: Make choices that affect your survival and lead to different outcomes.

Roadmap / To-Do List

1. Initial Setup

	•	Set up the basic project structure (folders, main script, etc.)
	•	Create a README.md with a description and roadmap
	•	Initialize Git for version control

2. Core Classes

	•	Player Class
	•	Define attributes (e.g., health, stamina, inventory)
	•	Implement basic methods for interacting with the game world (e.g., check_inventory, use_item)
	•	Survivor Classes (e.g., Scavenger, Soldier, Medic)
	•	Define each class with unique attributes (e.g., special abilities, starting resources)
	•	Create a factory function or method to allow players to choose a class
	•	Enemy Class
	•	Create an Enemy base class with attributes like health, damage, and type
	•	Define a Zombie subclass with specific behaviors
	•	Item Class
	•	Design items (e.g., weapons, food, medical supplies) with attributes like durability and effect on health
	•	Define methods to apply item effects (e.g., healing, increasing attack power)

3. Basic Game Logic

	•	Combat System
	•	Create turn-based combat between the player and zombies
	•	Implement attack and defense mechanics, including critical hits and dodging
	•	Inventory System
	•	Set up inventory management (e.g., add/remove items, display inventory)
	•	Implement usage of items and update character stats accordingly
	•	Exploration and Events
	•	Develop a map or location system for exploration
	•	Generate random events for encounters (e.g., finding resources, encountering enemies)

4. Advanced Features

	•	Story and Missions
	•	Write an introductory storyline and guide for the player
	•	Create optional missions or goals to provide direction (e.g., “Find shelter,” “Save another survivor”)
	•	NPC Interactions
	•	Develop non-playable characters (e.g., other survivors) with whom players can interact
	•	Implement a simple dialogue system with branching choices
	•	Save and Load System
	•	Set up a way to save the game state to a file
	•	Allow players to load from a previous save

5. Balancing and Testing

	•	Playtest each feature to check for bugs and balance issues
	•	Adjust difficulty as necessary to keep gameplay engaging and challenging