import numpy_financial as npt

# 每月还款金额(pmt函数)
print("月供:", npt.pmt(0.0578 / 12, 12 * 30, 800000))

# 还款期数(nper函数)
print("还款期数:", npt.nper(0.0578 / 12, -4093.908, 700000))

# 贷款利率(rate函数)
print("贷款利率:", 12 * npt.rate(360, -4093.908, 700000, 0))

