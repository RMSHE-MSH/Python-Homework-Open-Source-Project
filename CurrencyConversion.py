# Powered by RMSHE;
# 2022.09.1;
# 实时汇率获取&动态美元对主流货币的转换;
# 通过爬取网络中的实时汇率来计算货币转换;
import requests
import re
import time

url = 'http://www.cnhuilv.com/'


class CurrencyConverter:
    head = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'}
    Url = ""
    Currency_Type = ""
    toCurrency_Type = ""

    def GET_ExchangeRate(self):
        ExchangeRate = 0

        obj = re.compile(
            r'<p onClick="check_hld\(' + "'" + self.Currency_Type + "'" + ',' + "'" + self.toCurrency_Type + "'" + ',.*?\);" class=.*?><span>(?P<ExchangeRate>.*?)</span>',
            re.S)

        resp = requests.get(url, self.head)
        result = obj.finditer(resp.text)
        for i in result:
            ExchangeRate = i.group('ExchangeRate')

        resp.close()
        return ExchangeRate

    def SetParameter(self, URL, CurrencyType, toCurrencyType):
        self.Url = URL
        self.Currency_Type = CurrencyType
        self.toCurrency_Type = toCurrencyType

    pass

    def CurrencyCalculation(self, value, Invert):
        ExchangeRate = self.GET_ExchangeRate()

        if Invert == True:
            result = eval(value) / eval(ExchangeRate)
        else:
            result = eval(ExchangeRate) * eval(value)

        Return = {'ExchangeRate': ExchangeRate, 'Result': result}
        return Return


# 本类的我定义的关键字,表示不同的主流货币类型;
# (usd:美元)["人民币","欧元","英镑","澳大利亚元","加拿大元","新加坡元","港币","日元"];
Currency_Type = ["cny", "eur", "gbp", "aud", "cad", "sgd", "hkd", "jpy"]
CC = CurrencyConverter()
for i in Currency_Type:
    CC.SetParameter(url, "usd", i)  # 设置参数(URL,原始货币类型,目标货币类型);注:目前原始货币类型只能为美元;
    Result = CC.CurrencyCalculation("7", False)  # 转换货币(货币面额,反相);如果反相为True,则转换方向会反转;

    # 打印结果;
    print("Current exchange rate: " + Result['ExchangeRate'] + ";\tusd to " + i + ": ", Result['Result'])
    time.sleep(1)  # 访问太频繁有可能会被封IP,适量添加访问延时;
