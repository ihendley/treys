Treys
=====

A pure Python poker hand evaluation library

::

   [ 3 ❤ ] , [ 3 ♠ ]

Installation
------------

::

   $ pip install treys

Implementation notes
--------------------

Treys is a Python 3 port of
`Deuces <https://github.com/worldveil/deuces>`__ based on the initial work in
`msaindon’s <https://github.com/msaindon/deuces>`__ fork. Deuces was written 
by `Will Drevo <http://willdrevo.com/>`__ for the MIT Pokerbots Competition. 

Treys is lightweight and fast. All lookups are done with bit arithmetic and
dictionary lookups. That said, Treys won’t beat a C implemenation (~250k
eval/s) but it is useful for situations where Python is required or
where bots are allocated reasonable thinking time (human time scale).

Treys handles 5, 6, and 7 card hand lookups. The 6 and 7 card lookups
are done by combinatorially evaluating the 5 card choices.

Usage
-----

Treys is easy to set up and use.

.. code:: python

   >>> from treys import Card
   >>> card = Card.new('Qh')

Card objects are represented as integers to keep Treys performant and
lightweight.

Now let’s create the board and an example Texas Hold’em hand:

.. code:: python

   >>> board = [
   >>>     Card.new('Ah'),
   >>>     Card.new('Kd'),
   >>>     Card.new('Jc')
   >>> ]
   >>> hand = [
   >>>    Card.new('Qs'),
   >>>    Card.new('Th')
   >>> ]

Pretty print card integers to the terminal:

::

   >>> Card.print_pretty_cards(board + hand)
     [ A ❤ ] , [ K ♦ ] , [ J ♣ ] , [ Q ♠ ] , [ T ❤ ] 

If you have `termcolor <http://pypi.python.org/pypi/termcolor>`__
installed, they will be colored as well.

Otherwise move straight to evaluating your hand strength:

.. code:: python

   >>> from treys import Evaluator
   >>> evaluator = Evaluator()
   >>> print(evaluator.evaluate(board, hand))
   1600

Hand strength is valued on a scale of 1 to 7462, where 1 is a Royal
Flush and 7462 is unsuited 7-5-4-3-2, as there are only 7462 distinctly
ranked hands in poker.

If you want to deal out cards randomly from a deck, you can also do that
with Treys:

.. code:: python

   >>> from treys import Deck
   >>> deck = Deck()
   >>> board = deck.draw(5)
   >>> player1_hand = deck.draw(2)
   >>> player2_hand = deck.draw(2)

and print them:

::

   >>> Card.print_pretty_cards(board)
     [ 4 ♣ ] , [ A ♠ ] , [ 5 ♦ ] , [ K ♣ ] , [ 2 ♠ ]
   >>> Card.print_pretty_cards(player1_hand)
     [ 6 ♣ ] , [ 7 ❤ ] 
   >>> Card.print_pretty_cards(player2_hand)
     [ A ♣ ] , [ 3 ❤ ] 

Let’s evaluate both hands strength, and then bin them into classes, one
for each hand type (High Card, Pair, etc)

.. code:: python

   >>> p1_score = evaluator.evaluate(board, player1_hand)
   >>> p2_score = evaluator.evaluate(board, player2_hand)
   >>> p1_class = evaluator.get_rank_class(p1_score)
   >>> p2_class = evaluator.get_rank_class(p2_score)

or get a human-friendly string to describe the score,

::

   >>> print("Player 1 hand rank = %d (%s)\n" % (p1_score, evaluator.class_to_string(p1_class)))
   Player 1 hand rank = 6330 (High Card)

   >>> print("Player 2 hand rank = %d (%s)\n" % (p2_score, evaluator.class_to_string(p2_class)))
   Player 2 hand rank = 1609 (Straight)

or, coolest of all, get a blow-by-blow analysis of the stages of the
game with relation to hand strength:

::

   >>> hands = [player1_hand, player2_hand]
   >>> evaluator.hand_summary(board, hands)

   ========== FLOP ==========
   Player 1 hand = High Card, percentage rank among all hands = 0.893192
   Player 2 hand = Pair, percentage rank among all hands = 0.474672
   Player 2 hand is currently winning.

   ========== TURN ==========
   Player 1 hand = High Card, percentage rank among all hands = 0.848298
   Player 2 hand = Pair, percentage rank among all hands = 0.452292
   Player 2 hand is currently winning.

   ========== RIVER ==========
   Player 1 hand = High Card, percentage rank among all hands = 0.848298
   Player 2 hand = Straight, percentage rank among all hands = 0.215626

   ========== HAND OVER ==========
   Player 2 is the winner with a Straight
