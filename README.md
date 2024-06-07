# SeamCast Movie Recommender
![logo](images/seamcast%20light%20small.png)

Author:Ian Musau

## Libraries
- Pandas
- Feather
- Matplotlib
- NumPy
- Seaborn
- SciKit Learn

## Data
Data in the analysis can be found here:
https://www.kaggle.com/datasets/netflix-inc/netflix-prize-data <br>
The dataset need to be extracted to a `netflix-data` folder in the project base directory

## Overview
SeamCast is a planned movie streaming service that will also allow separate users to strem the same film in sync. They are in need of a robust movie recommendation system that users can enjoy together. Recommendations will be done by clustering similar users together and recommending movies popular with similar users.

## Business Problem
Given that the system is not only astreming platform, but will also allow multiple users to stream the same film concurrently to watch together, SeamCast is in need of a system that will:
- Find the best suited movies for a given user
- Recommend movies that will be enjoyed by all parties in the group
- Identify different subsets of users and cater to their tastes

## Evaluation
- With 67% accuracy the model falls just short of a serviceable score of 70%. This may be due to the fact that only a small subset of the data (less than 1%) was used for the analysis. One would assume, that when fed more data it wold perform more reliably. The combining of user clustering and classification prediction does well to solve the problem of recommending good movies.
- Such a system can easily be refined and deployed for the SeamCast service and would keep users entertaind with good suggestions.
- The proposed system would do well for watch parties by finding movies commonly popular in all users' clusters

## Conclusion
The use of KNN clustering and Decision Tree Forest classification is a powerful solution to a key problem for any sreaming service. Good recommendation keep hold of viewers longer and encourage them to resubscribe. Even in this rudimentary form the system would easily be up to the task, but with the aforementioned reommendations, the final version oof the system would rival that of any gian in the streaming space.<br>
SeamCast would do well to fund further development of the proposed solution to ensure domination of the streaming sector. 

## Previewing
Use the last 2 cells in the notebook. The first cell will select a user and recommend movies popular in their cluster:<br>
`
User: 704642 |
Recommendations: ['The Game', 'Richard III', 'Silk Stockings']
`<br>
The last cell will use the classifier to confirm that the given uesr will enjoy said recommendations:<br>
`
models predict user:704642 will like 'The Game' |
models predict user:704642 will like 'Richard III' |
models predict user:704642 will like 'Silk Stockings'
`
