def solution(cacheSize, cities):
    cache = {}
    cache_hit, cache_miss = 0, 0
    if cacheSize == 0:
        cache_miss = len(cities)
    else:
        for i in range(len(cities)):
            city = cities[i].lower()
            if cache.get(city, 0):
                cache_hit += 1
            else:
                if len(cache) >= cacheSize:
                    least_recentyl_used_city = sorted(cache.items(), key = lambda x: x[1])[0][0]
                    del cache[least_recentyl_used_city]
                cache_miss += 1
            cache[city] = i + 1
    return cache_miss * 5 + cache_hit


if __name__ == "__main__":
    cacheSize = 2
    cities = ["Jeju", "Pangyo", "NewYork", "newyork"]
    print(solution(cacheSize, cities))