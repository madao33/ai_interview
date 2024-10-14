class Solution {
public:
    string reverseVowels(string s) {
        auto isVowel = [vowels = "aeiouAEIOU"s](char ch) {
            return vowels.find(ch) != string::npos;
        };

        int left = 0, right = s.size() - 1;
        while(left < right) {
            while(left < right && !isVowel(s[left])) {
                ++left;
            }
            while(left < right && !isVowel(s[right])) {
                --right;
            }
            if (left < right) {
                swap(s[left], s[right]);
                ++left;
                --right;
            }
        }
        return s;
    }
};