import random
import math

# Dữ liệu các địa điểm (ID, tên, x, y)
locations = [
    ('Hà Nội', 0, 0),
    ('Hạ Long (Quảng Ninh)', 25, 20),
    ('Sapa (Lào Cai)', 5, 55),
    ('Ninh Bình', 15, 32),
    ('Phong Nha (Quảng Bình)', 25, 10),
    ('Huế', 32, 5),
    ('Đà Nẵng', 38, 2),
    ('Mai Châu (Hòa Bình)', 10, 38),
    ('Đảo Cát Bà (Hải Phòng)', 33, 35),
    ('Hà Giang', 12, 58)
]

N = 10
start_id = 0

def euclidean(a, b):
    """Tính khoảng cách Euclid giữa hai điểm"""
    x1, y1 = locations[a][1], locations[a][2]
    x2, y2 = locations[b][1], locations[b][2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def create_chromosome():
    """Tạo một cá thể ngẫu nhiên (hoán vị 9 điểm, điểm 0 ở đầu/cuối)"""
    mids = list(range(1, N))
    random.shuffle(mids)
    return [start_id] + mids + [start_id]

def population_init(size):
    """Khởi tạo quần thể với 'size' cá thể"""
    return [create_chromosome() for _ in range(size)]

def total_distance(route):
    """Tính tổng quãng đường của một hành trình"""
    return sum(euclidean(route[i], route[i+1]) for i in range(N))

def fitness(route):
    """Hàm fitness: 1 / tổng quãng đường"""
    return 1 / total_distance(route)

def tournament_selection(pop, k):
    """Chọn lọc theo phương pháp Tournament (k=5)"""
    selected = random.sample(pop, k)
    return min(selected, key=total_distance)

def ordered_crossover(p1, p2):
    """Ordered Crossover (OX) - Đúng chuẩn TSP"""
    size = len(p1)
    start, end = sorted(random.sample(range(1, size-1), 2))
    offspring = [None] * size
    offspring[0] = offspring[-1] = start_id
    
    # Copy đoạn giữa từ parent 1
    offspring[start:end] = p1[start:end]
    
    # Điền gen còn lại từ parent 2, bỏ qua gen đã có
    p2_mid = [gene for gene in p2[1:-1] if gene not in offspring]
    pos = 1
    for gene in p2_mid:
        while offspring[pos] is not None:
            pos += 1
        offspring[pos] = gene
    
    return offspring

def swap_mutate(chrom, rate=0.05):
    """Đột biến hoán vị (Swap Mutation)"""
    if random.random() < rate:
        idx1, idx2 = random.sample(range(1, len(chrom)-1), 2)
        chrom[idx1], chrom[idx2] = chrom[idx2], chrom[idx1]
    return chrom

def print_route_and_dist(route):
    """In hành trình ra tên địa điểm và tổng số km"""
    names = [locations[city_id][0] for city_id in route]
    s = " → ".join(names)
    dist = total_distance(route)
    print(f"Lộ trình: {s}")
    print(f"Tổng quãng đường: {dist:.2f} km\n")

def genetic_algorithm(
    generations=500,
    pop_size=100,
    crossover_rate=0.8,
    mutation_rate=0.05,
    tournament_k=5
):
    """Giải thuật di truyền chính"""
    pop = population_init(pop_size)
    best_route = min(pop, key=total_distance)
    best_distance = total_distance(best_route)

    for gen in range(1, generations + 1):
        new_pop = []
        while len(new_pop) < pop_size:
            # Selection
            parent1 = tournament_selection(pop, tournament_k)
            parent2 = tournament_selection(pop, tournament_k)
            
            # Crossover
            if random.random() < crossover_rate:
                child = ordered_crossover(parent1, parent2)
            else:
                child = parent1[:]
            
            # Mutation
            child = swap_mutate(child, mutation_rate)
            new_pop.append(child)

        pop = new_pop
        current_best = min(pop, key=total_distance)
        current_dist = total_distance(current_best)
        
        if current_dist < best_distance:
            best_route = current_best
            best_distance = current_dist

        # In kết quả theo yêu cầu: thế hệ 1, mỗi 50 thế hệ, và cuối cùng
        if gen == 1 or gen % 50 == 0 or gen == generations:
            print(f"Thế hệ {gen}: ", end="")
            print_route_and_dist(current_best)

    print("\n==> Kết quả tối ưu cuối cùng:")
    print_route_and_dist(best_route)

if __name__ == "__main__":
    genetic_algorithm()
