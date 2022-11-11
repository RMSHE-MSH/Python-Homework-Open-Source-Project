# Powered by RMSHE;
# 2022.11.09;

def gbp_to_rmb(GBP):
    RMB = 8.11 * GBP
    return RMB


def rmb_to_gbp(RMB):
    GBP = RMB / 8.11
    return GBP


def CurrencyConverter(Input: str):
    if Input[-3:] == "GBP":
        return gbp_to_rmb(eval(Input[:-3])), "RMB"
    if Input[-3:] == "RMB":
        return rmb_to_gbp(eval(Input[:-3])), "GBP"


Re = CurrencyConverter(input('输入: '))
print(f"输出: {(Re[0]):.2f}{Re[1]}")

Re = CurrencyConverter(input('输入: '))
print(f"输出: {(Re[0]):.2f}{Re[1]}")
