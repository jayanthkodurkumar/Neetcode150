class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        count = 0
        n = len(isConnected)

        visited = [0] * n
        adj_list = []

        for i in range(n):
            adj_list.append([])

        for i in range(n):
            edges = isConnected[i]
            edges_list = adj_list[i]
            for j in range(len(edges)):
                if i != j and edges[j] == 1:
                    edges_list.append(j)

        print(adj_list)

        for i in range(n):
            if visited[i] == 0:
                count += 1
                self.dfs(i, adj_list, visited)

        return count

    def dfs(self, curr_node, adj_list, visited):
        visited[curr_node] = 1

        for node in adj_list[curr_node]:
            if visited[node] == 0:
                self.dfs(node, adj_list, visited)
