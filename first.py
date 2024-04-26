class account:
    def __init__(self, acc_no, acc_pass):
        self.acc_no = acc_no
        self.acc_pass = acc_pass


acc1 = account("12345", "abcd")

print(acc1.__acc_no)
print(acc1.__acc_pass)



