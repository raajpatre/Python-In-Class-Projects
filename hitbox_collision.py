# [x, y, width, height]
enemy = [20, 20, 40, 40] 
print(f"Enemy is at {enemy[0]},{enemy[1]} with size {enemy[2]}x{enemy[3]}")

bullet_x = int(input("Fire at X: "))

bullet_y = int(input("Fire at Y: "))

re=enemy[0]+enemy[2]
bh=enemy[1]+enemy[3]
if enemy[0]<=bullet_x<=re and enemy[1]<=bullet_y<=bh:
    print("HIT")
else:
    print("MISS")