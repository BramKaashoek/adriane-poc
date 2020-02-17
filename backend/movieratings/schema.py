# schema.py
from ariadne import ObjectType, make_executable_schema
from ratings import models
from .helpers import query_movie

type_defs = """
    type Query {
        movies: [Movie!]!
        ratings: [Rating!]!
    }

    type Movie {
        title: String!
        ratings: [Rating!]!
    }

    type Rating {
        user: User!
        movie: Movie!
        stars: Float!
    }

    type User {
        username: String!
    }

    type Mutation {
        createRating(input: CreateRatingInput): Rating!
    }

    input CreateRatingInput {
        movieId: Int!
        stars: Float!
    }
"""

query = ObjectType('Query')
movie = ObjectType('Movie')
rating = ObjectType('Rating')
mutation = ObjectType('Mutation')

@query.field("movies")
def resolve_movies(*_):
    ids = models.Movie.objects.values_list('id', flat=True)
    movies = [query_movie(id) for id in ids]
    return movies

@movie.field("ratings")
def resolve_ratings(movie, _):
    movie_id = movie['episode_id']
    return get_ratings(movie_id=movie_id)

@query.field("ratings")
def get_ratings(*_, movie_id=None, user_id=None):
    queryset = models.Rating.objects.all()
    if movie_id:
        queryset = queryset.filter(movie=movie_id)
    if user_id:
        queryset = queryset.filter(user=user_id)
    queryset.prefetch_related('movie').prefetch_related('user')

    ratings = []
    for rating in queryset:
        ratings.append({"stars": rating.stars, "user": rating.user, "_movie_id": rating.movie.id})

    return ratings

@rating.field("movie")
def get_movie_from_rating(rating, _):
    return query_movie(rating['_movie_id'])

@mutation.field("createRating")
def resolve_create_rating(_, info, input):
    movie = models.Movie(id=input['movieId'])
    user = models.CustomUser(id=1)
    res =  models.Rating.objects.create(movie=movie, stars=input['stars'], user=user)
    return {
        "stars": res.stars,
        "movie": query_movie(res.movie.id),
        "user": res.user
    }


schema = make_executable_schema(type_defs, query, mutation, movie, rating)

