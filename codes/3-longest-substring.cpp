#include <iostream>
#include <set>

class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        unordered_set<char> repeated;
        int n = s.size();
        int r = -1, ans = 0;
        for (int l = 0; l < n; l++) {
            if (l != 0) {
                repeated.erase(s[l-1]);
            }
            while(r + 1 < n && !repeated.count(s[r + 1])) {
                repeated.insert(s[r+1]);
                ++r;
            }
            ans = max(ans, r - l + 1);
        }
        return ans;
    }
};