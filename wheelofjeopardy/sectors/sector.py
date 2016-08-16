"""
Sector Super Class

action() method MUST be overriden by sub-classes
"""

#@TODO: unit tests for class
class Sector(object):
    MINIMUM_WAGER_AMOUNT = 5

    def __init__(self, name):
        self.name = name

    def action(self, game_state):
        raise NotImplementedError

    def __str__(self):
        return self.name

    def ask_next_question_in_category(self, category, game_state):
        game_state.current_question = game_state.next_question_in_category(category)

        # if no question was available in the selected category...
        if game_state.current_question == None:
            # @TODO god this is all kinds of horrible
            category_name = game_state.board._q_mat[game_state.current_round - 1].headers[category - 1]
            game_state.events.broadcast(
                'sector.no_questions_in_category', category_name
            )
        else:
            if game_state.current_question.is_daily_double():
                game_state.events.broadcast('board_sector.daily_double_selected')

                game_state.events.broadcast(
                    'board_sector.prompt_for_wager',
                    Sector.MINIMUM_WAGER_AMOUNT,
                    self._get_max_wager_amount(
                        game_state.current_question,
                        game_state.get_current_player()
                    )
                )
            else:
                self._ask_question(game_state.current_question, game_state)

    """
    Methods to deal with answering question for board_sector,
    player_choice_sector & opponent_choice_sector
    """
    def receive_answer(self, game_state, question, answer):
        game_state.events.broadcast('board_sector.check_answer', question, answer)

    def received_correct_answer(self, game_state, question):
        amount = self.get_question_value(question, game_state)
        game_state.get_current_player().increase_score_by(amount)
        game_state.active_wager = None
        game_state.current_question = None
        game_state.check_for_game_or_round_end()

    def received_incorrect_answer(self, game_state, question):
        current_player = game_state.get_current_player()
        amount = self.get_question_value(question, game_state)
        current_player.decrease_score_by(amount)
        game_state.active_wager = None
        game_state.current_question = None

        if current_player.has_free_spin_token():
            game_state.events.broadcast('sector.prompt_for_token_use')
        else:
            game_state.end_turn()

    def received_use_free_token(self, game_state):
        game_state.get_current_player().use_free_spin_token()
        game_state.check_for_game_or_round_end()

    def received_dont_use_free_token(self, game_state):
        game_state.end_turn()

    def received_wager_amount(self, game_state, wager):
        question = game_state.current_question
        player = game_state.get_current_player()

        if not self._is_wager_in_bounds(wager, question, player):
            game_state.events.broadcast('board_sector.received_invalid_wager')
            game_state.events.broadcast(
                'board_sector.prompt_for_wager',
                Sector.MINIMUM_WAGER_AMOUNT,
                self._get_max_wager_amount(question, player)
            )

            return

        game_state.active_wager = wager
        self._ask_question(question, game_state)

    def get_question_value(self, question, game_state):
        if question.is_daily_double():
            return game_state.active_wager
        else:
            return question.point_value

    # private

    def _ask_question(self, question, game_state):
        game_state.start_timer()
        game_state.events.broadcast('board_sector.question_will_be_asked', question)

    def _is_wager_in_bounds(self, wager, question, player):
        maximum = self._get_max_wager_amount(question, player)
        return wager >= Sector.MINIMUM_WAGER_AMOUNT and wager <= maximum

    def _get_max_wager_amount(self, question, player):
        return max([player.score, question.point_value])
