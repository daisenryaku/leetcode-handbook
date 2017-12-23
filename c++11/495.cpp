class Solution {
public:
    int findPoisonedDuration(vector<int>& timeSeries, int duration) {
        int size = timeSeries.size();
        int ans = duration * size;
        for (int i=1; i<size; ++i) {
            ans -= max(0, duration-(timeSeries[i] - timeSeries[i-1]));
        }
        return ans;
    }
};
