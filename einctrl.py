#einctrl

class EinCtrl:

    def __init__(self, acc, acc_name, per, ytd, month, year):
        self.acc = acc
        self.acc_name = acc_name
        self.per = per
        self.ytd = ytd
        self.month = month
        self.year = year

    def description(self):
        return 'ctrl af konto ' + str(self.acc) + ' ' + str(self.acc_name) + ' ' + str(self.month) + ' ' + str(self.year)

    def firstuse(self, acc, per, ytd):
        if self.per == self.ytd and self.ytd != 0:
            print(str(self.acc) + ' ' + str(self.acc_name) + ' !!! First time posting' + '. Amount is : ' +str(self.per))

        else:
            print('ok')
