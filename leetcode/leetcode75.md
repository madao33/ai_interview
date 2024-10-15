



## [3. 无重复字符的最长子串](https://leetcode.cn/problems/longest-substring-without-repeating-characters/)

中等



相关标签

相关企业



提示



给定一个字符串 `s` ，请你找出其中不含有重复字符的 **最长** 

**子串**

 的长度。



 

**示例 1:**

```
输入: s = "abcabcbb"
输出: 3 
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
```

**示例 2:**

```
输入: s = "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
```

**示例 3:**

```
输入: s = "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
```

 

**提示：**

- `0 <= s.length <= 5 * 104`
- `s` 由英文字母、数字、符号和空格组成

题解

转换为双指针问题，相当于求解两个重复字符最大的距离

```c++
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
```

## [146. LRU 缓存](https://leetcode.cn/problems/lru-cache/)

中等



相关标签

相关企业



请你设计并实现一个满足 [LRU (最近最少使用) 缓存](https://baike.baidu.com/item/LRU) 约束的数据结构。

实现 `LRUCache` 类：

- `LRUCache(int capacity)` 以 **正整数** 作为容量 `capacity` 初始化 LRU 缓存
- `int get(int key)` 如果关键字 `key` 存在于缓存中，则返回关键字的值，否则返回 `-1` 。
- `void put(int key, int value)` 如果关键字 `key` 已经存在，则变更其数据值 `value` ；如果不存在，则向缓存中插入该组 `key-value` 。如果插入操作导致关键字数量超过 `capacity` ，则应该 **逐出** 最久未使用的关键字。

函数 `get` 和 `put` 必须以 `O(1)` 的平均时间复杂度运行。

 

**示例：**

```
输入
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
输出
[null, null, null, 1, null, -1, null, -1, 3, 4]

解释
LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 1); // 缓存是 {1=1}
lRUCache.put(2, 2); // 缓存是 {1=1, 2=2}
lRUCache.get(1);    // 返回 1
lRUCache.put(3, 3); // 该操作会使得关键字 2 作废，缓存是 {1=1, 3=3}
lRUCache.get(2);    // 返回 -1 (未找到)
lRUCache.put(4, 4); // 该操作会使得关键字 1 作废，缓存是 {4=4, 3=3}
lRUCache.get(1);    // 返回 -1 (未找到)
lRUCache.get(3);    // 返回 3
lRUCache.get(4);    // 返回 4
```

 

**提示：**

- `1 <= capacity <= 3000`
- `0 <= key <= 10000`
- `0 <= value <= 105`
- 最多调用 `2 * 105` 次 `get` 和 `put`

**题解**

```c++
struct DLinkedNode {
    int key, value;
    DLinkedNode* prev;
    DLinkedNode* next;
    DLinkedNode(): key(0), value(0), prev(nullptr), next(nullptr){}
    DLinkedNode(int _key, int _value): key(_key), value(_value), prev(nullptr), next(nullptr) {}
};

class LRUCache {
private:
    unordered_map<int, DLinkedNode*> key_map;
    DLinkedNode* head;
    DLinkedNode* tail;
    int size;
    int capacity;

public:
    LRUCache(int _capacity): capacity(_capacity), size(0){
        head = new DLinkedNode();
        tail = new DLinkedNode();
        head->next = tail;
        tail->prev = head;
    }

    void addToHead(DLinkedNode* node) {
        node->prev = head;
        node->next = head->next;
        head->next->prev = node;
        head->next = node;
    }

    void removeNode(DLinkedNode* node) {
        node->prev->next = node->next;
        node->next->prev = node->prev;
    }

    void moveToHead(DLinkedNode* node) {
        removeNode(node);
        addToHead(node);
    }

    DLinkedNode* removeTail() {
        DLinkedNode* node = tail->prev;
        removeNode(node);
        return node;
    }
    
    int get(int key) {
        if (!key_map.count(key)) {
            return -1;
        }
        
        // 存在key，返回对应value，并将当前node移动到链表头
        DLinkedNode* node = key_map[key];
        moveToHead(node);
        return node->value;
    }
    
    void put(int key, int value) {
        if (!key_map.count(key)){
            DLinkedNode* node = new DLinkedNode(key, value);
            key_map[key] = node;
            addToHead(node);
            ++size;
            if (size > capacity){
                DLinkedNode* removed = removeTail();
                key_map.erase(removed->key);
                delete removed;
                --size;
            }

        } else {
            DLinkedNode* node = key_map[key];
            node->value = value;
            moveToHead(node);
        }
    }

    
};

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache* obj = new LRUCache(capacity);
 * int param_1 = obj->get(key);
 * obj->put(key,value);
 */
```



# 数组/字符串

## [1768. 交替合并字符串](https://leetcode.cn/problems/merge-strings-alternately/)

已解答

简单



相关标签

相关企业



提示



给你两个字符串 `word1` 和 `word2` 。请你从 `word1` 开始，通过交替添加字母来合并字符串。如果一个字符串比另一个字符串长，就将多出来的字母追加到合并后字符串的末尾。

返回 **合并后的字符串** 。

 

**示例 1：**

```
输入：word1 = "abc", word2 = "pqr"
输出："apbqcr"
解释：字符串合并情况如下所示：
word1：  a   b   c
word2：    p   q   r
合并后：  a p b q c r
```

**示例 2：**

```
输入：word1 = "ab", word2 = "pqrs"
输出："apbqrs"
解释：注意，word2 比 word1 长，"rs" 需要追加到合并后字符串的末尾。
word1：  a   b 
word2：    p   q   r   s
合并后：  a p b q   r   s
```

**示例 3：**

```
输入：word1 = "abcd", word2 = "pq"
输出："apbqcd"
解释：注意，word1 比 word2 长，"cd" 需要追加到合并后字符串的末尾。
word1：  a   b   c   d
word2：    p   q 
合并后：  a p b q c   d
```

 

**提示：**

- `1 <= word1.length, word2.length <= 100`
- `word1` 和 `word2` 由小写英文字母组成

**题解**

```c++
class Solution {
public:
    string mergeAlternately(string word1, string word2) {
        int m = word1.size(), n = word2.size();
        int i = 0, j = 0;
        
        string ans;
        ans.reserve(m + n);
        while(i < m || j < n) {
            if (i < m) {
                ans.push_back(word1[i]);
                ++i;
            }

            if (j < n) {
                ans.push_back(word2[j]);
                ++j;
            }
        }

        return ans;
    }
};
```

**题解**

```c++
class Solution {
public:
    string gcdOfStrings(string str1, string str2) {
        if (str1 + str2 != str2 + str1) return "";
        return str1.substr(0, gcd(str1.length(), str2.length()));
    }
};
```

## [1431. 拥有最多糖果的孩子](https://leetcode.cn/problems/kids-with-the-greatest-number-of-candies/)

简单



相关标签

相关企业



提示



有 `n` 个有糖果的孩子。给你一个数组 `candies`，其中 `candies[i]` 代表第 `i` 个孩子拥有的糖果数目，和一个整数 `extraCandies` 表示你所有的额外糖果的数量。

返回一个长度为 `n` 的布尔数组 `result`，如果把所有的 `extraCandies` 给第 `i` 个孩子之后，他会拥有所有孩子中 **最多** 的糖果，那么 `result[i]` 为 `true`，否则为 `false`。

注意，允许有多个孩子同时拥有 **最多** 的糖果数目。

 

**示例 1：**

```
输入：candies = [2,3,5,1,3], extraCandies = 3
输出：[true,true,true,false,true] 
解释：如果你把额外的糖果全部给：
孩子 1，将有 2 + 3 = 5 个糖果，是孩子中最多的。
孩子 2，将有 3 + 3 = 6 个糖果，是孩子中最多的。
孩子 3，将有 5 + 3 = 8 个糖果，是孩子中最多的。
孩子 4，将有 1 + 3 = 4 个糖果，不是孩子中最多的。
孩子 5，将有 3 + 3 = 6 个糖果，是孩子中最多的。
```

**示例 2：**

```
输入：candies = [4,2,1,1,2], extraCandies = 1
输出：[true,false,false,false,false] 
解释：只有 1 个额外糖果，所以不管额外糖果给谁，只有孩子 1 可以成为拥有糖果最多的孩子。
```

**示例 3：**

```
输入：candies = [12,1,12], extraCandies = 10
输出：[true,false,true]
```

 

**提示：**

- `n == candies.length`
- `2 <= n <= 100`
- `1 <= candies[i] <= 100`
- `1 <= extraCandies <= 50`

**题解**

```c++
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
```

## [605. 种花问题](https://leetcode.cn/problems/can-place-flowers/)

简单



相关标签

相关企业



假设有一个很长的花坛，一部分地块种植了花，另一部分却没有。可是，花不能种植在相邻的地块上，它们会争夺水源，两者都会死去。

给你一个整数数组 `flowerbed` 表示花坛，由若干 `0` 和 `1` 组成，其中 `0` 表示没种植花，`1` 表示种植了花。另有一个数 `n` ，能否在不打破种植规则的情况下种入 `n` 朵花？能则返回 `true` ，不能则返回 `false` 。

 

**示例 1：**

```
输入：flowerbed = [1,0,0,0,1], n = 1
输出：true
```

**示例 2：**

```
输入：flowerbed = [1,0,0,0,1], n = 2
输出：false
```

 

**提示：**

- `1 <= flowerbed.length <= 2 * 104`
- `flowerbed[i]` 为 `0` 或 `1`
- `flowerbed` 中不存在相邻的两朵花
- `0 <= n <= flowerbed.length`

**题解**

```c++
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
```

## [345. 反转字符串中的元音字母](https://leetcode.cn/problems/reverse-vowels-of-a-string/)

简单



相关标签

相关企业



给你一个字符串 `s` ，仅反转字符串中的所有元音字母，并返回结果字符串。

元音字母包括 `'a'`、`'e'`、`'i'`、`'o'`、`'u'`，且可能以大小写两种形式出现不止一次。

 

**示例 1：**

**输入：**s = "IceCreAm"

**输出：**"AceCreIm"

**解释：**

`s` 中的元音是 `['I', 'e', 'e', 'A']`。反转这些元音，`s` 变为 `"AceCreIm"`.

**示例 2：**

**输入：**s = "leetcode"

**输出：**"leotcede"

 

**提示：**

- `1 <= s.length <= 3 * 105`
- `s` 由 **可打印的 ASCII** 字符组成

**题解**

```c++
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
```

## [151. 反转字符串中的单词](https://leetcode.cn/problems/reverse-words-in-a-string/)

中等



相关标签

相关企业



给你一个字符串 `s` ，请你反转字符串中 **单词** 的顺序。

**单词** 是由非空格字符组成的字符串。`s` 中使用至少一个空格将字符串中的 **单词** 分隔开。

返回 **单词** 顺序颠倒且 **单词** 之间用单个空格连接的结果字符串。

**注意：**输入字符串 `s`中可能会存在前导空格、尾随空格或者单词间的多个空格。返回的结果字符串中，单词间应当仅用单个空格分隔，且不包含任何额外的空格。

 

**示例 1：**

```
输入：s = "the sky is blue"
输出："blue is sky the"
```

**示例 2：**

```
输入：s = "  hello world  "
输出："world hello"
解释：反转后的字符串中不能存在前导空格和尾随空格。
```

**示例 3：**

```
输入：s = "a good   example"
输出："example good a"
解释：如果两个单词间有多余的空格，反转后的字符串需要将单词间的空格减少到仅有一个。
```

 

**提示：**

- `1 <= s.length <= 104`
- `s` 包含英文大小写字母、数字和空格 `' '`
- `s` 中 **至少存在一个** 单词

 

**进阶：**如果字符串在你使用的编程语言中是一种可变数据类型，请尝试使用 `O(1)` 额外空间复杂度的 **原地** 解法。

**题解**

```python
class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()
        i = j = len(s) - 1
        res = []
        while i >= 0:
            while i >= 0 and s[i] != ' ': i -= 1
            res.append(s[i+1:j+1])
            while i >= 0 and s[i] == ' ': i -= 1
            j = i
        return ' '.join(res)
```

## [238. 除自身以外数组的乘积](https://leetcode.cn/problems/product-of-array-except-self/)

中等



相关标签

相关企业



提示



给你一个整数数组 `nums`，返回 数组 `answer` ，其中 `answer[i]` 等于 `nums` 中除 `nums[i]` 之外其余各元素的乘积 。

题目数据 **保证** 数组 `nums`之中任意元素的全部前缀元素和后缀的乘积都在 **32 位** 整数范围内。

请 **不要使用除法，**且在 `O(n)` 时间复杂度内完成此题。

 

**示例 1:**

```
输入: nums = [1,2,3,4]
输出: [24,12,8,6]
```

**示例 2:**

```
输入: nums = [-1,1,0,-3,3]
输出: [0,0,9,0,0]
```

 

**提示：**

- `2 <= nums.length <= 105`
- `-30 <= nums[i] <= 30`
- **保证** 数组 `nums`之中任意元素的全部前缀元素和后缀的乘积都在 **32 位** 整数范围内

 

**进阶：**你可以在 `O(1)` 的额外空间复杂度内完成这个题目吗？（ 出于对空间复杂度分析的目的，输出数组 **不被视为** 额外空间。）

**题解**

```python
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        N = len(nums)
        prev, back = [1 for i in range(N+1)], [1 for i in range(N+1)]
        for i in range(N):
            prev[i+1] = prev[i] * nums[i]
            back[N-i-1] = back[N-i] * nums[N-i-1]
        res = [prev[i] * back[i+1] for i in range(N)]
        return res
```

## [334. 递增的三元子序列](https://leetcode.cn/problems/increasing-triplet-subsequence/)

中等



相关标签

相关企业



给你一个整数数组 `nums` ，判断这个数组中是否存在长度为 `3` 的递增子序列。

如果存在这样的三元组下标 `(i, j, k)` 且满足 `i < j < k` ，使得 `nums[i] < nums[j] < nums[k]` ，返回 `true` ；否则，返回 `false` 。

 

**示例 1：**

```
输入：nums = [1,2,3,4,5]
输出：true
解释：任何 i < j < k 的三元组都满足题意
```

**示例 2：**

```
输入：nums = [5,4,3,2,1]
输出：false
解释：不存在满足题意的三元组
```

**示例 3：**

```
输入：nums = [2,1,5,0,4,6]
输出：true
解释：三元组 (3, 4, 5) 满足题意，因为 nums[3] == 0 < nums[4] == 4 < nums[5] == 6
```

 

**提示：**

- `1 <= nums.length <= 5 * 105`
- `-231 <= nums[i] <= 231 - 1`

 

**进阶：**你能实现时间复杂度为 `O(n)` ，空间复杂度为 `O(1)` 的解决方案吗？

**题解**

```python
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        N = len(nums)
        if N < 3:
            return False
        first, second = nums[0], float('inf')
        i = 0
        for i in range(1, N):
            num = nums[i]
            if num > second:
                return True
            if num > first:
                second = num
            else:
                first = num
        return False
```

## [443. 压缩字符串](https://leetcode.cn/problems/string-compression/)

中等



相关标签

相关企业



提示



给你一个字符数组 `chars` ，请使用下述算法压缩：

从一个空字符串 `s` 开始。对于 `chars` 中的每组 **连续重复字符** ：

- 如果这一组长度为 `1` ，则将字符追加到 `s` 中。
- 否则，需要向 `s` 追加字符，后跟这一组的长度。

压缩后得到的字符串 `s` **不应该直接返回** ，需要转储到字符数组 `chars` 中。需要注意的是，如果组长度为 `10` 或 `10` 以上，则在 `chars` 数组中会被拆分为多个字符。

请在 **修改完输入数组后** ，返回该数组的新长度。

你必须设计并实现一个只使用常量额外空间的算法来解决此问题。

 

**示例 1：**

```
输入：chars = ["a","a","b","b","c","c","c"]
输出：返回 6 ，输入数组的前 6 个字符应该是：["a","2","b","2","c","3"]
解释："aa" 被 "a2" 替代。"bb" 被 "b2" 替代。"ccc" 被 "c3" 替代。
```

**示例 2：**

```
输入：chars = ["a"]
输出：返回 1 ，输入数组的前 1 个字符应该是：["a"]
解释：唯一的组是“a”，它保持未压缩，因为它是一个字符。
```

**示例 3：**

```
输入：chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
输出：返回 4 ，输入数组的前 4 个字符应该是：["a","b","1","2"]。
解释：由于字符 "a" 不重复，所以不会被压缩。"bbbbbbbbbbbb" 被 “b12” 替代。
```

 

**提示：**

- `1 <= chars.length <= 2000`
- `chars[i]` 可以是小写英文字母、大写英文字母、数字或符号

**题解**

```python
class Solution:
    def compress(self, chars: List[str]) -> int:
        N = len(chars)
        if N <= 1:
            return N
        prevCnt = 1
        left = 0
        for i in range(N):
            if i == N - 1 or chars[i] != chars[i+1]:
                chars[left] = chars[i]
                left += 1
                if prevCnt > 1:
                    for ch in str(prevCnt):
                        chars[left] = ch
                        left += 1
                prevCnt = 1
            else:
                prevCnt += 1
        return left
```



# 双指针

## [283. 移动零](https://leetcode.cn/problems/move-zeroes/)

简单



相关标签

相关企业



提示



给定一个数组 `nums`，编写一个函数将所有 `0` 移动到数组的末尾，同时保持非零元素的相对顺序。

**请注意** ，必须在不复制数组的情况下原地对数组进行操作。

 

**示例 1:**

```
输入: nums = [0,1,0,3,12]
输出: [1,3,12,0,0]
```

**示例 2:**

```
输入: nums = [0]
输出: [0]
```

 

**提示**:

- `1 <= nums.length <= 104`
- `-231 <= nums[i] <= 231 - 1`

 

**进阶：**你能尽量减少完成的操作次数吗？

**题解**

```python
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        N = len(nums)
        z_ptr = 0
        for i in range(N):
            if nums[i] != 0:
                nums[z_ptr] = nums[i]
                z_ptr += 1
        for j in range(z_ptr, N):
            nums[j] = 0
            
```

## [392. 判断子序列](https://leetcode.cn/problems/is-subsequence/)

简单



相关标签

相关企业



给定字符串 **s** 和 **t** ，判断 **s** 是否为 **t** 的子序列。

字符串的一个子序列是原始字符串删除一些（也可以不删除）字符而不改变剩余字符相对位置形成的新字符串。（例如，`"ace"`是`"abcde"`的一个子序列，而`"aec"`不是）。

**进阶：**

如果有大量输入的 S，称作 S1, S2, ... , Sk 其中 k >= 10亿，你需要依次检查它们是否为 T 的子序列。在这种情况下，你会怎样改变代码？

**致谢：**

特别感谢 [@pbrother ](https://leetcode.com/pbrother/)添加此问题并且创建所有测试用例。

 

**示例 1：**

```
输入：s = "abc", t = "ahbgdc"
输出：true
```

**示例 2：**

```
输入：s = "axc", t = "ahbgdc"
输出：false
```

 

**提示：**

- `0 <= s.length <= 100`
- `0 <= t.length <= 10^4`
- 两个字符串都只由小写字符组成。

**题解**

```python
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        N1, N2 = len(s), len(t)
        if N1 == 0:
            return True
        i, j = 0, 0
        while i < N1 and j < N2:
            if s[i] == t[j]:
                i += 1
                j += 1
            else:
                j += 1
            if i == N1:
                return True
        return False
```



## [11. 盛最多水的容器](https://leetcode.cn/problems/container-with-most-water/)

中等



相关标签

相关企业



提示



给定一个长度为 `n` 的整数数组 `height` 。有 `n` 条垂线，第 `i` 条线的两个端点是 `(i, 0)` 和 `(i, height[i])` 。

找出其中的两条线，使得它们与 `x` 轴共同构成的容器可以容纳最多的水。

返回容器可以储存的最大水量。

**说明：**你不能倾斜容器。

 

**示例 1：**

![img](assets/question_11.jpg)

```
输入：[1,8,6,2,5,4,8,3,7]
输出：49 
解释：图中垂直线代表输入数组 [1,8,6,2,5,4,8,3,7]。在此情况下，容器能够容纳水（表示为蓝色部分）的最大值为 49。
```

**示例 2：**

```
输入：height = [1,1]
输出：1
```

 

**提示：**

- `n == height.length`
- `2 <= n <= 105`
- `0 <= height[i] <= 104`

**题解**

双指针分别指向开头和结尾，每次移动高度最低的指针，直到相遇

```python
class Solution:

    def getArea(self, height: List[int], left: int, right: int) -> int:
        return min(height[left], height[right]) * (right - left)
    
    def maxArea(self, height: List[int]) -> int:
        N = len(height)
        left, right = 0, N-1
        res = self.getArea(height, left, right)
        while left < right:
            if height[left] < height[right]:
                left += 1
                res = max(self.getArea(height, left, right), res)
            else:
                right -= 1
                res = max(self.getArea(height, left, right), res)
        return res
```



## [1679. K 和数对的最大数目](https://leetcode.cn/problems/max-number-of-k-sum-pairs/)

中等



相关标签

相关企业



提示



给你一个整数数组 `nums` 和一个整数 `k` 。

每一步操作中，你需要从数组中选出和为 `k` 的两个整数，并将它们移出数组。

返回你可以对数组执行的最大操作数。

 

**示例 1：**

```
输入：nums = [1,2,3,4], k = 5
输出：2
解释：开始时 nums = [1,2,3,4]：
- 移出 1 和 4 ，之后 nums = [2,3]
- 移出 2 和 3 ，之后 nums = []
不再有和为 5 的数对，因此最多执行 2 次操作。
```

**示例 2：**

```
输入：nums = [3,1,3,4,3], k = 6
输出：1
解释：开始时 nums = [3,1,3,4,3]：
- 移出前两个 3 ，之后nums = [1,4,3]
不再有和为 6 的数对，因此最多执行 1 次操作。
```

 

**提示：**

- `1 <= nums.length <= 105`
- `1 <= nums[i] <= 109`
- `1 <= k <= 109`

**题解**

先对数组进行排序，然后双指针分别指向0， N-1

```python
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        list.sort(nums)
        N = len(nums)
        left, right = 0, N - 1
        res = 0
        while left < right:
            if nums[left] + nums[right] > k:
                right -= 1
            elif nums[left] + nums[right] < k:
                left += 1
            else:
                res += 1
                left += 1
                right -= 1
        return res

```

# 滑动窗口

## [643. 子数组最大平均数 I](https://leetcode.cn/problems/maximum-average-subarray-i/)

简单



相关标签

相关企业



给你一个由 `n` 个元素组成的整数数组 `nums` 和一个整数 `k` 。

请你找出平均数最大且 **长度为 `k`** 的连续子数组，并输出该最大平均数。

任何误差小于 `10-5` 的答案都将被视为正确答案。

 

**示例 1：**

```
输入：nums = [1,12,-5,-6,50,3], k = 4
输出：12.75
解释：最大平均数 (12-5-6+50)/4 = 51/4 = 12.75
```

**示例 2：**

```
输入：nums = [5], k = 1
输出：5.00000
```

 

**提示：**

- `n == nums.length`
- `1 <= k <= n <= 105`
- `-104 <= nums[i] <= 104`

**题解**

```python
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        res = sum(nums[:k])
        temp = res
        for i in range(k, len(nums)):
            temp += nums[i]
            temp -= nums[i-k]
            res = max(res, temp)
        return res / k
```



## [1456. 定长子串中元音的最大数目](https://leetcode.cn/problems/maximum-number-of-vowels-in-a-substring-of-given-length/)

中等



相关标签

相关企业



提示



给你字符串 `s` 和整数 `k` 。

请返回字符串 `s` 中长度为 `k` 的单个子字符串中可能包含的最大元音字母数。

英文中的 **元音字母** 为（`a`, `e`, `i`, `o`, `u`）。

 

**示例 1：**

```
输入：s = "abciiidef", k = 3
输出：3
解释：子字符串 "iii" 包含 3 个元音字母。
```

**示例 2：**

```
输入：s = "aeiou", k = 2
输出：2
解释：任意长度为 2 的子字符串都包含 2 个元音字母。
```

**示例 3：**

```
输入：s = "leetcode", k = 3
输出：2
解释："lee"、"eet" 和 "ode" 都包含 2 个元音字母。
```

**示例 4：**

```
输入：s = "rhythms", k = 4
输出：0
解释：字符串 s 中不含任何元音字母。
```

**示例 5：**

```
输入：s = "tryhard", k = 4
输出：1
```

 

**提示：**

- `1 <= s.length <= 10^5`
- `s` 由小写英文字母组成
- `1 <= k <= s.length`

**题解**

```python
class Solution:

    def isVowels(self, s: str) -> bool:
        return s in "aeiou"

    def maxVowels(self, s: str, k: int) -> int:
        N = len(s)
        vowels = [1 if self.isVowels(s[i]) else 0 for i in range(N)]
        res = sum(vowels[:k])
        temp = res
        for i in range(k, N):
            temp += vowels[i]
            temp -= vowels[i-k]
            res = max(res, temp)
        return res
```



## [1004. 最大连续1的个数 III](https://leetcode.cn/problems/max-consecutive-ones-iii/)

中等



相关标签

相关企业



提示



给定一个二进制数组 `nums` 和一个整数 `k`，如果可以翻转最多 `k` 个 `0` ，则返回 *数组中连续 `1` 的最大个数* 。

 

**示例 1：**

```
输入：nums = [1,1,1,0,0,0,1,1,1,1,0], K = 2
输出：6
解释：[1,1,1,0,0,1,1,1,1,1,1]
粗体数字从 0 翻转到 1，最长的子数组长度为 6。
```

**示例 2：**

```
输入：nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], K = 3
输出：10
解释：[0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
粗体数字从 0 翻转到 1，最长的子数组长度为 10。
```

 

**提示：**

- `1 <= nums.length <= 105`
- `nums[i]` 不是 `0` 就是 `1`
- `0 <= k <= nums.length`



**题解**

转化为滑动窗口内最多有k个0的子区间长度为多大，有两个变量维护左右区间0的前缀和

```python
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        lsum, rsum = 0, 0
        ans = 0
        N = len(nums)
        left = 0
        for right in range(N):
            rsum += 1 - nums[right]
            while rsum - lsum > k:
                lsum += 1 - nums[left]
                left += 1
            ans = max(ans, right - left + 1)
        return ans
```



## [1493. 删掉一个元素以后全为 1 的最长子数组](https://leetcode.cn/problems/longest-subarray-of-1s-after-deleting-one-element/)

中等



相关标签

相关企业



提示



给你一个二进制数组 `nums` ，你需要从中删掉一个元素。

请你在删掉元素的结果数组中，返回最长的且只包含 1 的非空子数组的长度。

如果不存在这样的子数组，请返回 0 。

 

**提示 1：**

```
输入：nums = [1,1,0,1]
输出：3
解释：删掉位置 2 的数后，[1,1,1] 包含 3 个 1 。
```

**示例 2：**

```
输入：nums = [0,1,1,1,0,1,1,0,1]
输出：5
解释：删掉位置 4 的数字后，[0,1,1,1,1,1,0,1] 的最长全 1 子数组为 [1,1,1,1,1] 。
```

**示例 3：**

```
输入：nums = [1,1,1]
输出：2
解释：你必须要删除一个元素。
```

 

**提示：**

- `1 <= nums.length <= 105`
- `nums[i]` 要么是 `0` 要么是 `1` 。



**题解**

```python
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        N = len(nums)
        if sum(nums) == N:
            return N - 1
        lsum, rsum = 0, 0
        left, ans = 0, 0
        for right in range(N):
            rsum += 1 - nums[right]
            while rsum - lsum > 1:
                lsum += 1 - nums[left]
                left += 1
            ans = max(ans, right - left + 1 - rsum + lsum)
        return ans
```

# 前缀和

## [1732. 找到最高海拔](https://leetcode.cn/problems/find-the-highest-altitude/)

简单



相关标签

相关企业



提示



有一个自行车手打算进行一场公路骑行，这条路线总共由 `n + 1` 个不同海拔的点组成。自行车手从海拔为 `0` 的点 `0` 开始骑行。

给你一个长度为 `n` 的整数数组 `gain` ，其中 `gain[i]` 是点 `i` 和点 `i + 1` 的 **净海拔高度差**（`0 <= i < n`）。请你返回 **最高点的海拔** 。

 

**示例 1：**

```
输入：gain = [-5,1,5,0,-7]
输出：1
解释：海拔高度依次为 [0,-5,-4,1,1,-6] 。最高海拔为 1 。
```

**示例 2：**

```
输入：gain = [-4,-3,-2,-1,4,3,2]
输出：0
解释：海拔高度依次为 [0,-4,-7,-9,-10,-6,-3,-1] 。最高海拔为 0 。
```

 

**提示：**

- `n == gain.length`
- `1 <= n <= 100`
- `-100 <= gain[i] <= 100`

**题解**

```python
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        ans, alti = 0, 0
        for n in gain:
            alti += n
            ans = max(ans, alti)
        return ans
```



## [724. 寻找数组的中心下标](https://leetcode.cn/problems/find-pivot-index/)

简单



相关标签

相关企业



提示



给你一个整数数组 `nums` ，请计算数组的 **中心下标** 。

数组 **中心下标** 是数组的一个下标，其左侧所有元素相加的和等于右侧所有元素相加的和。

如果中心下标位于数组最左端，那么左侧数之和视为 `0` ，因为在下标的左侧不存在元素。这一点对于中心下标位于数组最右端同样适用。

如果数组有多个中心下标，应该返回 **最靠近左边** 的那一个。如果数组不存在中心下标，返回 `-1` 。

 

**示例 1：**

```
输入：nums = [1, 7, 3, 6, 5, 6]
输出：3
解释：
中心下标是 3 。
左侧数之和 sum = nums[0] + nums[1] + nums[2] = 1 + 7 + 3 = 11 ，
右侧数之和 sum = nums[4] + nums[5] = 5 + 6 = 11 ，二者相等。
```

**示例 2：**

```
输入：nums = [1, 2, 3]
输出：-1
解释：
数组中不存在满足此条件的中心下标。
```

**示例 3：**

```
输入：nums = [2, 1, -1]
输出：0
解释：
中心下标是 0 。
左侧数之和 sum = 0 ，（下标 0 左侧不存在元素），
右侧数之和 sum = nums[1] + nums[2] = 1 + -1 = 0 。
```

 

**提示：**

- `1 <= nums.length <= 104`
- `-1000 <= nums[i] <= 1000`

 

**注意：**本题与主站 1991 题相同：https://leetcode-cn.com/problems/find-the-middle-index-in-array/



**题解**

```python
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        N = len(nums)
        lsum, rsum = [0 for i in range(N+1)], [0 for i in range(N+1)]
        for i in range(N):
            lsum[i+1] += lsum[i] + nums[i]
            rsum[N-i-1] = rsum[N-i] + nums[N-i-1]

        for i in range(N):
            if lsum[i] == rsum[i+1]:
                return i
        return -1
```

# 哈希表

## [2215. 找出两数组的不同](https://leetcode.cn/problems/find-the-difference-of-two-arrays/)

简单



相关标签

相关企业



提示



给你两个下标从 `0` 开始的整数数组 `nums1` 和 `nums2` ，请你返回一个长度为 `2` 的列表 `answer` ，其中：

- `answer[0]` 是 `nums1` 中所有 **不** 存在于 `nums2` 中的 **不同** 整数组成的列表。
- `answer[1]` 是 `nums2` 中所有 **不** 存在于 `nums1` 中的 **不同** 整数组成的列表。

**注意：**列表中的整数可以按 **任意** 顺序返回。

 

**示例 1：**

```
输入：nums1 = [1,2,3], nums2 = [2,4,6]
输出：[[1,3],[4,6]]
解释：
对于 nums1 ，nums1[1] = 2 出现在 nums2 中下标 0 处，然而 nums1[0] = 1 和 nums1[2] = 3 没有出现在 nums2 中。因此，answer[0] = [1,3]。
对于 nums2 ，nums2[0] = 2 出现在 nums1 中下标 1 处，然而 nums2[1] = 4 和 nums2[2] = 6 没有出现在 nums2 中。因此，answer[1] = [4,6]。
```

**示例 2：**

```
输入：nums1 = [1,2,3,3], nums2 = [1,1,2,2]
输出：[[3],[]]
解释：
对于 nums1 ，nums1[2] 和 nums1[3] 没有出现在 nums2 中。由于 nums1[2] == nums1[3] ，二者的值只需要在 answer[0] 中出现一次，故 answer[0] = [3]。
nums2 中的每个整数都在 nums1 中出现，因此，answer[1] = [] 。 
```

 

**提示：**

- `1 <= nums1.length, nums2.length <= 1000`
- `-1000 <= nums1[i], nums2[i] <= 1000`

**题解**

```python
class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        ans = [[], []]

        set1, set2 = set(nums1), set(nums2)
        for num in set2:
            if num not in set1:
                ans[1].append(num)

        for num in set1:
            if num not in set2:
                ans[0].append(num)

        return ans
```

[1207. 独一无二的出现次数](https://leetcode.cn/problems/unique-number-of-occurrences/)

简单



相关标签

相关企业



提示



给你一个整数数组 `arr`，如果每个数的出现次数都是独一无二的，就返回 `true`；否则返回 `false`。

 

**示例 1：**

```
输入：arr = [1,2,2,1,1,3]
输出：true
解释：在该数组中，1 出现了 3 次，2 出现了 2 次，3 只出现了 1 次。没有两个数的出现次数相同。
```

**示例 2：**

```
输入：arr = [1,2]
输出：false
```

**示例 3：**

```
输入：arr = [-3,0,1,-3,1,1,1,-3,10,0]
输出：true
```

 

**提示：**

- `1 <= arr.length <= 1000`
- `-1000 <= arr[i] <= 1000`

## [1207. 独一无二的出现次数](https://leetcode.cn/problems/unique-number-of-occurrences/)

简单



相关标签

相关企业



提示



给你一个整数数组 `arr`，如果每个数的出现次数都是独一无二的，就返回 `true`；否则返回 `false`。

 

**示例 1：**

```
输入：arr = [1,2,2,1,1,3]
输出：true
解释：在该数组中，1 出现了 3 次，2 出现了 2 次，3 只出现了 1 次。没有两个数的出现次数相同。
```

**示例 2：**

```
输入：arr = [1,2]
输出：false
```

**示例 3：**

```
输入：arr = [-3,0,1,-3,1,1,1,-3,10,0]
输出：true
```

 

**提示：**

- `1 <= arr.length <= 1000`
- `-1000 <= arr[i] <= 1000`

**题解**

```python
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        cntMap = dict()
        for a in arr:
            if a in cntMap:
                cntMap[a] += 1
            else:
                cntMap[a] = 1
        
        freqMap = set()
        for _, v in cntMap.items():
            if v in freqMap:
                return False
            else:
                freqMap.add(v)
        return True
```

## [1657. 确定两个字符串是否接近](https://leetcode.cn/problems/determine-if-two-strings-are-close/)

中等



相关标签

相关企业



提示



如果可以使用以下操作从一个字符串得到另一个字符串，则认为两个字符串 **接近** ：

- 操作 1：交换任意两个

   

  现有

   

  字符。

  - 例如，`abcde -> aecdb`

- 操作 2：将一个

   

  现有

   

  字符的每次出现转换为另一个

   

  现有

   

  字符，并对另一个字符执行相同的操作。

  - 例如，`aacabb -> bbcbaa`（所有 `a` 转化为 `b` ，而所有的 `b` 转换为 `a` ）

你可以根据需要对任意一个字符串多次使用这两种操作。

给你两个字符串，`word1` 和 `word2` 。如果 `word1` 和 `word2` **接近** ，就返回 `true` ；否则，返回 `false` 。

 

**示例 1：**

```
输入：word1 = "abc", word2 = "bca"
输出：true
解释：2 次操作从 word1 获得 word2 。
执行操作 1："abc" -> "acb"
执行操作 1："acb" -> "bca"
```

**示例 2：**

```
输入：word1 = "a", word2 = "aa"
输出：false
解释：不管执行多少次操作，都无法从 word1 得到 word2 ，反之亦然。
```

**示例 3：**

```
输入：word1 = "cabbba", word2 = "abbccc"
输出：true
解释：3 次操作从 word1 获得 word2 。
执行操作 1："cabbba" -> "caabbb"
执行操作 2："caabbb" -> "baaccc"
执行操作 2："baaccc" -> "abbccc"
```

**提示：**

- `1 <= word1.length, word2.length <= 105`
- `word1` 和 `word2` 仅包含小写英文字母



**题解**

```python
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        return set(word1) == set(word2) and Counter(Counter(word1).values()) == Counter(Counter(word2).values())
```

## [2352. 相等行列对](https://leetcode.cn/problems/equal-row-and-column-pairs/)

中等



相关标签

相关企业



提示



给你一个下标从 **0** 开始、大小为 `n x n` 的整数矩阵 `grid` ，返回满足 `Ri` 行和 `Cj` 列相等的行列对 `(Ri, Cj)` 的数目*。*

如果行和列以相同的顺序包含相同的元素（即相等的数组），则认为二者是相等的。

 

**示例 1：**

![img](assets/ex1.jpg)

```
输入：grid = [[3,2,1],[1,7,6],[2,7,7]]
输出：1
解释：存在一对相等行列对：
- (第 2 行，第 1 列)：[2,7,7]
```

**示例 2：**

![img](assets/ex2.jpg)

```
输入：grid = [[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]
输出：3
解释：存在三对相等行列对：
- (第 0 行，第 0 列)：[3,1,2,2]
- (第 2 行, 第 2 列)：[2,4,2,2]
- (第 3 行, 第 2 列)：[2,4,2,2]
```

 

**提示：**

- `n == grid.length == grid[i].length`
- `1 <= n <= 200`
- `1 <= grid[i][j] <= 105`



**题解**

```python

```

