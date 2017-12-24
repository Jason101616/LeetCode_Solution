// Given n points on a 2D plane, find the maximum number of points that lie on the same straight line.

// 每次迭代以某一个点为基准， 看后面每一个点跟它构成的直线， 维护一个HashMap， key是跟这个点构成直线的斜率的值， 而value就是该斜率对应的点的数量， 计算它的斜率， 如果已经存在， 那么就多添加一个点， 否则创建新的key。 这里只需要考虑斜率而不用考虑截距是因为所有点都是对应于一个参考点构成的直线， 只要斜率相同就必然在同一直线上。 最后取map中最大的值， 就是通过这个点的所有直线上最多的点的数量。 对于每一个点都做一次这种计算， 并且后面的点不需要看扫描过的点的情况了， 因为如果这条直线是包含最多点的直线并且包含前面的点， 那么前面的点肯定统计过这条直线了。 因此算法总共需要两层循环， 外层进行点的迭代， 内层扫描剩下的点进行统计， 时间复杂度是O（n^2), 空间复杂度是哈希表的大小， 也就是O（n)

// 注意java会有精度的问题，因此这种方法并不能通过OJ
public int maxPoints(Point[] points) {
    if (points == null || points.length == 0) return 0;
    int max = 1;
    double ratio = 0.0;
    for (int i = 0; i < points.length - 1; i++) 
    {
        HashMap<Double, Integer> map = new HashMap<Double, Integer>();
        int numofSame = 0;
        int localMax = 1;
        for (int j = i + 1; j < points.length; j++) 
        {
            if(points[j].x == points[i].x && points[j].y == points[i].y) {
                numofSame++;
                continue;
            }
            else if(points[j].x == points[i].x)
            {
                ratio = (double) Integer.MAX_VALUE;
            }
            else if(points[j].y == points[i].y)
            {
                ratio = 0.0;
            }
            else
            {
                ratio = (double) (points[j].y - points[i].y) / (double) (points[j].x - points[i].x);
            }
            int num;
            if (map.containsKey(ratio)) 
            {
                num = map.get(ratio)+1;
                
            }
            else 
            {
                num = 2;
            }
            map.put(ratio, num);
        }
        for (Integer value : map.values()) 
        {
            localMax = Math.max(localMax, value);
        }
        localMax += numofSame;
        max = Math.max(max, localMax);
    }
    return max;
}



// appoach 2: save the largest common divisor in the hashmap (C++)
class Solution {
    public:
        int maxPoints(vector<Point>& points) {
            int res = 0;
            for (int i = 0; i < points.size(); ++i) {
                map<pair<int, int>, int> m;
                int duplicate = 1;
                for (int j = i + 1; j < points.size(); ++j) {
                    if (points[i].x == points[j].x && points[i].y == points[j].y) {
                        ++duplicate; continue;
                    } 
                    int dx = points[j].x - points[i].x;
                    int dy = points[j].y - points[i].y;
                    int d = gcd(dx, dy);
                    ++m[{dx / d, dy / d}];
                }
                res = max(res, duplicate);
                for (auto it = m.begin(); it != m.end(); ++it) {
                    res = max(res, it->second + duplicate);
                }
            }
            return res;
        }
        int gcd(int a, int b) {
            return (b == 0) ? a : gcd(b, a % b);
        }
    };