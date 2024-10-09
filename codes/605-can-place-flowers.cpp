class Solution {
public:
    bool canPlaceFlowers(vector<int>& flowerbed, int n) {
        int len = flowerbed.size(), res = 0;
        if (len == 1 and flowerbed[0] == 0) return 1>=n; 
        if (len >= 2) {
            if (flowerbed[0] == 0 && flowerbed[1] == 0) {
                flowerbed[0] = 1;
                ++res;
            }

            if (flowerbed[len-2] == 0 && flowerbed[len - 1] == 0) {
                flowerbed[len-1] = 1;
                ++res;
            }
        } 
        for (int i = 1; i < len - 1; i++) {
            if (flowerbed[i-1] == 0 && flowerbed[i] == 0 && flowerbed[i + 1] == 0) {
                flowerbed[i] = 1;
                ++res;
            }
        }
        return res >= n;
    }
};