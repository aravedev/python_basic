
friends = ["Rolf","Adam","Pamela"]
guest=["Pamela","George","Julio"]

friends_lower = set([f.lower() for f in friends])
guest_lower=set([g.lower() for g in guest])

print(friends_lower.intersection(guest_lower))