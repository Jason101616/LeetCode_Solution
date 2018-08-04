# TinyURL is a URL shortening service where you enter a URL such as https://leetcode.com/problems/design-tinyurl and it returns a short URL such as http://tinyurl.com/4e9iAk.

# Design the encode and decode methods for the TinyURL service. There is no restriction on how your encode/decode algorithm should work. You just need to ensure that a URL can be encoded to a tiny URL and the tiny URL can be decoded to the original URL.

# 思路1：用hash table来存储每个URL从而加快访问
# 当遇到已存储的longUrl时候直接返回
# 每一个url都有一个编号，对这个编号进行62进制编码
# 这种思路的优势在于不需要反复进行随机数运算，找尚未使用过的编码

# 思路2：如果需要定长的code，比如固定6位数，可以采用如下方案
# 在62个备选character之中随机选取一个，重复6次
# 这种思路的劣势在于后期会出现反复进行随机数运算的情况

class Codec:
    def __init__(self):
        self.url2code = {}
        self.code2url = {}
        self.cnt = 1
        self.choice = string.ascii_letters + string.digits

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.
        
        :type longUrl: str
        :rtype: str
        """
        if longUrl in self.url2code:
            return self.url2code[longUrl]

        # encode the url
        tmp = self.cnt
        answer = ""
        while tmp:
            answer += self.choice[tmp % len(self.choice)]
            tmp = int(tmp / len(self.choice))
        self.cnt += 1
        # add it to the dict
        self.url2code[longUrl] = answer
        self.code2url[answer] = longUrl
        # return the answer
        return answer

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.
        
        :type shortUrl: str
        :rtype: str
        """
        return self.code2url[shortUrl]

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
