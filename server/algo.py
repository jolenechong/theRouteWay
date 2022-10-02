from create_graph import adj_list, mapping, test_delay
from heap import MinHeap
import datetime

U_TURN = {0, 2}

def wrapper(source, destination, time, delays=test_delay):

    def get_delay(edge):
        return sum([delays['Road '+e] for e in edge.label.split()])

    def get_total_dist(edge):
        if edge is None:
            return 0
        return edge.weight + get_delay(edge)

    def get_neighbour_edge(vfrom, vto):
        for e in adj_list[vfrom]:
            if e.to == vto:
                return e

    def compare(elem):
        return elem[1]

    def find_path(distances, paths, start, end):
        curr = end
        path_len = distances[end]
        total_delay, total_len = 0, 0
        result, path = [], []
        print(paths)
        if not paths:
            return None

        while not curr == start:
            res = get_neighbour_edge(paths[curr], curr)
            total_delay += get_delay(res)
            total_len += get_total_dist(res)
            path.append(curr)
            curr = paths[curr]
            result.append(res.label)

        result.reverse()
        path.reverse()
        # print(result, total_len, path_len)

        temp_result, temp_path, uturn = [], [], -1
        if not round(total_len, 2) == round(path_len, 2):
            curr = paths[curr]
            if curr == 0:
                uturn = 0
                temp_result.extend(['3 1', '2 4'])
                temp_path.extend([1, 0, 1])
                uturn_res1 = get_neighbour_edge(1, 0)
                uturn_res2 = get_neighbour_edge(0, 1)
                total_delay += get_delay(uturn_res1) + get_delay(uturn_res2)
                total_len += get_total_dist(uturn_res1) + get_total_dist(uturn_res2)
            elif curr == 2:
                uturn = 2
                temp_result.append('16 17')
                temp_path.append(2)

            curr = paths[curr]
            if not uturn:
                while not curr == start:
                    res1 = get_neighbour_edge(curr, paths[curr])
                    res2 = get_neighbour_edge(paths[curr], curr)
                    total_delay += get_delay(res1) + get_delay(res2)
                    total_len += get_total_dist(res1) + get_total_dist(res2)
                    temp_result.insert(0, res2.label)
                    temp_result.append(res1.label)
                    temp_path.insert(0, paths[curr])
                    temp_path.append(paths[curr])
                    curr = paths[curr]
            else:
                while not paths[curr] == start:
                    res1 = get_neighbour_edge(curr, paths[curr])
                    res2 = get_neighbour_edge(paths[curr], curr)
                    total_delay += get_delay(res1) + get_delay(res2)
                    total_len += get_total_dist(res1) + get_total_dist(res2)
                    temp_result.insert(0, res1)
                    temp_result.append(res2.label)
                    temp_path.insert(0, curr)
                    temp_path.append(curr)
                    curr = paths[curr]
            
        temp_result.extend(result)
        temp_path.extend(path)
        # print(temp_path)
        assert round(total_len, 2) == round(path_len, 2)
        return temp_result, total_delay, total_len, temp_path, uturn

    def dijkstra(start, end, start_uturn=None):
        pq = MinHeap(compare)
        # pq.push((start, 0))
        dist = [float('inf') for _ in range(len(adj_list))]
        dist[start] = 0
        visited = [False for _ in range(len(adj_list))]
        visited[start] = True   
        path, invalid, curr = {}, {}, start
        if start_uturn:
            invalid[curr] = (True, start_uturn)

        first_iteration = 0
        while not pq.isEmpty() or not first_iteration:
        # while curr != end:
            first_iteration += 1
            for edge in adj_list[curr]:
                # print(dist)
                # print(path)
                # print(visited)
                # print(invalid)
                # print(pq.heap_list)
                # print('CURR:', curr, ' EDGE:', edge.to)
                curr_dist = 0
                check_invalid = invalid.get(curr, [0, -1])
                if not check_invalid[0] and check_invalid[1] != -1 and check_invalid[2] == edge.to:
                    curr_dist += check_invalid[1]
                curr_dist += dist[curr] + get_total_dist(edge)
                if curr_dist < dist[edge.to] and not (check_invalid[0] and check_invalid[1] == edge.to and edge.to not in U_TURN and curr not in U_TURN):
                    dist[edge.to] = curr_dist
                    path[edge.to] = curr
                    invalid[edge.to] = (True, curr)
                    visited[edge.to] = False
                    pq.push((edge.to, dist[edge.to]))

                if not visited[edge.to]:
                    for e in adj_list[edge.to]:
                        if pq.get_elem(e.to) and pq.get_elem(e.to)[1] > dist[edge.to]+get_total_dist(e) or not pq.get_elem(e.to):
                            try:
                                pq.remove(e.to)
                            except KeyError as err:
                                pass
                            pq.push((e.to, dist[edge.to]+get_total_dist(e)))
                        if edge.to in U_TURN:
                            prev, turn_invalid, running_total = edge.to, e.to, 0
                            while invalid.get(turn_invalid, [0, -1])[0]:
                                if turn_invalid == start:
                                    path[start] = edge.to
                                ori_invalid = invalid[turn_invalid][1]
                                e_edge = get_neighbour_edge(prev, turn_invalid)
                                if e_edge is None:
                                    break
                                running_total += get_total_dist(e_edge) + get_total_dist(get_neighbour_edge(turn_invalid, prev))
                                invalid[turn_invalid] = (False, running_total, ori_invalid)
                                prev, turn_invalid = turn_invalid, ori_invalid
                    visited[edge.to] = True   

            curr = pq.pop()

        # print(first_iteration)
        # print(dist, path)
        res = find_path(dist, path, start, end)
        if not res:
            return None
        result = {'route': [res[0]], 'timeNeeded': res[2], 'delay': 1 if res[1] else 0, 'uturn': 0 if res[4] == -1 else 1}
        if result['delay']:
            result['delayTime'] = res[1]
        if result['uturn']:
            result['uturnAt'] = res[4]
        return result, res[3], dist
        # return dist, path

    # print(dijkstra(5, 7, 7))
    # print(dijkstra(3, 5, 5))
    # # print(dijkstra(1, 3, 3))
    # print(dijkstra(7, 9, 9))
    # print(dijkstra(4, 6, 6))

    def generate_json(res, source, destination, time):
        res['source'] = source
        res['destination'] = destination
        formatted_date = datetime.datetime.strptime(time, "%Y-%m-%dT%H:%M")
        res['timeStart'] = datetime.datetime.strftime(formatted_date, '%I:%M %p')
        res['timeEnd'] = datetime.datetime.strftime(formatted_date + datetime.timedelta(minutes=res['timeNeeded']), '%I:%M %p')
        return res

    def generate_more_routes(k, best_path, best_route, dist, source, destination, time):
        all_paths = MinHeap(compare)
        result = []
        for j in range(1, len(best_path)-1):
            uturn = best_path[j-1]
            neighbour = get_neighbour_edge(best_path[j], best_path[j+1])
            # print(neighbour)
            adj_list[best_path[j]].remove(neighbour)
            spur_path = dijkstra(best_path[j], best_path[-1], uturn)
            if not spur_path:
                continue
            root_path = best_route[0][:j+1]
            # print(root_path, j)
            # print(spur_path[1])
            new_path_json = spur_path[0]
            new_path_json['timeNeeded'] = dist[best_path[j]]+new_path_json['timeNeeded']
            root_path.extend(new_path_json['route'][0])
            new_path_json['route'] = root_path
            all_paths.push([j, new_path_json['timeNeeded'], new_path_json])
            adj_list[best_path[j]].append(neighbour)
        for i in range(k-1):
            if all_paths.isEmpty():
                break
            res = all_paths.heap_list[0][2]
            all_paths.pop()
            res = generate_json(res, source, destination, time)
            res['option'] = i+2
            result.append(res)
        return result

    def final(source, destination, time):
        start = mapping[source[0]][1]
        start_uturn = None if len(mapping[source[0]]) <= 2 else mapping[source[0]][2]
        end = mapping[destination[0]][0]
        result = []
        res, path, dist = dijkstra(start, end, start_uturn)
        # print(path)
        res = generate_json(res, source, destination, time)
        res['option'] = 1
        result.append(res)
        # print('PATH',path)
        # print('RES', res)
        result.extend(generate_more_routes(5, path, res['route'], dist, source, destination, time))
        return result
    
    return final(source, destination, time)