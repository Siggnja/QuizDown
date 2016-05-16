					QuizDown




What is it?
------------
QuizDown is a simple question based game between two individuals.


How does it work?
-----------------
QuizDown gets its questions from an online database jservice.io, the questions gathered are within the category selected at the beginning of the game.

QuizDown uses a library called SequenceMatcher to calculate the similarity ratio between the users answer and the correct answer. If the ratio is 80% or higher the answer must surely be correct!

When a match is played QuizDown stores the names of the players and their scores in an SQL database. The information in this database is then used to display the highscore table after each match.

XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX



How do I use it?
----------------
The game is rather straightforward.

At the startup screen you choose how many questions you want, the difficulty and the category of the questions. You also enter the names of both players.

After pressing 'Start!' the game begins with player 1's turn. (We highly recommend that player 2 steps away from the computer during this time since the questions are identical)

The questions appears on the screen and the answer is submitted in the line below it. The 'Go!' button is pressed to check if the answer is correct. Should it be so the 'Next' button lights up indicating that the player can go to the next question.

If the player is unable to come up with an answer, the '?'(hint button) can be pressed. It displays a portion of the correct answer but does reduce the total points available for the question.

XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

If the player is clueless and is not able to come up with an answer the 'skip' button can be pressed. It takes the player to the next question but does not give any points.

Once player 1 has finished his turn player 2 takes over and is faced with the same questions.

After his turn has ended a result screen appears showing the percentage of points each player got out of the total available. A 'winner' icon appears over the victorious contestant.

A 'highscore' table is also displayed showing the 9 best scores achieved in QuizDowns (local) history. 


