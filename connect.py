import requests
import pandas as pd
api_key = "ff2748e9602bce73e783c5047ada016e"

"""https://api.themoviedb.org/3/movie/550?api_key=ff2748e9602bce73e783c5047ada016e"""
"""https://api.themoviedb.org/3/movie/{movie_id}?api_key=<<api_key>>&language=en-US"""
output = "movies.csv"
movies = []
for x in range(0,5000):
    movie_id = x
    api_version = 3
    api_base_url = f"https://api.themoviedb.org/{api_version}"
    endpoint_path = f"/movie/{movie_id}"
    endpoint = f"{api_base_url}{endpoint_path}?api_key={api_key}&language=en-US"
    r = requests.get(endpoint) #data={"api_key": api_key})
    if r.status_code in range(200,299):
        data = r.json()
        l = {'id','release_date','budget','revenue','title', 'genres', 'vote_average','adult'}
        j = {key: data[key] for key in data.keys() & l}
        movies.append(j)
        # x+=1
        #print(type(movies))

df = pd.DataFrame(movies)
df.to_csv(output, index=False)
print(df.head())
# lst = ['adult','budget','id']
# for k,v in txt.items():
#     if k == 'adult':
#         print(v)
    
# print(txt['adult'],txt['title'])