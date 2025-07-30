# Define sets of users
premium_users = {"alice", "bob", "carol"}
trial_users = {"carol", "dave", "eve"}

# 1. Users who have both premium and trial accounts
both = premium_users.interersection(trial_users)
print("Users with both premium and trial: ", both)

# 2. Users who are only premium
only_premium = premium_users.difference(trial_users)
print("Only premium users: ", only_premium)

# 3. Users who are only trial
only_trial = trial_users.difference(premium_users)
print("Only trial users: ", only_trial)

# 4. All users on the platform
all_users = premium_users.union(trial_users)
print("All users on platform: ", all_users)