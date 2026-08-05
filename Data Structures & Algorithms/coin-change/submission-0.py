class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        queue = deque([amount])
        visited = set()
        count = 0
        while queue:
            # number of coins available at each graph level
            s = len(queue)
            while s:
                s -= 1
                amount = queue.popleft()
                if amount == 0:
                    return count
                if amount in visited or amount < 0:
                    continue
                visited.add(amount)
                for coin in coins:
                    queue.append(amount - coin)
            count += 1
        return -1
