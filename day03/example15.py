"""
example15 - 个税计算器（新）居民个人综合所得适用，简要版，合并五险一金专项扣除和专项附加扣除，并假设没有减免收入及减免税额等情况。
适用于当年在同一单位的情况。

Author: larry
Date: 10/2/22

"""
months = int(input("请输入当前月份："))  # 比如现在是10月，则输入10。
month = 1
all_income_sum = 0  # 截止当月的累计总收入（包含五险一金等）
deduct_sum = 0  # 截止当月的专项扣除
acc_tax = 0  # 截止上月末当年的累计税额
while month <= months:
    all_income = float(input(f"请输入{month}月税前收入：（元）"))  # 当月的总收入（包含五险一金）
    all_income_sum += all_income
    deduct = float(input(f"请输入{month}月专项扣除额：（元）")) + 5000  # 当月的专项扣除，5000元为每月固定减除费用
    deduct_sum += deduct
    deducted_all_income_sum = all_income_sum - deduct_sum
    if deducted_all_income_sum <= 36000:
        r = 0.03  # 税率
        q = 0  # 速算扣除数
    elif 36000 < deducted_all_income_sum <= 144000:
        r = 0.10  # 税率
        q = 2520  # 速算扣除数
    elif 144000 < deducted_all_income_sum <= 300000:
        r = 0.20  # 税率
        q = 16920  # 速算扣除数
    elif 300000 < deducted_all_income_sum <= 420000:
        r = 0.25  # 税率
        q = 31920  # 速算扣除数
    elif 420000 < deducted_all_income_sum <= 660000:
        r = 0.30  # 税率
        q = 52920  # 速算扣除数
    elif 660000 < deducted_all_income_sum <= 960000:
        r = 0.35  # 税率
        q = 85920  # 速算扣除数
    else:
        r = 0.45  # 税率
        q = 181920  # 速算扣除数

    all_tax = deducted_all_income_sum * r - q  # 截止当月的当年所交税费
    if all_tax >= 0:
        month_tax = all_tax - acc_tax  # 当月所交税费
    else:
        month_tax = 0
    acc_tax += month_tax  # 截止上月末当年的累计税额

    if all_tax >= 0:
        print(f"{month}月所交税费为{month_tax}元。截止{month}月，当年所交税费为{all_tax}元。")
    else:
        print(f"{month}月所交税费为0元。截止{month}月，当年所交税费为0元。")
    month += 1
