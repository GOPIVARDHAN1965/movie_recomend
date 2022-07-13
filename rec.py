import pandas as pd
from sklearn.neighbors import NearestNeighbors
import matplotlib.pyplot as plt
from scipy.sparse import csr_matrix

def movie(name):
    return movie_rec(name)
    



def movie_rec(movie_name):
    movie_list = movies[movies['title'].str.contains(movie_name)]
    movie_index = movie_list.iloc[0]['movieId']
    knn=NearestNeighbors(metric='cosine',n_neighbors=20)
    knn.fit(csr_data)
    similarities,indeces=knn.kneighbors(csr_data[final_dataset[final_dataset['movieId'] == movie_index].index[0]],n_neighbors=11)
    rec = sorted(zip(indeces.squeeze().tolist(),similarities.squeeze().tolist()),key=lambda x:x[1])[:0:-1]
    l=[]
    for val in rec:
        movie_Id = final_dataset.iloc[val[0]]['movieId']
        l.append(movies[movies['movieId']==movie_Id]['title'].values[0])
        print(movies[movies['movieId']==movie_Id]['title'].values[0])
    return l

movies = pd.read_csv('movies.csv')
ratings = pd.read_csv('ratings.csv')
final_dataset=ratings.pivot(index="movieId", columns="userId", values="rating")
final_dataset.fillna(0,inplace=True)
no_of_users_who_rated_movie = ratings.groupby('movieId')['userId'].agg('count')
plt.scatter(no_of_users_who_rated_movie.index, no_of_users_who_rated_movie)
plt.xlabel('Movie Id')
plt.ylabel('The no of users who rated')
plt.axhline(y=10,color='r')
final_dataset=final_dataset.loc[no_of_users_who_rated_movie[no_of_users_who_rated_movie>10].index,:]
movies_rated_by_users = ratings.groupby('userId')['movieId'].agg('count')
plt.scatter(movies_rated_by_users.index,movies_rated_by_users)
plt.xlabel('userId')
plt.ylabel('No of movies')
plt.axhline(y=50,color='r')
final_dataset = final_dataset.loc[:,movies_rated_by_users[movies_rated_by_users>50].index]
csr_data = csr_matrix(final_dataset.values)
final_dataset.reset_index(inplace=True)



# print(final_dataset)
