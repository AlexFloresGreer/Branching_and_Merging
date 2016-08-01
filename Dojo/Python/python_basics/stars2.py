# Draw Stars

x = [4, "tom", "michael", 10]
def draw_star(x):
    for i in x:
        try:
            int(i)
            print i * "*"
        except ValueError:
            print len(i) * i[0].lower()



draw_star(x)

