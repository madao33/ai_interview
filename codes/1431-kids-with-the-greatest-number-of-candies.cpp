class Solution {
public:
    vector<bool> kidsWithCandies(vector<int>& candies, int extraCandies) {
        int maxCandy = *max_element(candies.begin(), candies.end());
        int len = candies.size();
        vector<bool> res;
        for (int i = 0; i < len; i++) {
            if (candies[i] >= maxCandy - extraCandies) {
                res.push_back(true);
            } else {
                res.push_back(false);
            }
        }
        return res;
    }
};