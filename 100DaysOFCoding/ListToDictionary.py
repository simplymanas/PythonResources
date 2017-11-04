# convert lists to dictionaries

names = ['manas', 'deepak', 'devansh']
jobs = ['father', 'uncle', 'son']

names_jobs = zip(names, jobs)
#print(list(names_jobs))

# convert to dict
names_jobs_dict = dict(names_jobs)

print(names_jobs_dict)
