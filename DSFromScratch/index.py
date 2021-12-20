users = [
    {"id": 0, "name": "Hero"},
    {"id": 1, "name": "Dunn"},
    {"id": 2, "name": "Sue"},
    {"id": 3, "name": "Chi"},
    {"id": 4, "name": "Thor"},
    {"id": 5, "name": "Clive"},
    {"id": 6, "name": "Hicks"},
    {"id": 7, "name": "Devin"},
    {"id": 8, "name": "Kate"},
    {"id": 9, "name": "Klein"},
]
# fmt: off
friendship_pairs = [
  (0, 1),
  (0, 2), 
  (1, 2),
  (1, 3), 
  (2, 3),
  (3, 4), 
  (4, 5),
  (5, 6), 
  (5, 7), 
  (6, 8),
  (7, 8), 
  (8, 9)
  ]

# fmt: on

friendships = {user["id"]: [] for user in users}

for i, j in friendship_pairs:
    friendships[i].append(j)
    friendships[j].append(i)


def number_of_friends(user):
    # How many friends does _user_ have?
    user_id = user["id"]
    friend_ids = friendships[user_id]
    return len(friend_ids)


total_connections = sum(number_of_friends(user) for user in users)
average_connections = total_connections / len(users)

most_friendly = [(user["id"], number_of_friends(user)) for user in users]


from collections import Counter


def friends_of_friends(user):
    user_id = user["id"]
    return Counter(
        foaf_id
        for friend_id in friendships[user_id]  # For each of my friends,
        for foaf_id in friendships[friend_id]  # find their friends
        if foaf_id != user_id and foaf_id not in friendships[user_id]  # who aren't me  # and aren't my friends.
    )


# fmt: off
interests = [
(0, "Hadoop"), (0, "Big Data"), (0, "HBase"), (0, "Java"),
(0, "Spark"), (0, "Storm"), (0, "Cassandra"),
(1, "NoSQL"), (1, "MongoDB"), (1, "Cassandra"), (1, "HBase"),
(1, "Postgres"), (2, "Python"), (2, "scikit-learn"), (2, "scipy"),
(2, "numpy"), (2, "statsmodels"), (2, "pandas"), (3, "R"), (3, "Python"),
(3, "statistics"), (3, "regression"), (3, "probability"),
(4, "machine learning"), (4, "regression"), (4, "decision trees"),
(4, "libsvm"), (5, "Python"), (5, "R"), (5, "Java"), (5, "C++"),
(5, "Haskell"), (5, "programming languages"), (6, "statistics"),
(6, "probability"), (6, "mathematics"), (6, "theory"),
(7, "machine learning"), (7, "scikit-learn"), (7, "Mahout"),
(7, "neural networks"), (8, "neural networks"), (8, "deep learning"),
(8, "Big Data"), (8, "artificial intelligence"), (9, "Hadoop"),
(9, "Java"), (9, "MapReduce"), (9, "Big Data")
]

# fmt: on


def data_scientists_who_like(target_interest):
    return [user_id for user_id, interest in interests if interest == target_interest]


print(data_scientists_who_like("Hadoop"))

from collections import defaultdict

user_ids_by_interest = defaultdict(list)

for user_id, interest in interests:
    user_ids_by_interest[user_id].append(interest)

# print(user_ids_by_interest)

interests_by_users = defaultdict(list)

for user_id, interest in interests:
    interests_by_users[interest].append(user_id)


print(interests_by_users)
