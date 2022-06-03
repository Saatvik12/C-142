import pandas as pd

df = pd.read_csv('final.csv')

#df2.head()
C = df['vote_average'].mean()
#print(C)
m = df['vote_count'].quantile(0.9)
#print(m)
q_movies = df.copy().loc[df['vote_count']>=m]
#print(q_movies.shape)
def weighed_rating(x,m=m,C=C):
  V=x['vote_count']
  R=x['vote_average']
  return (V/(V+m)*R+(m/V+m)*C)
q_movies['score']=q_movies.apply(weighed_rating,axis=1)
q_movies=q_movies.sort_values('score',ascending=False)
q_movies[['title','poster_link','relese_date','run_time','vote_average','overview']].head(20).values.tolist()