# Given a list accounts, each element accounts[i] is a list of strings, where the first element accounts[i][0] is a name, and the rest of the elements are emails representing emails of the account.

# Now, we would like to merge these accounts. Two accounts definitely belong to the same person if there is some email that is common to both accounts. Note that even if two accounts have the same name, they may belong to different people as people could have the same name. A person can have any number of accounts initially, but all of their accounts definitely have the same name.

# After merging the accounts, return the accounts in the following format: the first element of each account is the name, and the rest of the elements are emails in sorted order. The accounts themselves can be returned in any order.

# Example 1:
# Input: 
# accounts = [["John", "johnsmith@mail.com", "john00@mail.com"], ["John", "johnnybravo@mail.com"], ["John", "johnsmith@mail.com", "john_newyork@mail.com"], ["Mary", "mary@mail.com"]]
# Output: [["John", 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com'],  ["John", "johnnybravo@mail.com"], ["Mary", "mary@mail.com"]]
# Explanation: 
# The first and third John's are the same person as they have the common email "johnsmith@mail.com".
# The second John and Mary are different people as none of their email addresses are used by other accounts.
# We could return these lists in any order, for example the answer [['Mary', 'mary@mail.com'], ['John', 'johnnybravo@mail.com'], 
# ['John', 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com']] would still be accepted.
# Note:

# The length of accounts will be in the range [1, 1000].
# The length of accounts[i] will be in the range [1, 10].
# The length of accounts[i][j] will be in the range [1, 30].


# Approach 1: build graph + BFS
# parse the accounts to make a graph
# find the connected component of the graph
# output the answer
# time: O(sigma ai*logai), where ai is the length of accounts[i]
class Graph:
    def __init__(self, accounts):
        self.accounts = accounts
        self.visited = set()
        self.edges = collections.defaultdict(lambda: set())
        self.email_2_user = {}
        self.find_adj_undirected()
    
    def find_adj_undirected(self):
        for account in self.accounts:
            user_name = account[0]
            for email in account[1:]:
                self.edges[account[1]].add(email)
                self.edges[email].add(account[1])
                self.email_2_user[email] = user_name

class Solution(object):
    def accountsMerge(self, accounts):
        """
        :type accounts: List[List[str]]
        :rtype: List[List[str]]
        """
        # parse the accounts to make a graph
        graph = Graph(accounts)
        # find the connected component of the graph
        # bfs approach
        res = []
        for node in graph.edges.keys():
            if node not in graph.visited:
                q = collections.deque()
                graph.visited.add(node)
                q.append(node)
                component = []
                while q:
                    cur_node = q.popleft()
                    component.append(cur_node)
                    for adj_node in graph.edges[cur_node]:
                        if adj_node not in graph.visited:
                            graph.visited.add(adj_node)
                            q.append(adj_node)
                component.sort()
                res.append([graph.email_2_user[node]] + component)
        return res
                    
# Approach 2: build the graph during union find. One trick is to convert the email to id
# parse the accounts to make a graph
# find the connected component of the graph (use disjoint set union)
# output the answer
# time: O(sigma ai*logai), where ai is the length of accounts[i]
class DSU(object):
    def __init__(self):
        self.num_of_item = 10001
        self.par = list(range(self.num_of_item))
        self.rnk = [0] * self.num_of_item

    def find(self, x):
        if self.par[x] != x:
            self.par[x] = self.find(self.par[x])
        return self.par[x]

    def union(self, x, y):
        xr, yr = self.find(x), self.find(y)
        if xr == yr:
            return False
        elif self.rnk[xr] < self.rnk[yr]:
            self.par[xr] = yr
        elif self.rnk[xr] > self.rnk[yr]:
            self.par[yr] = xr
        else:
            self.par[yr] = xr
            self.rnk[xr] += 1
        return True

        
        
class Solution(object):
    def accountsMerge(self, accounts):
        """
        :type accounts: List[List[str]]
        :rtype: List[List[str]]
        """
        # parse the accounts to make a graph
        # find the connected component of the graph
        # DSU approach
        dsu = DSU()
        email2id = {}
        email2name = {}
        cur_id = 0
        for account in accounts:
            user_name = account[0]
            for email in account[1:]:
                if email not in email2id:
                    email2id[email] = cur_id
                    cur_id += 1
                    email2name[email] = user_name
                dsu.union(email2id[email], email2id[account[1]])
        ans = collections.defaultdict(lambda: list())
        for email in email2id:
            ans[dsu.find(email2id[email])].append(email)
        res = []
        for email_id in ans:
            user_name = email2name[ans[email_id][0]]
            emails = sorted(ans[email_id])
            res.append([user_name] + emails)
        return res
        