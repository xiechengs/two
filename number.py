# 请使用Python/JavaScript完成小代码测试，上传至公共github，并将github链接返回给我们。
# 请不要在github上写任何与TKWw有关的文字作为网络安全问题，否则将被视为代码测试失败给定一个包含数字[0,9]的整数列表，
# 任务是打印出这些数字可能表示的所有字母组合。接下来是数字到字母的映射(就像电话按钮一样)。注意，O和1不映射到任何字母。
# 示例输入:[2、3],输出:ad ae at bd be bf cd ce cf输入 [9]，输出： wxyz
def phoneLetter(digits):
    if not digits:
        return []
    keyboard = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz"
    }
    res = []
    if len(digits) == 0:
        return []
    if len(digits) == 1:
        return keyboard[digits]
    result = phoneLetter(digits[1:])
    for i in result:
        for j in keyboard[digits[0]]:
            res.append((j + i))
    return res

a=input("输入数字: ")
print(phoneLetter(a))
# print(phoneLetter("45"))