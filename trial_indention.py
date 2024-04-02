def should_hit(dealer_total, player_total, player_low_aces, player_high_aces):
    """Return True if the player should hit (request another card) given the current game
    state, or False if the player should stay.
    When calculating a hand's total value, we count aces as "high" (with value 11) if doing so
    doesn't bring the total above 21, otherwise we count them as low (with value 1). 
    For example, if the player's hand is {A, A, A, 7}, we will count it as 11 + 1 + 1 + 7,
    and therefore set player_total=20, player_low_aces=2, player_high_aces=1.
    """
    if(dealer_total >= 2 and dealer_total <=3 and player_low_aces == 0):
        if player_total >= 13 and player_total <=21:
            return False
        else:
            return True
    elif (dealer_total > 3 and dealer_total < 7 and player_low_aces == 0):
        if player_total >= 12 and player_total <= 21:
            return False
        else:
            return True
    elif dealer_total > 6 and player_low_aces == 0:
        if player_total >= 17 and player_total <=21:
            return False
        else:
            return True
    elif(dealer_total >= 2 and dealer_total < 9 and player_low_aces != 0):
        if player_total >= 18 and player_total <= 21:
            return False
        else:
            return True
    elif (dealer_total >=9 and player_low_aces != 0):
        if player_total >= 19 and player_total <= 21:
            return False
        else:
            return True