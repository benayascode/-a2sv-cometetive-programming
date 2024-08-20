class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        processorTime.sort()  
        tasks.sort(reverse=True) 
        out = 0
        for i in range(len(tasks) // 4):
            for j in range(4):
                out = max(out, processorTime[i] + tasks[i * 4 + j])

        return out
