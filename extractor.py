import instaloader
import sys

def main():
	username = sys.argv[1]
	password = sys.argv[2]
	print("username: {}, Password: {}".format(username, password))
	search = sys.argv[3]
	print("perfil de: {}".format(search))
	max_posts=int(sys.argv[4])
	print("Curtidores dos últimos {} posts".format(sys.argv[4]))

	L = instaloader.Instaloader()
	L.login(username,password)
	profile = instaloader.Profile.from_username(L.context, search)

	likes = set()
	likes_all = list()
	print("fetching likes of all posts of profile {}".format(search))
	for k,post in enumerate(profile.get_posts()):
		if k < max_posts:
			print(post)
			new = post.get_likes()
			likes_all.extend(list(new))
			likes = likes | set(new)
	print("start")
	print("fetching followers of profile {}".format(search))
	followers = set(profile.get_followers())
	ghosts = followers - likes

	print("Storing ghosts into a file.")
	with open("ghosts-{}.txt".format(search), 'w') as f:
		for ghost in ghosts:
			print(ghost.username, file=f)
	print("storing likes into a file.")
	with open("likes-{}.txt".format(search), 'w') as f:
		for like in likes:
			print(like.username, file=f)
	print("storing likes_all into a file")
	with open("likes-all-{}".format(search), 'w') as f:
		for like in likes_all:
			print(like.username, file=f)
	print("end")
if __name__=="__main__":
	main()
