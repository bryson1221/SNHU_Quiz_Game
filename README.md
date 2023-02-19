# SNHU_Quiz_Game

The second artifact of my e-Portfolio is an SNHU Quiz Game I created in Python using Visual Studio 2022 as my IDE. This was one of the first projects I created when I started taking classes at SNHU and was new to the Computer Science program. 

# Here is the original work: 

This project consisted of 6 total questions (including the opening question “Do you want to play?”). After each question has answered, a response was prompted informing the user if they were correct or incorrect and the quiz moved on to the next question. Once you answered the final question, the game would close out.

# Here are my improvements: 
I added a timer to each question, that shows how long it took to the user to answer each prompted question. Once the question is answered a dialogue displays whether the user was ‘correct or incorrect’ and shows how long it took to answer the question. 

Each question was previously isolated in an ‘if else’ statement. To improve on this, I refactored my code to make it more efficient, readable, and maintainable. 

Once the quiz is completed, a final score is displayed to show how many questions were answered correctly. A new question is then prompted, asking if the user wants to play again. If the user selects ‘yes’ the game will loop through again. If the user selects ‘no’ the game will close. 

# Here is the value of these improvements: 

A timer gives more insight into the game and could help determine which questions are more difficult than others, allowing difficulty levels to be created if the game is expanded. 

By putting the questions and answers together in a list of tuples, it makes it easy to add or remove questions without having to change multiple lines of code.

Additionally, using a for loop to iterate through the list of questions allows for a more elegant solution to the problem, rather than having a bunch of duplicated code for each question. 

A final score gives the user something to ‘aim’ for and makes the game more competitive. 

Asking the user if they ‘want to play again’ allows for a new game to start quickly and easily rather than closing out the application and restarting.

# Here is how I met the course outcomes:

Course Outcome 4: I demonstrated an ability to use well-founded and innovative techniques, skills, and tools in computing practices for the purpose of implementing computer solutions that deliver value and accomplish industry-specific goals by completing the following enhancements:

I effectively improved the data structures (for loop rather than if /else statements for each question). 

I articulated my ideas of improvement by expanding the complexity of this quiz game (a timer, final score, and play again option). 

I also articulated the value of the improvements I made, allowing for expansion and insight into what will make the game more successful.
