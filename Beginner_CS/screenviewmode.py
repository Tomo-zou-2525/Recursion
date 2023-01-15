def screenViewMode(height, width):
    # 関数を完成させてください
    if height >= width:
        return "portrait"
    else:
        return "landscape"


print(screenViewMode(150, 100))
print(screenViewMode(150, 150))
print(screenViewMode(150, 1000))
