implication = [
    'Science',
    'Movies',
    'Exercise',
    'Computer',
    'Music',
    'Socializing',
    'Sports',
    'Shopping',
    'Traveling',
    'Homemade',
    'Faith',
    'Housework',
    'Crafting',
    'Technics',
    'Gambling',
    'Cooking',
    'Art',
    'Dancing',
    'Painting',
    'Computer gaming',
    'Coding',
    'Hunting',
    'Fishing',
    'Running',
    'Swimming',
    'Skiing',
    'Family',
    'Working',
    'Development',
    'Guns',
    'Reading',
]

if __name__ == "__main__":

    implication_formated = {}
    for skill in implication:
        skill_id = skill.lower().replace(' ', '_')
        implication_formated[skill_id] = skill
