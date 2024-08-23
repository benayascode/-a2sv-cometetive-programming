class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        c = {}
        w = set(tuple(wa) for wa in walls)
        g = set(tuple(gu) for gu in guards)

        for i in guards:
            row, col = i
            for l in range(col - 1, -1, -1):
                if (row, l) in w or (row, l) in g:
                    break
                c[(row, l)] = 1

            for r in range(col + 1, n):
                if (row, r) in w or (row, r) in g: 
                    break
                c[(row, r)] = 1

            for u in range(row - 1, -1, -1):
                if (u, col) in w or (u, col) in g:
                    break
                c[(u, col)] = 1

            for d in range(row + 1, m):
                if (d, col) in w or (d, col) in g:
                    break
                c[(d, col)] = 1

        return m * n - (len(g) + len(w) + len(c))
