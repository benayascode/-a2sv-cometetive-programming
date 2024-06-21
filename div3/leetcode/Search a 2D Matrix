class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        out=[]
        for i in matrix:
            out.append(abs(target-i[0]))
        mini=min(out)
        if mini==0:
            return True
        ind=out.index(mini)
        for i in matrix[ind]:
            if i==target:
                return True
        for i in matrix[ind-1]:
            if i==target:
                return True
        return False
