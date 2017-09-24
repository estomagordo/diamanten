class Game:

    def __init__(self):    
        self.MAX_PLAYERS = 5
        self.VOID_COUNT = 6
        self.BANDIT_COUNT = 4
        self.RUBY_COUNT = 2
        self.EMERALD_COUNT = 3
        self.TOPAZ_COUNT = 6
        self.VISA_COUNT = 8
        self.STAR_OF_AFRICA_COUNT = 1
        
        self.TOPAZ_VALUE = 3000
        self.EMERAL_VALUE = 4000
        self.RUBY_COUNT = 5000
        self.STARTING_MONEY = 5000
        
        self.places = {
            'Tangier': (
                (0, 5, 'Tunis'),
                (0, 5, 'Sahara'),
                (0, 2, 'Marrakesh'),
                (1, 3, 'Tunis'),
                (1, 3, 'Canary Islands'),
                (2, 1, 'Marrakesh'),
                (2, 1, 'Tripoli')
            ),
            'Marrakesh': (
                (0, 2, 'Tangier'),
                (0, 8, 'Dakar'),
                (2, 1, 'Tangier'),
                (2, 1, 'Sierra Leone'),
                (2, 1, 'The Gold Coast')
            ),
            'Canary Islands': (
                (1, 3, 'Tangier'),
                (1, 5, 'Dakar')
            ),
            'Dakar': (
                (0, 8, 'Marrakesh'),
                (0, 4, 'Sierra Leone'),
                (1, 5, 'Canary Islands'),
                (1, 3, 'Sierra Leone'),
                (1, 10, 'Saint Helena')
            ),
            'Sierra Leone': (
                (0, 4, 'Dakar'),
                (0, 5, 'The Gold Coast'),
                (0, 5, 'Timbuktu'),
                (1, 3, 'Dakar'),
                (1, 4, 'The Gold Coast'),
                (1, 11, 'Saint Helena'),
                (2, 1, 'Saint Helena'),
                (2, 1, 'Marrakesh')
            ),
            'The Gold Coast': (
                (0, 5, 'Sierra Leone'),
                (0, 4, 'Timbuktu'),
                (1, 4, 'Sierra Leone'),
                (1, 4, 'The Slave Coast'),
                (1, 11, 'Whale Bay'),
                (2, 1, 'Marrakesh'),
                (2, 1, 'Tripoli'),
                (2, 1, 'Luanda'),
                (2, 1, 'Whale Bay')
            ),
            'The Slave Coast': (
                (0, 5, 'Timbuktu'),
                (0, 7, 'Ouaddai'),
                (0, 7, 'Darfur'),
                (0, 5, 'Congo'),
                (1, 4, 'The Gold Coast'),
                (1, 9, 'Whale Bay')
            ),
            'Luanda': (
                (0, 3, 'Congo'),
                (0, 4, 'Kabalo'),
                (0, 9, 'Mozambique'),
                (0, 10, 'Victoria Falls'),
                (0, 10, 'Drakensberg'),
                (2, 1, 'The Gold Coast'),
                (2, 1, 'Whale Bay')
            ),
            'Saint Helena': (
                (1, 10, 'Dakar'),
                (1, 11, 'Sierra Leone'),
                (1, 9, 'Cape Town'),
                (1, 10, 'Whale Bay'),
                (2, 1, 'Sierra Leone'),
                (2, 1, 'Cape Town')
            ),
            'Whale Bay': (
                (0, 4, 'Victoria Falls'),
                (0, 4, 'Cape Town'),
                (1, 9, 'The Slave Coast'),
                (1, 11, 'The Gold Coast'),
                (1, 10, 'Saint Helena'),
                (1, 3, 'Cape Town'),
                (2, 1, 'Luanda'),
                (2, 1, 'Cape Town')
            ),
            'Cape Town': (
                (0, 4, 'Whale Bay'),
                (1, 3, 'Whale Bay'),
                (1, 9, 'Saint Helena'),
                (1, 8, 'Cape Sainte Marie'),
                (2, 1, 'Saint Helena'),
                (2, 1, 'Whale Bay'),
                (2, 1, 'Kabalo'),
                (2, 1, 'Drakensberg'),
                (2, 1, 'Tamatave'),
                (2, 1, 'Cape Sainte Marie')
            ),
            'Drakensberg': (
                (0, 3, 'Victoria Falls'),
                (0, 5, 'Mozambique'),
                (0, 10, 'Luanda'),
                (2, 1, 'Cape Town'),
                (2, 1, 'Lake Victoria')
            ),
            'Victoria Falls': (
                (0, 4, 'Whale Bay'),
                (0, 3, 'Drakensberg'),
                (0, 5, 'Mozambique'),
                (0, 10, 'Luanda')
            ),
            'Kabalo': (
                (0, 4, 'Luanda'),
                (0, 4, 'Lake Victoria'),
                (2, 1, 'Cape Town'),
                (2, 1, 'Darfur')
            ),
            'Congo': (
                (0, 3, 'Luanda'),
                (0, 5, 'The Slave Coast'),
                (0, 6, 'Darfur'),
                (0, 6, 'Ouaddai')
            ),
            'Timbuktu': (
                (0, 5, 'The Slave Coast'),
                (0, 4, 'The Gold Coast'),
                (0, 5, 'Sierra Leone')
            ),
            'Sahara': (
                (0, 5, 'Tangier'),
                (0, 5, 'Marrakesh'),
                (0, 8, 'Darfur')
            ),
            'Tunis': (
                (0, 3, 'Tripoli'),
                (0, 5, 'Tangier'),
                (1, 3, 'Tangier'),
                (1, 5, 'Cairo')
            ),
            'Tripoli': (
                (0, 3, 'Tunis'),
                (0, 6, 'Omdurman'),
                (2, 1, 'Tangier'),
                (2, 1, 'The Gold Coast'),
                (2, 1, 'Darfur')
            ),
            'Omdurman': (
                (0, 4, 'Cairo'),
                (0, 3, 'Darfur'),
                (0, 6, 'Tripoli')
            ),
            'Cairo': (
                (0, 4, 'Omdurman'),
                (1, 4, 'Suakin'),
                (1, 5, 'Tunis'),
                (2, 1, 'Suakin')
            ),
            'Darfur': (
                (0, 3, 'Omdurman'),
                (0, 4, 'Suakin'),
                (0, 2, 'Bahr el Gazel'),
                (0, 6, 'Congo'),
                (0, 7, 'The Slave Coast'),
                (0, 4, 'Ouaddai'),
                (0, 8, 'Sahara'),
                (2, 1, 'Tripoli'),
                (2, 1, 'Suakin'),
                (2, 1, 'Kabalo')
            ),
            'Bahr el Gazel': (
                (0, 2, 'Darfur'),
                (0, 2, 'Lake Victoria')
            ),
            'Lake Victoria': (
                (0, 2, 'Bahr el Gazel'),
                (0, 4, 'Kabalo'),
                (0, 4, 'Addis Ababa'),
                (0, 5, 'Zanzibar'),
                (0, 6, 'Mozambique'),
                (2, 1, 'Suakin'),
                (2, 1, 'Drakensberg')
            ),
            'Suakin': (
                (0, 4, 'Darfur'),
                (0, 3, 'Addis Ababa'),
                (1, 4, 'Cairo'),
                (1, 4, 'Cape Guardafui'),
                (2, 1, 'Cairo'),
                (2, 1, 'Darfur'),
                (2, 1, 'Lake Victoria')
            ),
            'Addis Ababa': (
                (0, 3, 'Lake Victoria'),
                (0, 3, 'Suakin'),
                (0, 3, 'Cape Guardafui')
            ),
            'Cape Guardafui': (
                (0, 3, 'Addis Ababa'),
                (0, 6, 'Zanzibar'),
                (1, 4, 'Suakin'),
                (1, 8, 'Mozambique'),
                (1, 8, 'Tamatave'),
                (2, 1, 'Lake Victoria'),
                (2, 1, 'Tamatave')
            ),
            'Tamatave': (
                (0, 4, 'Cape Sainte Marie'),
                (1, 8, 'Cape Guardafui'),
                (2, 1, 'Cape Guardafui')
            ),
            'Cape Sainte Marie': (
                (0, 4, 'Tamatave'),
                (1, 3, 'Mozambique'),
                (1, 8, 'Cape Town'),
                (2, 1, 'Cape Town')
            ),
            'Ouaddai': (
                (0, 4, 'Darfur'),
                (0, 6, 'Congo'),
                (0, 7, 'The Slave Coast')
            ),
            'Zanzibar': (
                (0, 3, 'Mozambique'),
                (0, 6, 'Cape Guardafui'),
                (0, 5, 'Lake Victoria')
            ),
            'Mozambique': (
                (0, 3, 'Zanzibar'),
                (0, 6, 'Lake Victoria'),
                (0, 5, 'Drakensberg'),
                (0, 5, 'Victoria Falls'),
                (0, 9, 'Luanda'),
                (1, 8, 'Cape Guardafui'),
                (1, 3, 'Cape Sainte Marie')
            )
        }
    
def tests():
    game = Game()
    
    for place in game.places.values():
        for destination in place:
            assert destination[2] in game.places, 'Illegal destination name ' + destination[2]
    
if __name__ == '__main__':
    tests()