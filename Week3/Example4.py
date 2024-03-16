def find_closest_pair_simple(points):
    min_distance = float('inf')
    closest_pair = None

    # Noktalari karsilastir
    for i in range(len(points)):
        for j in range(i+1, len(points)):
            # Mesafe hesaplamaca
            distance = ((points[i][0] - points[j][0])**2 + (points[i][1] - points[j][1])**2)**0.5
            # Closest buldugun her seferinde guncelleme yapalim
            if distance < min_distance:
                min_distance = distance
                closest_pair = (points[i], points[j])

    print(f"En yakın nokta çifti: {closest_pair}, Mesafe: {min_distance}")

# Örnek deneyelim
points_example = [(1, 2), (3, 4), (5, 6), (1, 3)]

# Fonksiyon
find_closest_pair_simple(points_example)
