t = int(input("Time (hr) : "))
s = int(input("Distance (km) : "))

if t < 1 or s < 1:
    print("Time and distance must be 1 or bigger.")
else:
    v = int(s/t)
    print("Velocity :", v, "km/h")

