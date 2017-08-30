/*
There are N gas stations along a circular route, where the amount of gas at station i is gas[i].

You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from station i to its next station (i+1). You begin the journey with an empty tank at one of the gas stations.

Return the starting gas station's index if you can travel around the circuit once, otherwise return -1
*/
// O(N*N) Time Limit Exceeded
class Solution {
public:
    int canCompleteCircuit(vector<int>& gas, vector<int>& cost) {
        int N = gas.size();
        for(int start = 0; start < N; start++) {
            bool temp = true;
            for (int next = 1; next <= N; next++) {
                if (!isAble(gas, cost, start, next, N)) {
                    temp = false;
                    break;
                }
            }
            if (temp == true)
                return start;
        }
        return -1;
    }
    bool isAble(vector<int>& gas, vector<int>& cost, int start, int next, int size) {
        int gas_cur = 0; int cost_cur = 0;
        for (int i = 0; i < next; i++) {
            gas_cur += gas[(start + i) % size];
            cost_cur += cost[(start + i) % size];
        }
        if (gas_cur < cost_cur)
            return false;
        else
            return true;
    }
};

// O(N)
/*
key point:
1. If car starts at A and can not reach B. Any station between A and B can not reach B.(B is the first station that A can not reach.)
2. If the total number of gas is bigger than the total number of cost. There must be a solution.
*/
class Solution {
public:
	int canCompleteCircuit(vector<int> &gas, vector<int> &cost) {
		int total = 0;
		int j = -1;
		for (int i = 0, sum = 0; i < gas.size(); ++i) {
			sum += gas[i] - cost[i];
			total += gas[i] - cost[i];
			if (sum < 0) {
				j = i;
				sum = 0;
			}
		}
		return total >= 0 ? j + 1 : -1;
	}
};