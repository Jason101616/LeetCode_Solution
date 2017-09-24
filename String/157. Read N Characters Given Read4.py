# The API: int read4(char *buf) reads 4 characters at a time from a file.

# The return value is the actual number of characters read. For example, it returns 3 if there is only 3 characters left in the file.

# By using the read4 API, implement the function int read(char *buf, int n) that reads n characters from the file.

# Note:
# The read function will only be called once for each test case.

# The read4 API is already defined for you.
# @param buf, a list of characters
# @return an integer
# def read4(buf):

# 思路：
#         while remain >= 4:
#             read into tmp_buf
#             copy tmp_buf to buf
#             update has_read, remain
#             if cur_read < 4:
#                 return has_read
#
#         read into a tmp_buf
#         if cur_read > remain:
#             copy tmp_buf to buf for remain times
#             update has_read
#             return has_read
#         else:
#             copy tmp buf to buf for cur_read times
#             update has_read
#             return has_read

class Solution(object):
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Maximum number of characters to read (int)
        :rtype: The number of characters read (int)
        """
        remain = n
        has_read = 0
        while remain >= 4:
            tmp_buf = [''] * 4
            cur_read = read4(tmp_buf)
            for i in range(cur_read):
                buf[has_read + i] = tmp_buf[i]
            remain -= cur_read
            has_read += cur_read
            if cur_read < 4:
                return has_read
        
        tmp_buf = [''] * 4
        cur_read = read4(tmp_buf)

        for i in range(min(remain, cur_read)):
            buf[has_read + i] = tmp_buf[i]
        has_read += min(remain, cur_read)
        return has_read
