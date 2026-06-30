class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        visited={}
        for ch in strs:
            key= tuple(sorted(ch))
            if key not in visited:
                visited[key]=[]
            visited[key].append(ch)
        return list(visited.values())
       
