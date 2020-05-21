# friend_visualizer
Program that analyzes twitter friends/followers and dispays graph showing connections between groups of people </br>
Twitter makes it difficult to scrape user data and the API rate limit is 15 calls per 15 minutes which is quite low </br>
I used a library I found online called Twint that scrapes data for you, but Twitter blocks a lot of their info as well and so the information received is incomplete </br>
The program graphs whatever information is given, and shows a somewhat accurate cluster of relationships </br>
Because the information given isn't 100% complete, the individual connections between people aren't important. Seeing the clusters that people lie in is what I cared more about as I wanted to visualize how my different groups of friends were connected. </br>
Check out example_graph.png for an example.
